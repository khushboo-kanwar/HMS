from django.contrib import admin # type: ignore
from .models import (
    Restaurant, MenuCategory, MenuItem, Reservation, Order,
    OrderItem, Review, RestaurantImage, 
    Diet_and_Nutrition
)

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email', 'opening_hours')
    search_fields = ('name', 'email', 'phone_number')
    list_filter = ('opening_hours',)


@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'restaurant', 'category', 'price', 'is_available')
    list_filter = ('restaurant', 'category', 'is_available')
    search_fields = ('name',)


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('guest_name', 'restaurant', 'reservation_date', 'number_of_guests')
    list_filter = ('restaurant', 'reservation_date')
    search_fields = ('guest_name', 'guest_email', 'guest_phone')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('guest_name', 'restaurant', 'order_date', 'total_price')
    list_filter = ('restaurant', 'order_date')
    search_fields = ('guest_name', 'guest_email', 'guest_phone')


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'menu_item', 'quantity', 'price')
    list_filter = ('menu_item',)
    search_fields = ('menu_item__name', 'order__guest_name')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('guest_name', 'restaurant', 'rating', 'review_date')
    list_filter = ('restaurant', 'rating')
    search_fields = ('guest_name',)


@admin.register(RestaurantImage)
class RestaurantImageAdmin(admin.ModelAdmin):
    list_display = ('restaurant', 'uploaded_at')
    list_filter = ('restaurant',)
    search_fields = ('restaurant__name',)




@admin.register(Diet_and_Nutrition)
class DietAndNutritionAdmin(admin.ModelAdmin):
    list_display = ('name', 'restaurant', 'created_at', 'updated_at')
    list_filter = ('restaurant',)
    search_fields = ('name',)
