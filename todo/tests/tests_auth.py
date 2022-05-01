
from django.urls import reverse
from rest_framework.test import APITestCase
from todo.tests.fake_datasheet_tests import UserFactory
# Create your tests here.
class setup(APITestCase):
    def registering_user(self):
        users=UserFactory.build_batch(2)
        response=[]
        user_datas=[]
        for user in users:
            username=user.username
            firsname=user.first_name
            lastname=user.last_name
            email=user.email
            password=user.password
            user_data=[username,firsname,lastname,email,password]
            user_datas.append(user_data)
            response.append(self.client.post(reverse('register'),{'username': username, 'password': password,'first_name':firsname,'last_name':lastname,'email':email}))
        return [response,user_datas]

class Auth(setup):
    def test_signin_without_registering_the_user(self):
        print('Testing Sign in without Registering the User, Result will be failed.')
        response=self.client.post(reverse('token_obtain_pair'),{'username': 'JIT100', 'password': 'mars2008'})
        print(response.data)
        self.assertEqual(response.status_code, 200)

    def test_registering_user(self):
        responses=self.registering_user()
        responses=responses[0]
        for response in responses:
            self.assertEqual(response.status_code, 200)
        
    def test_signin_after_registering(self):
        responses=setup.registering_user(self)
        user_datas=responses[1]
        token_data=[]
        for data in user_datas:
            username=data[0]
            passwword=data[4]
            response=self.client.post(reverse('token_obtain_pair'),{'username': username, 'password': passwword})
            self.assertEqual(response.status_code, 200)
            token_data.append(response.data['access'])
        return token_data



