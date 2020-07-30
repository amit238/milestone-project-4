from django.shortcuts import render, redirect, reverse

# Create your views here.


def view_cart(request):
    """ A view that renders the cart page """
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add plan to shopping cart """
    cart = request.session.get('cart', {})
    cart[item_id] = cart.get(item_id, 1)

    request.session['cart'] = cart
    return render(request, 'cart/cart.html')


def remove_from_cart(request, item_id):
    """Remove a specified product from the cart"""

    cart = request.session.get('cart', {})
    cart.pop(item_id, None)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))