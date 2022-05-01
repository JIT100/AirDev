from django.urls import path,include
from .api import TaskCreateApi,TaskApi,TaskUpdateApi,TaskDeleteApi

urlpatterns=[
      path('', TaskApi.as_view(),name='todo_list'),
      path('create', TaskCreateApi.as_view(),name='todo_create'),
      path('<int:pk>', TaskUpdateApi.as_view()),
      path('<int:pk>/delete', TaskDeleteApi.as_view())
]