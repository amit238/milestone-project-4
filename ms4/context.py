from django.shortcuts import get_object_or_404
from plan.models import Plan


def cart_context(request):
    """
    Enables the cart contents to be shown when
    rendering any page on the site.
    """

    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    plan_count = 0

    for (id, quantity) in cart.items():
        plan = get_object_or_404(Plan, pk=id)
        total += quantity * plan.price
        plan_count += quantity
        cart_items.append({'plan.id': plan.id, 'quantity': quantity,
                          'plan': plan})

    return {'cart_items': cart_items, 'total': total,
            'plan_count': plan_count}