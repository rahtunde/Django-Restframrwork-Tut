from rest_framework import serializers
from rest_framework.reverse import reverse

from api.serializers import UserPublicSerializer
from . import validators
from .models import Product




class ProductinlineSerializer(serializers.Serializer):
     url = serializers.HyperlinkedIdentityField(
        view_name='product_datail',
          lookup_field='pk',
          read_only=True
          )
     
     title = serializers.CharField(read_only=True)

class ProductSerializer(serializers.ModelSerializer):

    owner = UserPublicSerializer(source='user',read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product_datail',
          lookup_field='pk')

    title = serializers.CharField(validators=[validators.unique_product_title,validators.validate_tiltle_no_hello])

    class Meta:
        model = Product
        fields = [
            'owner',
            'url',
            'edit_url',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'public',
           
        ]


    # def get_my_user_data(self, obj):
    #     return {
    #         'username': obj.user.username
    #     }

  

    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product_edit", kwargs= {"pk": obj.pk},request=request)
    

