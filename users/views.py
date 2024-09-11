from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from users.models import CustomUser


# Create your views here.

class RegisterView(TemplateView):
    template_name = 'register.html'


from django.shortcuts import render
from django.views import View
from .models import CustomUser

class UserMakeRegistrationView(View):

    def post(self, request, *args, **kwargs):
        data = request.POST
        password1 = data['password1']
        password2 = data['password']

        if password1 == password2:
            first = data['first_name']
            last = data['last_name']
            email = data['email']
            user = CustomUser.objects.create_user(email=email, password=password1, first_name=first, last_name=last)

            return render(request, 'product-list.html')
        else:
            pass



class LoginView(TemplateView):
    template_name = 'login.html'


class UserMakeLoginView(View):



