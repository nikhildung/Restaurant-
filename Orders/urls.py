from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home, name='index'),
    path('Register', views.Register, name='Register'),
    path('Login', views.Login, name='Login'),
    path('Logout', views.Logout, name="Logout"),
    path('Indian', views.Indian, name='Indian'),
    path('Chinese', views.Chinese, name='Chinese'),
    path('Italian', views.Italian, name='Italian'),
    path('FastFood', views.FastFood, name='FastFood'),
    path('Tea', views.Tea, name='Tea'),
    path('Desserts', views.Dessert, name='Dessert'),
    path('Update', views.update_item, name="Update"),
    path('ShowCart', views.ShowCart, name="ShowCart"),
    path('Incre', views.Incre, name="Incre"),
    path('Checkout',views.Checkout,name="Checkout")

]
