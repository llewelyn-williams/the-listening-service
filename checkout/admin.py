from django.contrib import admin
from .models import Order
# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('order_number', 'date',
                       'order_total', 'stripe_pid'
                       )

    fields = ('order_number', 'full_name',
              'email', 'phone_number',
              'street_address1', 'street_address2',
              'town_or_city', 'county',
              'postcode', 'country',
              'date', 'talking_topics',
              'order_total', 'stripe_pid',)

    list_display = ('date', 'full_name',
                    'order_total','order_number', 
                    )

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)
