from django.contrib import admin
from .models import User, Category, Sub_category, Product, Order, Contact_store

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'chat_id', 'phone', 'address']
    fields = ['username', 'first_name', 'last_name', 'chat_id', 'phone', 'address']
    search_fields = ['username', 'first_name', 'last_name', 'chat_id', 'phone', 'address']
    ordering = ['username', 'first_name', 'last_name', 'chat_id', 'phone', 'address']
    actions = ['make_published']
    actions = ['delete_queryset']
    list_display_links = ['username', 'first_name', 'last_name', 'chat_id', 'phone', 'address']

    def make_published(self, request, queryset):
        queryset.update(status=True)
    make_published.short_description = "Mark selected stories as published"

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin): 
    list_display = ['name', 'discription']
    fields = ['name', 'discription',]
    search_fields = ['name', 'discription']
    ordering = ['name', 'discription']
    actions = ['make_published']
    list_display_links = ['name', 'discription']

    def make_published(self, request, queryset):
        queryset.update(status=True)
    make_published.short_description = "Mark selected stories as published"

@admin.register(Sub_category)
class Sub_categoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'discription', 'category']
    fields = ['name', 'discription', 'category']
    search_fields = ['name', 'discription', 'category']
    ordering = ['name', 'discription', 'category']
    actions = ['make_published']
    list_display_links = ['name', 'discription', 'category']

    def make_published(self, request, queryset):
        queryset.update(status=True)
    make_published.short_description = "Mark selected stories as published"

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'discription', 'price', 'sub_category', 'image']
    fields = ['name', 'discription', 'price', 'sub_category', 'image']
    search_fields = ['name', 'discription', 'price', 'sub_category', 'image']
    ordering = ['name', 'discription', 'price', 'sub_category', 'image']
    actions = ['make_published']
    list_display_links = ['name', 'discription', 'price', 'sub_category', 'image']

    def make_published(self, request, queryset):
        queryset.update(status=True)
    make_published.short_description = "Mark selected stories as published"


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'count', 'address', 'phone', 'status']
    fields = ['user', 'product', 'count', 'address', 'phone', 'status']
    search_fields = ['user', 'product', 'count', 'address', 'phone', 'status']
    ordering = ['user', 'product', 'count', 'address', 'phone', 'status']
    actions = ['make_published']
    list_display_links = ['user', 'product', 'count', 'address', 'phone', 'status']

    # delete order status true
    def delete_queryset(self, request, queryset):
        queryset.update(status=True)
    delete_queryset.short_description = "Mark selected stories as published"


    def make_published(self, request, queryset):
        queryset.update(status=True)
    make_published.short_description = "Mark selected stories as published"

@admin.register(Contact_store)
class Contact_storeAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'location', 'address']
    fields = ['name', 'phone', 'location', 'address']
    search_fields = ['name', 'phone', 'location', 'address']
    ordering = ['name', 'phone', 'location', 'address']
    actions = ['make_published']
    list_display_links = ['name', 'phone', 'location', 'address']
    

    def make_published(self, request, queryset):
        queryset.update(status=True)
    make_published.short_description = "Mark selected stories as published"

