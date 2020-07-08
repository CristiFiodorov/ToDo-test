from django.contrib import admin
from .models import ToDoList, Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ('todolist', 'text')
    # spui ce vrei sa arate cand pui adresa aceasta http://127.0.0.1:8000/admin/main/item/


admin.site.register(ToDoList)
admin.site.register(Item, ItemAdmin)
