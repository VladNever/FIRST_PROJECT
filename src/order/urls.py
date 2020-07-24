from django.urls import path
from order.views import CreateOrder, ListOrders, CanceledStatusOrder, ListOrdersManager, DetailOrderManager, DeliveredStatusOrder

app_name = "order"


urlpatterns = [
    path('create/', CreateOrder.as_view(), name="create"),
    path('list/', ListOrders.as_view(), name="list"),
    path('canceled_status/<int:pk>', CanceledStatusOrder.as_view(), name="canceled_status"),
    path('list_manager/', ListOrdersManager.as_view(), name="list_manager"),
    path('detail_manager/<int:pk>', DetailOrderManager.as_view(), name="detail_manager"),
    path('delivered_status/<int:pk>', DeliveredStatusOrder.as_view(), name="delivered_status"),
]