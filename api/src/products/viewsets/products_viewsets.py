from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, MultiPartParser

from products.utils import validate_files
from products.serializers.product_serializers import ProductSerializer, ProductListSerializer

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    parser_classes = (JSONParser, MultiPartParser)
    
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()
    
    def list(self, request):
        product_serializer = self.get_serializer(self.get_queryset(), many=True)
        data = {
            'total': self.get_queryset().count(),
            'totalNotFiltered': self.get_queryset().count(),
            'rows': product_serializer.data,
        }
        return Response(data, status=status.HTTP_200_OK)
    
    def create(self, request):
        data = validate_files(request.data, 'image')
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return  Response({'message': 'Product successfully created!'}, status=status.HTTP_201_CREATED)
        return Response({'message': '', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def find(self, request, pk=None):
        product = self.get_queryset(pk)
        if product:
            product_serializer = ProductListSerializer(product)
            return Response(product_serializer.data, status=status.HTTP_200_OK)
        return Response({'error': 'Product not found!'}, status=status.HTTP_404_NOT_FOUND)
    
    def update(self, request, pk=None):
        if self.get_queryset(pk):
            data = validate_files(request.data, 'imagen', True)
            product_serializer = self.serializer_class(self.get_queryset(pk), data=data)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response({'message': 'Product successfully updated!'}, status=status.HTTP_200_OK)
            return Response({'message': '', 'error': product_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk=None):
        product = self.get_queryset().filter(id=pk).first()
        if product:
            product.state = False
            product.save()
            return Response({'message': 'Product successfully deleted!'}, status=status.HTTP_200_OK)
        return Response({'error': 'Product not found!'}, status=status.HTTP_404_NOT_FOUND)
            
        
    
