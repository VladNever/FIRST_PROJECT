from django.db import models
from basket.models import Basket

class Order(models.Model):
    CANCELED = 'Отменён'
    IN_PROCESSING = 'В обработке'
    DELIVERED = 'Доставлен'
    STATUS_ORDER = (
        (CANCELED, 'Отменён'),
        (IN_PROCESSING, 'В обработке'),
        (DELIVERED, 'Доставлен'),
    )
    basket = models.OneToOneField(
        Basket,
        on_delete = models.PROTECT,
        related_name='order',
    )
    status = models.CharField(
        verbose_name="Статус",
        max_length=20,
        choices=STATUS_ORDER,
        default=IN_PROCESSING)
    delivery_address = models.TextField(
        "Адрес доставки"
    )
    contact_phone = models.CharField(
        "Контактный телефон",
        max_length=50
    )
    created = models.DateTimeField(
        "Создан",
        auto_now=False,
        auto_now_add=True
    )
    updated = models.DateTimeField(
        "Обновлён",
        auto_now=True,
        auto_now_add=False
    )
    cancel_order = models.BooleanField(
        verbose_name="Отменить заказ",
        default=False
    )
    deliver_order = models.BooleanField(
        verbose_name="Заказ доставлен",
        default=False
    )
    class Meta:
        permissions = [
            ("view_all_orders", "Can view all orders"),
        ]


    def __str__(self):
        return f'Order #{self.pk}'