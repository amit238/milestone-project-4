from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from plans.models import Plans


def cart_contents(request):

    """
    Enables the cart contents to be shown when
    rendering any page on the site.
    """

    cart_items = []
    total = 0
    plan_count = 0
    cart = request.session.get('cart', {})

    for item_id, item_data in cart.items():
        if isinstance(item_data, int):
            plans = get_object_or_404(Plans, pk=item_id)
            total += item_data * plans.price
            plan_count += item_data
            cart_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'plans': plans,
            })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'plan_count': plan_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
