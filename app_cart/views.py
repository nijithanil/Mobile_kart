from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from app_home.models import *
from django.core.exceptions import ObjectDoesNotExist
import razorpay
from django.views.decorators.csrf import csrf_exempt

client = razorpay.Client(auth=("YOUR_ID", "YOUR_SECRET"))


# Create your views here.

def cart_details(request, ct_items=0, tot=0, count=0, total=0):
    try:
        ct = cartlist.objects.get(cart_id=c_id(request))
        ct_items = item.objects.filter(cart=ct, active=True)
        shippingx_charge = 50
        for i in ct_items:
            tot += (i.prodt.off_prize2 * i.quan)
            total += (i.prodt.off_prize2 * i.quan + shippingx_charge)

            count += i.quan

    except ObjectDoesNotExist:
        return render(request, 'Cart.html')
    return render(request, 'Cart.html', {'ci': ct_items, 't': tot, 'total': total, 'cn': count})


def c_id(request):
    ct_id = request.session.session_key
    if not ct_id:
        ct_id = request.session.create()
    return ct_id


def add_cart(request, product_id):
    prod = products.objects.get(id=product_id)
    try:
        ct = cartlist.objects.get(cart_id=c_id(request))
    except cartlist.DoesNotExist:
        ct = cartlist.objects.create(cart_id=c_id(request))
        ct.save()
    try:
        c_item = item.objects.get(prodt=prod, cart=ct)
        if c_item.quan < c_item.prodt.stock:
            c_item.quan += 1
        c_item.save()
    except item.DoesNotExist:
        c_items = item.objects.create(prodt=prod, quan=1, cart=ct)
        c_items.save()
    return redirect('cartdetails')


def min_cart(request, product_id):
    ct = cartlist.objects.get(cart_id=c_id(request))
    prod = get_object_or_404(products, id=product_id)
    c_items = item.objects.get(prodt=prod, cart=ct)
    if c_items.quan > 1:
        c_items.quan -= 1
        c_items.save()
    else:
        c_items.delete()
    return redirect('cartdetails')


def cart_delete(request, product_id):
    ct = cartlist.objects.get(cart_id=c_id(request))
    prod = get_object_or_404(products, id=product_id)
    c_items = item.objects.get(prodt=prod, cart=ct)
    c_items.delete()
    return redirect('cartdetails')


def address_page(request):
    if request.method == 'POST':
        amount: 50000
        order_currency: 'INR'
        client = razorpay.Client(
            auth=('rzp_test_tLsuerhwpepX4n', 'hjMbtAd9WeCdhpi84jQL0wyo'))

        payment = client.order.create({'amount': 'amount', 'currency': 'INR', 'payment_capture': '1'})
    return render(request, 'place_order_page.html')


def success(request):
    return render(request, "success.html")
