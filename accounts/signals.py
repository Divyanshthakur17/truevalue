from cars.models import WishItem,User
from django.db.models.signals import post_save
from django.dispatch import receiver
# from .models import UserProfile


user = User



@receiver(post_save, sender = user)
def create_wishlist(sender,instance,created, **kwargs):
    print(sender)
    print(instance)
    print(created)

    if created:
        WishItem.objects.create(user=instance)

# @receiver(post_save, sender = user)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user = instance)