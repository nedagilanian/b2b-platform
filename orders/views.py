from rest_framework import viewsets, permissions
from .models import Order, OrderItem,Payment 
from .serializers import OrderSerializer, OrderItemSerializer, PaymentSerializer
import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter



class OrderFilter(django_filters.FilterSet):
    status = django_filters.CharFilter(field_name='status', lookup_expr='icontains')
    min_total_price = django_filters.NumberFilter(field_name='total_price', lookup_expr='gte')
    max_total_price = django_filters.NumberFilter(field_name='total_price', lookup_expr='lte')
    start_date = django_filters.DateFilter(field_name='created_at', lookup_expr='gte')
    end_date = django_filters.DateFilter(field_name='created_at', lookup_expr='lte')

    class Meta:
        model = Order
        fields = ['status', 'min_total_price', 'max_total_price', 'start_date', 'end_date']
    

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend,SearchFilter)
    filterset_class = OrderFilter
    search_fields = ['id', 'user__username']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAuthenticated]


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

