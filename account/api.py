from rest_framework import generics,status
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from .models import BlackListedToken
from .serializers import RegisterSerializer, UserSerializer
APP_NAME = 'account'
class RegisterApi(generics.GenericAPIView):
    ''' User can can register/create their account with this API. The account will be normal user without any admin acesss. They can use the username & password to sign in.'''
    serializer_class = RegisterSerializer
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            'status': 'success',
            'code': status.HTTP_200_OK,
            "user": UserSerializer(user,context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Sign in to get your token",
        })
class SignoutApi(APIView):
    ''' User can sign out after they login sucessfully. Login format is "Bearer {Api access key}"'''
    permission_classes = [IsAuthenticated,]
    def get(self, request):
        bearer_token  = (request.headers['Authorization'])
        if 'Bearer' in bearer_token:
            bearer_token = bearer_token.split('Bearer')[1].strip()
        BlackListedToken.objects.create(user =request.user,token =  bearer_token)
        return Response({
            'status': 'success',
            'code': status.HTTP_200_OK,
            "message":'user logged out successfully!'
            })

@api_view(['GET'])
@permission_classes((AllowAny,))
def index(request):
    response = {
        'message':'Welcome to AirDev API'
    }
    return Response(response)

def format_api_response(response_dict):
    response = {
    "status": response_dict['status'],
    "code": response_dict['code'],
    "message": response_dict['message'],
    response_dict['app_label']: response_dict['data']
    }
    return response