from django.contrib import admin
from .models import *

# Register your models here.
class SizeAdmin(admin.ModelAdmin):
    list_display=('id', 'size')
    
class CategoryAdmin(admin.ModelAdmin):
    list_display=('id', 'category')

admin.site.register(Product)
admin.site.register(Size, SizeAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Discount)