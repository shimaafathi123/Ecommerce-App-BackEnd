from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
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
 
 
from django.contrib.auth import get_user_model


from django.http import JsonResponse
from django.db.models import Q
from product.models import Product


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
       
        data = json.loads(request.body)
     
        form = PasswordChangeForm(user=request.user, data=data)
        
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)   
            return JsonResponse({'success': 'Password has been changed successfully.'})
        else:
            print(form.errors)
            return JsonResponse({'error': form.errors}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)
    
#@login_required
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_current_user_info(request):
     
    user = request.user
    print(user)
    user_info = {
        'username': user.username,
        'fullname':user.full_name
      #  'email': user.email,
         
    }
    return JsonResponse(user_info)
    
    #admin-----------------------------------------------------------------------
User = get_user_model()

@api_view(['GET'])
@permission_classes([IsAdminUser])
def list_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_user(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
        user.delete()
        return Response({'message': 'User deleted successfully'})
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=404)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_user(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=404)
    ##search-----------------------------------------------------------
def search_products(request):
    query = request.GET.get('query', '')
    if query:
        results = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        serialized_results = [{'id': product.id, 'name': product.name} for product in results]
        return JsonResponse({'results': serialized_results})
    else:
        return JsonResponse({'results': []})
