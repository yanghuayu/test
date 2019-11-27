from django.conf.urls import url

from users import views
urlpatterns = [
	#url(r'^register$',views.register,name='register'),
	#url(r'^register_handler$',views.register_handler,name='register_handler'),
 	url(r'^register$',views.RegisterView.as_view(),name='register'),
	url(r'^active/(?P<token>.*)$',views.ActiveView.as_view(),name='active'),
 	url(r'^login$',views.LoginView.as_view(),name='login'),
 	url(r'^me$',views.MeView.as_view(),name='me'),
 	url(r'^logout$',views.LogoutView.as_view(),name='logout'),
]
