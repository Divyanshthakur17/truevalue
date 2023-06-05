from django.contrib import admin
from django.urls import path, include
from accounts import views
from base import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views 

# Using Rest Framework 
from rest_framework.routers import DefaultRouter
from cars.views import NewCarsViewSets,UsedCarsViewSets
from base.views import AgentViewsets, BlogViewsets

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = DefaultRouter()
router.register('newcars',NewCarsViewSets, basename='newcars')
router.register('usedcars',UsedCarsViewSets, basename='usedcars')
router.register('agents',AgentViewsets, basename='agents')
router.register('blogs',BlogViewsets, basename='blogs')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    path('auth/login/', TokenObtainPairView.as_view(),name='create-token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('',views.index, name = 'home'),
    path('about/',views.about, name = 'about'),
    path('agents/',views.agents, name = 'agents'),
    path('user_profile/',views.user_profile_view, name = 'user_profile'),
    path('edit_profile/',views.edit_profile, name = 'editprofile'),
    path('blog/',views.blogs, name = 'blog'),
    path('blog/<int:pk>/',views.blogdetail, name = 'blogdetail'),
    path('contact/',views.contact, name = 'contact'),
    path('accounts/',include('accounts.urls')),
    path('cars/',include('cars.urls')),
    path('chat/',include('chat.urls')),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_confirm.html"), name='password_reset_confirm'),
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),      
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
