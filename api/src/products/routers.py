from rest_framework.routers import DefaultRouter
from products.viewsets.general_viewsets import *
from products.viewsets.products_viewsets import ProductViewSet

router = DefaultRouter()

router.register(r'products', ProductViewSet, basename='products')
router.register(r'sizes', SizeViewSet, basename='sizes')
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'discounts', DiscountViewSet, basename='discounts')

urlpatterns = router.urls
