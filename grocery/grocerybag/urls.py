from django.urls import path ,include
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('',views.view,name='home'),
    path('add/',views.add,name='add'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout')
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
