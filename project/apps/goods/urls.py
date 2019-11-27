from django.conf.urls import url

from goods import views
urlpatterns = [
	url(r'^index$',views.IndexView.as_view(),name='index'),
	url(r'^category$',views.CategoryView.as_view(),name='category'),
	url(r'^search$',views.SearchView.as_view(),name='search'),
	url(r'^detail/(?P<goods_id>\d+)$',views.DetailView.as_view(),name='detail'),
]
