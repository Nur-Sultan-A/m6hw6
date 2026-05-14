from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import Product
from .serializers import ProductSerializer

from users.permissions import IsAdminOrSeller


class ProductListCreateView(generics.ListCreateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):

        if self.request.method == 'POST':
            return [IsAdminOrSeller()]

        return [AllowAny()]


class ProductUpdateView(generics.UpdateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrSeller]