
from os import access
from django.urls import reverse
from rest_framework.test import APITestCase
from todo.tests.tests_auth import Auth
from django.contrib.auth.models import User
# Create your tests here.

ACCESS_TOKEN=[]
def auth(self):
    auth_users=Auth.test_signin_after_registering(self)
    for user in auth_users:
        ACCESS_TOKEN.append(user)
    return ACCESS_TOKEN

class setup(APITestCase):
    def creating_dummy_todo_data(self):
        auth_users=auth(self)
        for user in auth_users:
            access_token=user
            user_db=User.objects.all().values_list('id', flat=True)
            response=self.client.post(reverse('todo_create'),{'user': user_db[0], 'tittle': 'Test 1','description': 'Test 2 Description','status':0,'due_Date':'2022-05-01'},HTTP_AUTHORIZATION=f'Bearer {access_token}')

class TodoTest(APITestCase):

    def test_get_todo_list_without_authentication_token(self):
        print('Testing of fetching todo list without Registering the User, Result will be failed.')
        response=self.client.post(reverse('token_obtain_pair'),{'username': 'TestUsername', 'password': 'Test@12312'})
        print(response.data)
        self.assertEqual(response.status_code, 200)

    def test_get_todo_list_after_authentication_token(self):
        setup.creating_dummy_todo_data(self)
        auth_users=ACCESS_TOKEN
        for user in auth_users:
            access_token=user
            response=self.client.get(reverse('todo_list'),HTTP_AUTHORIZATION=f'Bearer {access_token}')
            self.assertEqual(response.status_code, 200)
        print('sucess')