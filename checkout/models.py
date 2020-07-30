import uuid

from django.db import models
from plans.models import Plans
from django.conf import settings

from plans.models import Plans


class Order(models.Model):

    order_number = models.CharField(max_length=32, null=False, editable=False)
    plan = models.ForeignKey(Plans, null=True, on_delete=models.SET_NULL)
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    date = models.DateField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def __str__(self):
        return '{0}-{1}-{2}'.format(self.id, self.date, self.full_name)


class OrderLineItem(models.Model):

    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, null=False)
    plan = models.ForeignKey(Plans, on_delete=models.CASCADE,null=False)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return '{0} {1} @ {2}'.format(self.quantity, self.plan.name,
                                      self.plan.price)