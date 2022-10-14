# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from authentication import serializers, models


class UserAuthenticationView(APIView):
    def get(self, request, format=None):
        return Response({'msg': 'Authentication HomePage'}, status=status.HTTP_200_OK)


class UserRegisterView(generics.CreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserRegisterSerializer

    def perform_create(self, serializer):
        serializer.save()


class UserListView(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = models.User.objects.all()
    serializer_class = serializers.UserListSerializer


class UserListDetail(generics.RetrieveAPIView):
    permission_classes = [IsAdminUser]
    queryset = models.User.objects.all()
    serializer_class = serializers.UserListSerializer


# DIFFERENT METHOD (LENGTHY)
# class UserRegisterView(APIView):
#     renderer_classes = [renderers.UserRenderer]

#     def post(self, request, format=None):
#         serializer = serializers.UserRegisterSerializer(data=request.data)

#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response({'data': serializer.data, 'msg': 'Registration successful'}, status=status.HTTP_201_CREATED)


# class UserListView(APIView):
#     renderer_classes = [renderers.UserRenderer]
#     permission_classes = [IsAdminUser]

#     def get(self, request, format=None):
#         user_list = models.User.objects.all()
#         serializer = serializers.UserListSerializer(
#             instance=user_list, many=True)

#         return Response({'data': serializer.data, 'msg': 'Successful'}, status=status.HTTP_201_CREATED)


# class UserLoginView(APIView):
#     def post(self, request, format=None):
#         serializer = serializers.UserLoginSerializer(data=request.data)

#         serializer.is_valid(raise_exception=True)
#         email = serializer.data.get('email')
#         password = serializer.data.get('password')

#         user = authenticate(email=email, password=password)

#         if user is not None:
#             token = utils.get_tokens_for_user(user)
#             return Response({'access_token': token, 'msg': 'Login successful'}, status=status.HTTP_200_OK)
#         else:
#             return Response(data={'errors': {'non_field_errors': 'Invalid Credentials'}}, status=status.HTTP_400_BAD_REQUEST)
