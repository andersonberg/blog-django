from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<title>\w+)\.html$',  "blog.views.show_post"),
)
