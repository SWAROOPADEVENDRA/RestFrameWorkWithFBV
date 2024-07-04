from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response

from rest_framework.decorators import api_view,permission_classes

from app.models import *

from app.serializers import *

from rest_framework.permissions import IsAuthenticated

@api_view(['GET','POST'])
def school(request):

    return Response({'message':'hi all'})


@api_view(['GET','POST'])

#IsAuthenticated is used for user get the data after login the admin
@permission_classes([IsAuthenticated])

def students(request):

    LSO=Student.objects.all()
    
    #many=True is used for SMS is get only one object at a time,so we can use many=True
    #it will give all user inputs
    MSSO=StudentModelSerializers(LSO,many=True)

    return Response(MSSO.data)