from django.db.models.signals import post_save
from django.dispatch import receiver

from reviews.models import Restaurant
from reviews.models.top_restaurant import TopRestaurant


@receiver(post_save, sender=Restaurant, weak=False)
def update_attributes_land(
        sender, instance, raw, using, update_fields, weak=False,
        **kwargs  # pylint: disable=R0913 W0613
):
    restaurants = Restaurant.objects.order_by('-score')
    max_top = len(restaurants)
    min_top = 0
    for restaurant in restaurants:
        obj, status = TopRestaurant.objects.get_or_create(
            restaurant=restaurant,
        )
        obj.top = min_top + 1
        obj.score = restaurant.score
        if min_top != max_top:
            min_top += 1
        obj.save()
