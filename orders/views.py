from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from carts.models import CartItem
from .forms import OrderForm
import datetime
from .models import Order, Payment, OrderProduct
import os
import json
from django.db import transaction, IntegrityError
from django.contrib.auth.decorators import login_required


@login_required
@transaction.atomic
def payments(request):
    if request.method != "POST":
        return JsonResponse({'error': 'Invalid request'}, status=400)

    try:
        body = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid data'}, status=400)
    order = get_object_or_404(
    Order,
    user=request.user,
    is_ordered=False,
    order_number=body['orderID']
)
    if order.is_ordered:
        return JsonResponse({'error': 'Order already processed'}, status=400)

    # store transaction details inside payment model
    payment = Payment.objects.create(
        user=request.user,
        payment_id=body['transID'],
        payment_method=body['payment_method'],
        amount_paid=order.order_total,
        status=body['status']
    )

    order.payment = payment
    order.is_ordered = True
    order.save()

    # move the cart items to order product table
    cart_items = CartItem.objects.filter(user=request.user)

    for item in cart_items:
        product = item.product

        # check stock BEFORE saving anything
        if product.stock < item.quantity:
            return JsonResponse({'error': 'Insufficient stock'}, status=400)

        orderproduct = OrderProduct(
            order_id=order.id,
            payment=payment,
            user_id=request.user.id,
            product_id=item.product_id,
            quantity=item.quantity,
            product_price=item.product.price,
            ordered=True,
        )
        orderproduct.save()

        # reduce stock
        product.stock -= item.quantity
        product.save()


    # reduce the quantity of sold products

    # clear cart
    CartItem.objects.filter(user=request.user).delete()

    # send order recieved email to customer

    # send order number and transaction id back to sendData method via JsonResponse

    return JsonResponse({
        'order_number': order.order_number,
        'transID': payment.payment_id,
    })

def place_order(request, total=0, quantity=0):
    current_user = request.user

    cart_items = CartItem.objects.filter(user=current_user)
    cart_count = cart_items.count()
    if cart_count <= 0:
        return redirect('store')

    grand_total = 0
    tax = 0
    for cart_item in cart_items:
        total += (cart_item.product.price * cart_item.quantity)
        quantity += cart_item.quantity
    tax = (2 * total) / 100
    grand_total = total + tax

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # store all the billing information inside order table
            data = Order()
            data.user = current_user
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.phone = form.cleaned_data['phone']
            data.email = form.cleaned_data['email']
            data.address_line_1 = form.cleaned_data['address_line_1']
            data.address_line_2 = form.cleaned_data['address_line_2']
            data.country = form.cleaned_data['country']
            data.state = form.cleaned_data['state']
            data.city = form.cleaned_data['city']
            data.order_note = form.cleaned_data['order_note']
            data.order_total = grand_total
            data.tax = tax
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()

            # Generate Order Number
            yr = int(datetime.date.today().strftime('%Y'))
            dt = int(datetime.date.today().strftime('%d'))
            mt = int(datetime.date.today().strftime('%m'))
            d = datetime.date(yr, mt, dt)
            current_date = d.strftime("%Y%m%d")
            order_number = current_date + str(data.id)
            data.order_number = order_number
            data.save()

            order = get_object_or_404(
                Order,
                user=current_user,
                is_ordered=False,
                order_number=order_number
            )
            context = {
                'order': order,
                'cart_items': cart_items,
                'total': total,
                'tax': tax,
                'grand_total': grand_total,
                'client_id': os.getenv('PAYPAL_CLIENT_ID'),
            }    
            return render(request, 'orders/payments.html', context)
        else:
            return redirect('checkout')