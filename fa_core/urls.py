from django.conf.urls import include
from django.contrib import admin
from rest_framework import routers
from django.urls import path
from app_user.views import CustomAuthToken
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Yell API')
router = routers.DefaultRouter()
urlpatterns = [
    path('', schema_view),
    path('accounts/', include('rest_framework.urls')),
    path('yellyuyoi/', admin.site.urls),
    path('api-token-auth/', CustomAuthToken.as_view()),

    path('app_user/', include('app_user.urls')),
    path('app_story/', include('app_story.urls')),
]

# import django
# from django.conf.urls import url
# from django.contrib.auth import views
#
#     login = views.LoginView.as_view(template_name='rest_framework/login.html')
#     login_kwargs = {}
#     logout = views.LogoutView.as_view()
#
#
# app_name = 'rest_framework'
# urlpatterns = [
#     url(r'^login/$', login, login_kwargs, name='login'),
#     url(r'^logout/$', logout, name='logout'),
# ]
