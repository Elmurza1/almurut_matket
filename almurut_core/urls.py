"""
URL configuration for almurut_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf.urls.static import static
from django.conf.urls.static import settings
from django.urls import path
from market.views import HomeView, ProductView, ShoppingView, ProductDetailView, FaqView,   FavoriteView, PageFotFound
from users.views import RegisterView, UserMakeRegistrationView, LoginView


urlpatterns = [
    path('home/',HomeView.as_view(), name='home-list'),
    path('admin/', admin.site.urls),
    path('product-list/', ProductView.as_view(), name='product-list'),
    path('shopping-cart/', ShoppingView.as_view(), name='sopping-list'),
    path('register/', RegisterView.as_view(), name='register-list'),
    path('login/', LoginView.as_view(), name='login-list'),
    path('faq/', FaqView.as_view(), name='fag-list'),
    path('product-detail/', ProductDetailView.as_view(), name='product-detail-list'),
    path('favorite',FavoriteView.as_view(), name='favorite-list'),
    path('404/', PageFotFound.as_view(), name='404-list'),
    path('user_register_page/', UserMakeRegistrationView.as_view(), name='make-registration-user')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
