from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from reviews.models import Restaurant, Review
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


@receiver(pre_save, sender=Review)
def update_score_review(
        sender, instance, raw, using, update_fields, weak=False,
        **kwargs  # pylint: disable=R0913 W0613
):
    instance.score = int(
        (int(instance.score_service) + int(instance.score_food) + int(instance.score_environment) + int(
            instance.score_quality_price)) / 4)


@receiver(post_save, sender=Review)
def sig1(
        sender, instance, raw, using, update_fields, weak=False,
        **kwargs  # pylint: disable=R0913 W0613
):
    aux = 0
    site = Restaurant.objects.filter(id=instance.place.id).first()
    score = Review.objects.filter(place_id=instance.place.id)
    for i in score:
        aux = int(i.score) + aux
    if int(len(score)) == 0:
        site.score = 0
    else:
        site.score = int(aux / len(score))

    site.save()


@receiver(pre_save, sender=Restaurant)
def sig2(
        sender, instance, raw, using, update_fields, weak=False,
        **kwargs  # pylint: disable=R0913 W0613
):
    instance.count_reviews = Review.objects.filter(place__id=instance.id).count()


@receiver(pre_save, sender=Restaurant)
def sig3(
        sender, instance, raw, using, update_fields, weak=False,
        **kwargs  # pylint: disable=R0913 W0613
):
    aux = 0
    aux1 = 0
    aux2 = 0
    aux3 = 0
    r = Review.objects.filter(place__id=instance.id)
    for i in r:
        aux = int(i.score_food) + aux
        aux1 = int(i.score_service) + aux1
        aux2 = int(i.score_environment) + aux2
        aux3 = int(i.score_quality_price) + aux3
    if int(len(r)) == 0:
        instance.score_food = 0
        instance.score_service = 0
        instance.score_environment = 0
        instance.score_quality_price = 0
    else:
        instance.score_food = int(aux / len(r))
        instance.score_service = int(aux1 / len(r))
        instance.score_environment = int(aux2 / len(r))
        instance.score_quality_price = int(aux3 / len(r))

    # instance.score_food = int(aux / len(r))
    # instance.score_service = int(aux1 / len(r))
    # instance.score_environment = int(aux2 / len(r))
    # instance.score_quality_price = int(aux3 / len(r))
