from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt. tokens import RefreshToken
from .models import Product, Review, ShippingAddress, Order, OrderItem

class UserSerializer(serializers.ModelSerializer):
    # name property coming from get_name functin blow
    name = serializers.SerializerMethodField(read_only=True)
    _id = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ['id', '_id', 'username','email','name', 'isAdmin']
        
    # get name instead of creating new feild
    def get_name (self, obj):
        name = obj.first_name
        if name == "":
            name = obj.email
        return name
    
    # get id instead of creating new feild
    def get__id (self, obj):
        return obj.id
    
    # get admin instead of creating new feild
    def get_isAdmin (self, obj):
        return obj.is_staff
    
class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ['id', '_id', 'username','email','name', 'isAdmin', 'token']
        
    # get id instead of creating new feild
    def get_token (self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)
        
class ProductSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = "__all__"
    
    def get_reviews (self, obj):
        reviews = obj.review_set.all()
        serializer = ReviewSerializer(reviews, many=True)
        return serializer.data

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = "__all__"

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    orderItems = serializers.SerializerMethodField(read_only=True)
    shippingAddress = serializers.SerializerMethodField(read_only=True)
    user = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Order
        fields = "__all__"
        
    def get_orderItems (self, obj):
        items = obj.orderitem_set.all()
        serializer = OrderItemSerializer(items, many=True)
        return serializer.data
    
    def get_shippingAddress (self, obj):
        try:
            address = obj.shippingaddress
            serializer = ShippingAddressSerializer(address, many=False)
            return serializer.data
        except:
            address = False
            return address
        
    def get_user (self, obj):
        user = obj.user
        serializer = UserSerializer(user, many=False)
        return serializer.data
    