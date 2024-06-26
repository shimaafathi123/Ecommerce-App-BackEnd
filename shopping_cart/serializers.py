from rest_framework import serializers
from .models import Cart, CartItem
from product.serializers import ProductSerializer
from django.core.validators import MinValueValidator

class AddToCartSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField(validators=[MinValueValidator(1)] ,default =1)

    class Meta:
        model = CartItem
        fields = ['id','product', 'quantity', 'date_added']

    def create(self, validated_data):
        product = validated_data['product']
        quantity = validated_data['quantity']
        user = validated_data.get('user')
        
        cart, created = Cart.objects.get_or_create(user=user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

        if not created:
            cart_item.quantity += quantity
        else:
            cart_item.quantity = quantity

        cart_item.save()
        return cart_item

from rest_framework import serializers
from .models import CartItem

class UpdateCartSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CartItem
        fields = ['product', 'quantity', 'date_added']
    
    def update(self, instance, validated_data):
        action = validated_data.get('action')
        if action not in ('INCREASE', 'DECREASE'):
            raise serializers.ValidationError({'error': "Action can only be 'INCREASE' or 'DECREASE'"})
        
        if action == 'INCREASE':
            instance.quantity += 1
        elif action == 'DECREASE' and instance.quantity > 1:  # Corrected condition
            instance.quantity -= 1
        instance.save()
        
        if instance.quantity == 0:
            instance.delete()

        return instance

    
class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = CartItem
        fields = "__all__"

class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True, read_only=True)
    class Meta:
        model = Cart
        fields = ['id','cart_items']
        
    