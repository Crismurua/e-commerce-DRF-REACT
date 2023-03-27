from django.db import models
import uuid

class BaseModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, db_index=True, editable=False)
    state = models.BooleanField(default=True)
    created_date = models.DateField(auto_now=False, auto_now_add=True)
    modified_date = models.DateField(auto_now=True, auto_now_add=False)
    deleted_date = models.DateField(auto_now=True, auto_now_add=False)
    
    class Meta:
        abstract=True
        verbose_name='Base Model'
        verbose_name_plural='Base Models'
        
class Size(BaseModel):
    size = models.CharField(max_length=50, blank=False, null=False, unique=True)
    
    class Meta:
        verbose_name='Size'
        verbose_name_plural='Sizes'
        
    def __str__(self):
        return self.measure_unit
    
class Category(BaseModel):
    category = models.CharField(max_length=50, blank=False, null=False, unique=True)

    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categories'
        
    def __str__(self):
        return self.category
    
class Product(BaseModel):
    
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, db_index=True, editable=False)
    name = models.CharField(max_length=150, unique=True, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    image = models.ImageField(upload_to='products/', null=True, blank=True, default='products/default_product.png')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    size = models.ForeignKey(Size, on_delete=models.CASCADE, verbose_name='Measure Unit', null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category', null=True)  
    
    class Meta:
        verbose_name='Product'
        verbose_name_plural='Products'
        
    def __str__(self):
        return self.name
    
class Discount(BaseModel):
    discount_value = models.PositiveSmallIntegerField(default=0)
    category_product = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Discount')
    
    class Meta:
        verbose_name='Discount'
        verbose_name_plural='Discounts'
        
    def __str__(self):
        return f'Discount: {self.discount_value} On Category: {self.category_product}'
    