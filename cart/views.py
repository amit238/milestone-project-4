from django.shortcuts import render, redirect, reverse

# Create your views here.

def view_cart(request):
    """ A view that renders the cart page """

    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """ Add plan to shopping cart """
    
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    request.session['cart'] = cart
    return redirect(redirect_url)
    

    