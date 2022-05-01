from factory import django, Faker
from django.contrib.auth.models import User
class UserFactory(django.DjangoModelFactory):

    class Meta:
        model = User
        django_get_or_create =('username','first_name','last_name','email','username',)
    username=Faker('user_name')
    first_name = Faker('first_name')
    last_name = Faker('last_name')
    email = Faker('email')
    password = Faker('password')

    def __str__(self):
        return 'username: {},first_name: {},last_name: {}, email: {},password: {}.'.format(self.username,self.first_name,self.last_name,self.email,self.password)
        