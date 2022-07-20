from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LNdc5FCSPcqAtPr1ekL2Mk6ym2wMnjYe3ziJEsL4MKbXSfbteRkFeVWN9URaxWrzMFhAWMg0f8CQxkWQiYjhUzt00WUIEYSxe',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)