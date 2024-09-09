from django.views.generic import TemplateView, View

# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'


class ProductView(TemplateView):
    template_name = 'product-list.html'


class ShoppingView(TemplateView):
    template_name = 'shopping-cart.html'

class FaqView(TemplateView):
    template_name = 'faq.html'



class LoginView(TemplateView):
    template_name = 'login.html'

class ProductDetailView(TemplateView):
    template_name = 'product-detail.html'


class RegisterView(TemplateView):
    template_name = 'register.html'

class FavoriteView(TemplateView):
    template_name = 'favorites.html'


class PageFotFound(TemplateView):
    template_name = '404.html'
