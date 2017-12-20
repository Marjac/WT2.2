from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
from django.conf.urls.static import static

urlpatterns = [
    url(r'$', views.SnippetList.as_view()),
    url(r'(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

from webtech import settings
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)