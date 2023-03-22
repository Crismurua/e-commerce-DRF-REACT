from django.contrib import admin
from .models import *

# Register your models here.
class MeasureUnitAdmin(admin.ModelAdmin):
    list_display=('id', 'measure_unit')
    
class CategoryAdmin(admin.ModelAdmin):
    list_display=('id', 'category')

admin.site.register(Product)
admin.site.register(MeasureUnit, MeasureUnitAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Discount)