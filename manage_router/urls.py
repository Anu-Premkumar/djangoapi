from django.conf.urls import url
from manage_router import views

app_name = 'manage_router'

urlpatterns = [
    url(r'^$',views.routerListView.as_view(),name='list'),
    url(r'^(?P<pk>\d+)/$',views.routerDetailView.as_view(),name='detail'),
    url(r'^create/$',views.routerCreateView.as_view(),name='create'),
    url(r'^update/(?P<pk>\d+)/$',views.routerUpdateView.as_view(),name='update'),
    url(r'^delete/(?P<pk>\d+)/$',views.routerDeleteView.as_view(),name='delete')
]
