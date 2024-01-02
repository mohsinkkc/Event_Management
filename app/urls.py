from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('about',views.about,name='about'),
   path('contact',views.contact,name='contact'),
   path('ticket',views.ticket,name='ticket'),
   path('rent_venue',views.rent_venue,name='rent_venue'),
   path('login',views.login,name='login'),
   path('signup',views.signup,name='signup'),
   path('logout',views.logout,name='logout'),
   path('forget_pswd',views.forget_pswd,name='forget_pswd'),
   path('confirm_otp',views.confirm_otp,name='confirm_otp'),
   path('change_pswd',views.change_pswd,name='change_pswd'),


   path('cart',views.cart,name='cart'),
   path('add_cart/<int:pk>',views.add_cart,name='add_cart'),
   path('delete_cart/<int:pk>',views.delete_cart,name='delete_cart'),
   path('callback',views.callback,name='callback'),

   path('admin_index',views.admin_index,name='admin_index'),
   path('add_service',views.add_service,name='add_service'),
   path('add_event',views.add_event,name='add_event'),
   path('view_service',views.view_service,name='view_service'),
   path('delete_service/<int:pk>',views.delete_service,name='delete_service'),
   path('update_service/<int:pk>',views.update_service,name='update_service'),
    path('view_event',views.view_event,name='view_event'),
    path('delete_event/<int:pk>',views.delete_event,name='delete_event'),
    path('update_event/<int:pk>',views.update_event,name='update_event'),
    path('create-checkout-session/',views.create_checkout_session,name='payment'),
   path('success.html/',views.success,name='success'),
   path('cancel.html/',views.cancel,name='cancel'),



    path('ajax/validate',views.validate,name='validate'),
    
]
