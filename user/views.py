from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

from user.serializer import MyTokenObtainPairSerializer, ProfileSerializer, RegisterSerializer, UserSerializer
from user.models import Profile, User


from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({'message': 'User registered successfully', 'refresh_token': str(refresh), 'access_token': str(refresh.access_token)}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def obtain_token(request):
    serializer = MyTokenObtainPairSerializer(data=request.data)
    if serializer.is_valid():
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def profile(request):
    user = request.user
    if request.method == 'GET':
        serializer = ProfileSerializer(user.profile)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        data=request.data
       # if 'image' in request.data:
            #user.image = request.FILES.get('image')
        #data.image=request.FILES.get('image')
        #data['image'] = request.FILES['image']
        serializer = ProfileSerializer(user.profile, data= data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(csrf_exempt, name='dispatch')
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_password(request):
    if request.method == 'POST':
        # Retrieve JSON data from the request body
        data = json.loads(request.body)
        # Pass the JSON data to the PasswordChangeForm
        form = PasswordChangeForm(user=request.user, data=data)
        
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important for maintaining user's session
            return JsonResponse({'success': 'Password has been changed successfully.'})
        else:
            print(form.errors)
            return JsonResponse({'error': form.errors}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)