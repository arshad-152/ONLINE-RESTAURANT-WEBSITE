from django.urls import path
from . import views

urlpatterns = [

    path('',views.Home,name="Home"),
    path('menu',views.Menu,name="Menu"),
    path('book_table',views.Book_Table,name="Book_Table"),
    path('about',views.About,name="About"),
    path('feedback',views.Feedbackk,name="Feedbackk"),
    path('signup',views.SignUp,name="SignUp"),
    path('login',views.Login,name="Login"),
    path('logout',views.Logout,name="Logout"),
    path('viewdetails',views.Viewdetails,name="Viewdetails"),

]