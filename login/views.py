from django.shortcuts import render
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse

def login_page(request):
    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')


@api_view(['POST'])
def token_login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)
    if user is not None:
        refresh = RefreshToken.for_user(user)
        return JsonResponse({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
    return JsonResponse({'error': 'Invalid Credentials'}, status=401)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def hello(request):
    user= request.user
    print(f"Authenticated user: {user.username}")
    return JsonResponse({'user': user.username, 'message': 'Hello, world!'})
