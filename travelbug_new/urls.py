from django.urls import path
from .import views as v

urlpatterns = [
      path('', v.home,name="home"),
       path('signup/', v.signup,name="signup"),
       path('about/', v.about,name="about"),
       path('contact/', v.contact,name="contact"),
       path('vendorsignup/',v.vendorsignup,name="vendorsignup"),
       path('userlogin/',v.userlogin,name="userlogin"),
       path('userhome/',v.userhome,name="userhome"),
       path('userlogout/',v.uselogout,name='userlogout'),
       path('vendorhome/',v.vendorhome,name='vendorhome'),
       path('vendorlogin/',v.vendorlogin,name='vendorlogin'),
       path('vendorlogout/',v.vendorlogout,name='vendorlogout'),
       path('vcreate/',v.vcreate,name='vcreate'),
       path('item/<int:pk>/delete/',v.vendordelete,name='vendordelete'),
       path('item/<int:pk>/update/',v.vendorupdate,name='vendorupdate'),
       path('booking/<int:package_id>/', v.booking, name='booking'),
       path('bookingdisplay/',v.bookingdisplay,name='bookingdisplay'),
       path('vendorbookings/',v.vendorbookings, name='vendorbookings'),
       path('profile/',v.profile, name='profile'),
       path('payment/',v.payment, name='payment'),


       
]