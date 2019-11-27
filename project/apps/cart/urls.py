from django.conf.urls import url
from cart import views
urlpatterns = [
	url(r'^car$',views.CarView.as_view(),name='car')
]
