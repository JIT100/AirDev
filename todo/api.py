import imp
from rest_framework import generics
from .serializers import TaskSerializers
from .models import Task
from rest_framework.permissions import IsAuthenticated,AllowAny
#from rest_framework_api_key.permissions import HasAPIKey
class TaskCreateApi(generics.CreateAPIView):
    '''We can create new Task using this api. '''
    permission_classes = [IsAuthenticated,]
    queryset = Task.objects.all()
    serializer_class = TaskSerializers

class TaskApi(generics.ListAPIView):
    ''' We can fetch the details of all the Tasks we have in the DB using this api.'''
    permission_classes = [IsAuthenticated,]
    queryset = Task.objects.all()
    serializer_class = TaskSerializers
    filterset_fields = ('status','due_Date','user','tittle') 

class TaskUpdateApi(generics.RetrieveUpdateAPIView):
    ''' We can update/paritally update/check  indiviual Task we have in the DB using this api.'''
    permission_classes = [IsAuthenticated,]
    queryset = Task.objects.all()
    serializer_class = TaskSerializers

class TaskDeleteApi(generics.DestroyAPIView):
    ''' We can delete indiviual Task we have in the DB using this api.'''
    permission_classes = [IsAuthenticated,]
    queryset = Task.objects.all()
    serializer_class = TaskSerializers
