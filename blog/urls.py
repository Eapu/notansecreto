from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog'

urlpatterns = [
  	url(r'^$', views.post_list, name='post_list'),
	url(r'^new/$', views.post_new, name='post_new'),

	url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',views.post_detail, name='post_detail'),

	#url(r'^$', views.PostListView.as_view(), name='post_list'),
	url(r'^(?P<post_id>\d+)/share/$', views.post_share,  name='post_share'),
	url(r'^tag/(?P<tag_slug>[-\w]+)/$', views.post_list, name='post_list_by_tag'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
