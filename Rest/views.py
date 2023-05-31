from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view,permission_classes
from django.contrib.auth.models import User

# Create your views here.
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated,])
def index(request):
    if request.method == 'POST':
        name = request.data['name']
        age = request.data['age']
        print(name,age)
        return Response({'name':name,'age':age})
    context={
        'name': "shovick",
        'age': "24"
    }
    return Response(context)
#a= User.objects.filter(a=a).exists()