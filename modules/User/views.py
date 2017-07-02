from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

import requests

# Create your views here.
@api_view(['POST'])
def instagram(request):
    params = {'access_token':request.data['access_token']}
    data = requests.get('https://api.instagram.com/v1/users/self/', params=params).json()
    return Response({"data":data})