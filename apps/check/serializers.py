
from rest_framework import serializers


class ProductSerializer(serializers.Serializer):
    """Сериализатор продуктов"""
    product_id = serializers.CharField(max_length=255)
    quantity = serializers.IntegerField(min_value=1)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    category = serializers.CharField(max_length=255)


class ReceivingCheckSerializer(serializers.Serializer):
    """Сериализатор получения чеков"""
    transaction_id = serializers.CharField(max_length=255)
    timestamp = serializers.DateTimeField()
    items = ProductSerializer(many=True)
    total_amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    nds_amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    tips_amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    payment_method = serializers.CharField(max_length=255)
    place_name = serializers.CharField(max_length=255, required=False)

