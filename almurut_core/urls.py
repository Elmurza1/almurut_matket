

from django.contrib import admin
from django.conf.urls.static import static
from django.conf.urls.static import settings
from django.urls import path
from market.views import HomeView, ProductView, ShoppingView, ProductDetailView, FaqView, FavoriteView, PageFotFound, \
    SendProductFeedbackView, AddProductToFavoriteView, RemoveProductFromFavoriteView
from users.views import RegisterView, UserMakeRegistrationView, LoginView


urlpatterns = [
    path('home/',HomeView.as_view(), name='home-list'),
    path('admin/', admin.site.urls),
    path('product-list/', ProductView.as_view(), name='product-list'),
    path('shopping-cart/', ShoppingView.as_view(), name='sopping-list'),
    path('register/', RegisterView.as_view(), name='register-list'),
    path('login/', LoginView.as_view(), name='login-list'),
    path('faq/', FaqView.as_view(), name='fag-list'),
    path('product-detail/<int:pk>/', ProductDetailView.as_view(), name='product-detail-url'),
    path('favorites/', FavoriteView.as_view(), name= 'favorite-list'),
    path('add-product-to-favorite/<int:pk>/', AddProductToFavoriteView.as_view(), name='add-product-to-favorite-url'),
    path('remove/product-from-favorite/<int:pk>/', RemoveProductFromFavoriteView.as_view(), name='remove-from-favorite'),
    path('404/', PageFotFound.as_view(), name='404-list'),
    path('user_register_page/', UserMakeRegistrationView.as_view(), name='make-registration-user'),
    path('products/<int:pk>/send-feedback/', SendProductFeedbackView.as_view(), name='send-feedback-url'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
