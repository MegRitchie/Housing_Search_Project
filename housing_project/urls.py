"""housing_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from housing_app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include('social_django.urls', namespace='social')),
    #path('', include('social_django.urls', namespace='social')),
    url(r'^logged-out/', views.logout, name='logout'),
    url(r'^$', views.home, name='home'),
    url(r'^apartments/$', views.apartments, name='apartments'),
    url(r'^apartments/(\d+)/', views.apartment_detail, name='apartment_detail'),
    url(r'^login/', views.login, name='login'),
    url(r'^favorites/', views.favorites, name='favorites'),
    url(r'^login-success/', views.loginsuccess, name='login-success'),
    url(r'^save_favorite/(\d+)/', views.save_favorite, name='save_favorite'),
    url(r'^delete_favorite/(\d+)/', views.delete_favorite, name='delete_favorite'),
    url(r'profile/(?P<username>[a-zA-Z0-9!#$%^&*+-._]+)$', views.get_user_profile, name='profile'),
    url(r'profile/(?P<username>[a-zA-Z0-9!#$%^&*+-._]+)/reviews/', views.get_user_reviews, name='reviews'),
    url(r'^compare/', views.compare, name='compare'),
    url(r'^compare_maps/', views.compare_maps, name='compare_maps'),
    url(r'^save_compare0/(\d+)/', views.save_compare0, name='save_compare0'),
    url(r'^delete_compare0/', views.delete_compare0, name='delete_compare0'),
    url(r'^save_compare1/(\d+)/', views.save_compare1, name='save_compare1'),
    url(r'^delete_compare1/', views.delete_compare1, name='delete_compare1'),
    url(r'^fav_save_compare0/(\d+)/', views.fav_save_compare0, name='fav_save_compare0'),
    url(r'^fav_save_compare1/(\d+)/', views.fav_save_compare1, name='fav_save_compare1'),
    url(r'^ratings/', include('star_ratings.urls', namespace='ratings')),
    url(r'^filter/', views.apartments, name='filter'),
    url(r'^compare0_search', views.search_compare0, name='compare0_search'),
    url(r'^save_compare0_search/(\d+)/', views.save_compare0_search, name='save_compare0_search'),
    url(r'^compare1_search', views.search_compare1, name='compare1_search'),
    url(r'^save_compare1_search/(\d+)/', views.save_compare1_search, name='save_compare1_search'),
    url(r'^delete_review/(\d+)/', views.delete_review, name='delete_review'),
    # url(r'^edit_profile/', views.save_profile, name='save_profile'),
]

urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
