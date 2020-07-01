from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    name = 'profiles'

    def ready(self):
        from .signals import add_group_admin
        from .signals import add_group_managers
        from .signals import add_group_customers
        from .signals import set_group


