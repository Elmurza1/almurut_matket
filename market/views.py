import datetime

from django.views.generic import TemplateView, View
from .models import Product

# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
          context = {
        'publication_list': Product.objects.all()
    }

          return context




class ProductView(TemplateView):
    template_name = 'product-list.html'

    def get_context_data(self, **kwargs):
        context = {
        'publication_list': Product.objects.all(),
        'new': datetime.datetime.now().date()
    }
        return context



class ShoppingView(TemplateView):
    template_name = 'shopping-cart.html'

class FaqView(TemplateView):
    template_name = 'faq.html'





class ProductDetailView(TemplateView):
    template_name = 'product-detail.html'


class RegisterView(TemplateView):
    template_name = 'register.html'

class FavoriteView(TemplateView):
    template_name = 'favorites.html'


class PageFotFound(TemplateView):
    template_name = '404.html'
