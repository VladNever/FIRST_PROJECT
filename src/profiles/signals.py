from django.db.models.signals import pre_save, post_save, post_migrate, pre_migrate, post_init, pre_init
from django.dispatch import receiver
from .models import Profile
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission 


@receiver(post_save, sender=Profile)
def add_group_admin(sender, created, **kwargs):
    if created:
        perms_all = Permission.objects.all()
        perms_admin = perms_all
        gr_admin, created = Group.objects.get_or_create(
            name="Admin", 
            defaults = {}
            )
        gr_admin.permissions.set(perms_admin)
    else:
        pass


@receiver(post_save, sender=Profile)
def add_group_managers(sender, created, **kwargs):
    if created:
        perms_all = Permission.objects.all()
        perms_managers = [
            perms_all.get(name="Can change profile"),
            perms_all.get(name="Can delete profile"),
            perms_all.get(name="Can add books"),
            perms_all.get(name="Can change books"),
            perms_all.get(name="Can delete books"),
            perms_all.get(name="Can add genre"),
            perms_all.get(name="Can change genre"),
            perms_all.get(name="Can delete genre"),
        ]
        gr_managers, created = Group.objects.get_or_create(
            name="Managers", 
            defaults = {}
            )
        gr_managers.permissions.set(perms_managers)
    else:
        pass


@receiver(post_save, sender=Profile)
def add_group_customers(sender, created, **kwargs):
    if created:
        perms_all = Permission.objects.all()
        perms_customers = [
            perms_all.get(name="Can change profile"),
            perms_all.get(name="Can delete profile")
        ]
        gr_customers, created = Group.objects.get_or_create(
            name="Customers", 
            defaults = {}
            )
        gr_customers.permissions.set(perms_customers)
    else:
        pass


@receiver(post_save, sender=Profile)
# created - если сущность только создана, а не сохранялась 
def set_group(sender, instance, created,**kwargs):
    #if created:
        if instance.is_superuser:
            gr = Group.objects.get(
            name="Admin"
            )
            instance.groups.add(gr)
        else:
            pass
        if instance.is_staff:
            gr = Group.objects.get(
            name="Managers"
            )
            instance.groups.add(gr)
        else:
            pass
        if not (instance.is_superuser or instance.is_staff):
            gr = Group.objects.get(
            name="Customers"
            )
            instance.groups.add(gr)
        else:
            pass
    #else:
    #    pass




