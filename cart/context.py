from django.shortcuts import get_object_or_404
from plans.models import Plans


def cart_contents(request):
    """
    Enables the cart contents to be shown when
    rendering any page on the site.
    """

    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    product_count = 0

    for (id, quantity) in cart.items():
        plans = get_object_or_404(Plans, pk=id)
        total += quantity * plans.price
        product_count += quantity
        cart_items.append({'id': id, 'quantity': quantity,
                          'plans': plans})

    return {'cart_items': cart_items, 'total': total,
            'product_count': product_count}