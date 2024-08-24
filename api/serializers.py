from rest_framework import serializers
from .models import Meal, Rating 
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User



class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ['id', 'title', 'description','avg_rating','number_of_rating']

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'stars', 'user', 'meal']
        
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=User
        fields=['id','username','email','password']
        extra_kwargs={'password' : {'write_only' : True ,'required' : True} }
        
        # def create(self, validated_data):
        #     user=User.objects.create_user(**validated_data)
        #     Token.objects.update_or_create(user=user)
        #     # Token.objects.create(user=user)
        #     return user
        