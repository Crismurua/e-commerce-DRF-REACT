from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from products.api import GeneralListApiView
from products.models import Size, Category, Discount, Rating
from products.serializers.general_serializers import SizeSerializer, DiscountSerializer, CategorySerializer, DiscountUpdateSerializer, RatingSerializer

class SizeViewSet(viewsets.GenericViewSet):
    model = Size
    serializer_class = SizeSerializer
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)
    
    def get_object(self):
        return self.get_serializer().Meta.model.objects.filter(id=self.kwargs['pk'], state=True)
    
    @action(detail=False, methods=['GET'])
    def get_sizes(self, request):
        data = Size.objects.filter(state=True)
        data = SizeSerializer(data, many=True)
        return Response(data.data)
    
    def list(self, request):
        data = self.get_queryset()
        data = self.get_serializer(data, many=True)
        data = {
            'total': self.get_queryset().count(),
            'totalNotFiltered': self.get_queryset().count(),    
            'rows': data.data,        
        }
        return Response(data)
    
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Size successfully created!'}, status=status.HTTP_201_CREATED)
        return Response({'message': '', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        if self.get_object().exists():
            data = self.get_object().get()
            data = self.get_serializer(data)
            return Response(data.data)
        return Response({'message': '', 'error': 'Size not found!'}, status=status.HTTP_404_NOT_FOUND)
    
    def update(self, request, pk=None):
        if self.get_object().exists():
            serializer = self.serializer_class(instance=self.get_object().get(), data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Size successfully updated!'}, status=status.HTTP_200_OK)
            return Response({'message': '', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk=None):
        if self.get_object().exists():
            self.get_object().delete()
            return Response({'message': 'Size successfully deleted!'}, status=status.HTTP_200_OK)
        return Response({'message': '', 'error': 'Size not found'}, status=status.HTTP_404_NOT_FOUND)
    

class CategoryViewSet(viewsets.GenericViewSet):
    model = Category
    serializer_class = CategorySerializer
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)
    
    def get_object(self):
        return self.get_serializer().Meta.model.objects.filter(id=self.kwargs['pk'], state=True)
    
    @action(detail=False, methods=['GET'])
    def get_categories(self, request):
        data = Category.objects.filter(state=True)
        data = CategorySerializer(data, many=True)
        return Response(data.data)
    
    def list(self, request):
        data = self.get_queryset()
        data = self.get_serializer(data, many=True)
        data = {
            'total': self.get_queryset().count(),
            'totalNotFiltered': self.get_queryset().count(),    
            'rows': data.data,        
        }
        return Response(data)
    
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Category successfully created!'}, status=status.HTTP_201_CREATED)
        return Response({'message': '', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        if self.get_object().exists():
            data = self.get_object().get()
            data = self.get_serializer(data)
            return Response(data.data)
        return Response({'message': '', 'error': 'Category not found!'}, status=status.HTTP_404_NOT_FOUND)
    
    def update(self, request, pk=None):
        if self.get_object().exists():
            serializer = self.serializer_class(instance=self.get_object().get(), data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Category successfully updated!'}, status=status.HTTP_200_OK)
            return Response({'message': '', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk=None):
        if self.get_object().exists():
            self.get_object().delete()
            return Response({'message': 'Category successfully deleted!'}, status=status.HTTP_200_OK)
        return Response({'message': '', 'error': 'Measure Unit not found'}, status=status.HTTP_404_NOT_FOUND)
    
    
class DiscountViewSet(viewsets.GenericViewSet):
    model = Discount
    serializer_class = DiscountSerializer
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)
    
    def get_object(self):
        return self.get_serializer().Meta.model.objects.filter(id=self.kwargs['pk'], state=True)
    
    @action(detail=False, methods=['GET'])
    def get_discounts(self, request):
        data = Discount.objects.filter(state=True)
        data = DiscountSerializer(data, many=True)
        return Response(data.data)
    
    def list(self, request):
        data = self.get_queryset()
        data = self.get_serializer(data, many=True)
        data = {
            'total': self.get_queryset().count(),
            'totalNotFiltered': self.get_queryset().count(),    
            'rows': data.data,        
        }
        return Response(data)
    
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Discount successfully created!'}, status=status.HTTP_201_CREATED)
        return Response({'message': '', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        if self.get_object().exists():
            data = self.get_object().get()
            data = self.get_serializer(data)
            return Response(data.data)
        return Response({'message': '', 'error': 'Discount not found!'}, status=status.HTTP_404_NOT_FOUND)
    
    def update(self, request, pk=None):
        if self.get_object().exists():
            serializer = self.serializer_class(instance=self.get_object().get(), data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Discount successfully updated!'}, status=status.HTTP_200_OK)
            return Response({'message': '', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk=None):
        if self.get_object().exists():
            self.get_object().delete()
            return Response({'message': 'Discount successfully deleted!'}, status=status.HTTP_200_OK)
        return Response({'message': '', 'error': 'Measure Unit not found'}, status=status.HTTP_404_NOT_FOUND)
    
    
class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer  
      