import datetime

from django.db.models import Q
from django.http import Http404
from django.shortcuts import redirect
from django.views.generic import TemplateView, View
from .models import Product, ProductUserRating, ProductGallery

# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        # Получаем поисковый запрос
        search_world = self.request.GET.get('query', '')
        publication_list = Product.objects.filter(
                Q(name__icontains=search_world) | Q(description__icontains=search_world)
            )


        context = {
            'publication_list': publication_list,
            'search_world': search_world,
        }
        return context





class ProductView(TemplateView):
    template_name = 'product-list.html'

    def get_context_data(self, **kwargs):
        search_world = self.request.GET.get('query', '')
        publication_list = Product.objects.filter(
            Q(name__icontains=search_world) | Q(description__icontains=search_world)
        )

        context = {
        'publication_list': publication_list,
        'new': datetime.datetime.now().date()
    }
        return context



class ShoppingView(TemplateView):
    template_name = 'shopping-cart.html'

class FaqView(TemplateView):
    template_name = 'faq.html'






class ProductDetailView(TemplateView):
    template_name = 'product-detail.html'

    def get_context_data(self, **kwargs):
        star = [1, 2, 3, 4, 5, 6, ]
        try:
            product = Product.objects.get(id=kwargs['pk'])
        except Product.DoesNotExist:
            raise Http404
        user = self.request.user

        try:
            my_product_rating = ProductUserRating.objects.get(product=product, user=user)
            rating = my_product_rating.rating
        except ProductUserRating.DoesNotExist:
            rating = 0

        product_rating_list = ProductUserRating.objects.filter(product=product)
        total_value = 0
        for product_rating in product_rating_list:
            total_value += product_rating.rating
        if len(product_rating_list)==0:
            average_rating = 0
        else:
            average_rating = total_value / len(product_rating_list)

        product_category = product.category
        category_other_product_list = (
            Product.objects
            .filter(category=product_category)
            .exclude(id=product.id)
        )

        context = {
            'product': product,
            'rating': rating,
            'average_rating': average_rating,
            'other_products': category_other_product_list,
            'range': star
        }
        return context

class SendProductFeedbackView(View):
    """Вью для сохранения отзыва пользователя для конкретного товара"""

    def post(self, request, *args, **kwargs):
        data = request.POST
        rating_value = data['rating_value']
        name_value = data['author']
        email_value = data['email']
        comment_value = data['comment']
        product = Product.objects.get(id=kwargs['pk'])
        user = request.user
        if user.is_authenticated:
            try:
                product_rating = ProductUserRating.objects.get(product=product, user=user)
            except ProductUserRating.DoesNotExist:
                ProductUserRating.objects.create(
                    rating=rating_value,
                    product=product,
                    user=user,
                    name=name_value,
                    email=email_value,
                    comment=comment_value
                )
                return redirect('product-detail-url', pk=product.id)

            product_rating.rating = rating_value
            product_rating.email = email_value
            product_rating.comment = comment_value
            product_rating.name = name_value
            return redirect('product-detail-url', pk=product.id)
        else:
            return redirect('/login/')



class RegisterView(TemplateView):
    template_name = 'register.html'


class FavoriteView(TemplateView):
    template_name = 'favorites.html'

    def get_context_data(self, **kwargs):
        user = self.request.user  # получаем пользователя который делает запрос
        context = {
            'my_favorite_products': user.favorite_product.all()
        }
        return context

class PageFotFound(TemplateView):
    template_name = '404.html'


class AddProductToFavoriteView(TemplateView):
    """Добавляет товар в избранное пользователя"""
    template_name = 'favorites.html'

    def get_context_data(self, **kwargs):
        user = self.request.user  # получаем пользователя который делает запрос

        product_id = kwargs['pk']
        product = Product.objects.get(id=product_id)
        user.favorite_product.add(product)
        user.save()

        context = {
            'my_favorite_products': user.favorite_product.all()
        }
        return context



class RemoveProductFromFavoriteView(TemplateView):
    """Удаляет товар из избранного пользователя"""
    template_name = 'favorites.html'

    def get_context_data(self, **kwargs):
        user = self.request.user

        product_id = kwargs['pk']
        product = Product.objects.get(id=product_id)
        user.favorite_product.remove(product)
        user.save()

        context = {
            'my_favorite_products': user.favorite_product.all()
        }
        return context
