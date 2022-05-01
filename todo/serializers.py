
from .models import Task
from rest_framework import  serializers
class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields='__all__'
        extra_kwargs = {
            'tittle':{'required' : True},
            'user' : {'required' : True}
        }