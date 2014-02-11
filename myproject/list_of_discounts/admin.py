from django.contrib import admin

from list_of_discounts.models import Store_lists_of_discounts

class Store_lists_of_discounts_admin(admin.ModelAdmin):
    list_display = ('date_save', )
    list_filter = ['date_save']
    search_fields = ['data']

admin.site.register(Store_lists_of_discounts, Store_lists_of_discounts_admin)