from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from django.http import Http404
from django.shortcuts import get_object_or_404


from .models import Product
from .serializers import ProductSerializer


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')or None 
        if content is None:
            content = title
        serializer.save(content=content)

product_list_create_view = ProductListCreateAPIView.as_view()


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'


product_detail_view = ProductDetailAPIView.as_view()

# class ProductListAPIView(generics.ListAPIView):
#     """
#     not using this method yet
#     """
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


# product_list_view = ProductListAPIView.as_view()


@api_view(['GET', 'POST'])
def product_alt_view(request, pk = None, **args):

    method = request.method
    
    if method == "GET":
        if pk is not None:
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)
        
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)
    
    if method == 'POST':

        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content')or None 
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"Invalid": "Invaid data"}, status=400)
    