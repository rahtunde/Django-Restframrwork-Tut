from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()
class UserinlineSerializer(serializers.Serializer):
     url = serializers.HyperlinkedIdentityField(
        view_name='product_datail',
          lookup_field='pk',
          read_only=True
          )
     
     title = serializers.CharField(read_only=True)




class UserPublicSerializer(serializers.Serializer):

    username = serializers.CharField(read_only=True)
    this_is_not_real = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only= True)
    # other_product = serializers.SerializerMethodField(read_only=True)


    # class Meta:
    #      model = User
    #      fields = [
    #           'username',
    #           'this_is_not_real',
    #           'id'

    #      ]


    # def get_other_product(self, obj):
    #     user = obj
    #     my_products_qs = user.product_set.all()[:5]
    #     return UserinlineSerializer(my_products_qs, many=True, context=self.context).data