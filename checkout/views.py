from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.


def checkout(request):
    """ Returns the checkout page """
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Theres nothing in your cart")
        return redirect(reverse('plans'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HAU5ZDaUTV7lKMLHZAIOs2myhL850DYnpndsv3ACcRB7YlMq2vtZqVQ4K3XNLuZRAEmtoE3dGFzivRgTzRywrez00in3JBTqF',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)