from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Meal, Rating
from .serializers import MealSerializer, RatingSerializer

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status , filters
from rest_framework.authentication import TokenAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly
# Create your views here.


class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    filter_backends= [filters.SearchFilter]
    search_fields=['title']

    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]

    #1 stars from request data
    #2 user or username request data
    #3 pk(meal) from URL
    @action(detail=True , methods=['post'])
    def rate_meal(self , request , pk=None):
        if 'stars' in request.data:
            
            '''
                Create or Update Rating
            '''
            
            meal =Meal.objects.get(id=pk)
            # username =request.data['username']
            # user=User.objects.get(username=username)
            user=request.user# ما رح مرر الuser ولكن رح مرر ال troken وهو لحالو رح يعرف مين الuser
            #print(user)
            stars=request.data['stars']
            
            try:
                #Update
                
                rating_obj=Rating.objects.get(meal=meal.id,user=user.id)
                rating_obj.stars=stars
                rating_obj.save()
                serializer=RatingSerializer(rating_obj,many=False)
                json={
                    'message':'Meal Rate Updated',
                    'result':serializer.data
                }
                return Response(json,status=status.HTTP_200_OK)
            
            except:
                #Create
                
                rating_obj=Rating.objects.create(meal=meal,user=user,stars=stars)
                serializer = RatingSerializer(rating_obj, many=False)
                json = {
                    'message': 'Meal Rate Created',
                    'result': serializer.data
                }
                return Response(json,status=status.HTTP_200_OK)
            
        else:
            response_message={
            'message':'Stars Not Provided'
            }
            return Response(response_message,status=status.HTTP_400_BAD_REQUEST)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    
    def update(self , request , *args , **kwargs):
        response={
            "message":"Invalid way to URL Update rating"
        }
        return Response(response,status=status.HTTP_400_BAD_REQUEST)
    
    def create(self , request , *args , **kwargs):
        response={
            "message":"Invalid way to URL Create rating"
        }
        return Response(response,status=status.HTTP_400_BAD_REQUEST)