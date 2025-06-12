from rest_framework import serializers # type: ignore
from .models import (
    Restaurant, MenuCategory, MenuItem, Reservation, Order,
    OrderItem, Review, RestaurantImage, RestaurantOrderPayment,
    Diet_and_Nutrition
)

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCategory
        fields = '__all__'


class MenuItemSerializer(serializers.ModelSerializer):
    restaurant = serializers.StringRelatedField()
    category = serializers.StringRelatedField()

    class Meta:
        model = MenuItem
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    restaurant = serializers.StringRelatedField()

    class Meta:
        model = Reservation
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    restaurant = serializers.StringRelatedField()

    class Meta:
        model = Order
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    order = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all())
    menu_item = serializers.StringRelatedField()

    class Meta:
        model = OrderItem
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    restaurant = serializers.StringRelatedField()

    class Meta:
        model = Review
        fields = '__all__'


class RestaurantImageSerializer(serializers.ModelSerializer):
    restaurant = serializers.StringRelatedField()

    class Meta:
        model = RestaurantImage
        fields = '__all__'


class RestaurantOrderPaymentSerializer(serializers.ModelSerializer):
    order = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all())

    class Meta:
        model = RestaurantOrderPayment
        fields = '__all__'


class DietAndNutritionSerializer(serializers.ModelSerializer):
    restaurant = serializers.StringRelatedField()

    class Meta:
        model = Diet_and_Nutrition
        fields = '__all__'
