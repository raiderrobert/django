from django.conf.urls import url

from .views import empty_view

urlpatterns = [
    # no args
    url(r'^conflict/$', empty_view, name="name-conflict"),

    # 1 arg
    url(r'^conflict-first/(?P<first>\w+)/$', empty_view, name="name-conflict"),
    url(r'^conflict-cannot-go-here/(?P<middle>\w+)/$', empty_view, name="name-conflict"),
    url(r'^conflict-middle/(?P<middle>\w+)/$', empty_view, name="name-conflict"),
    url(r'^conflict-last/(?P<last>\w+)/$', empty_view, name="name-conflict"),

    # 2 args
    url(r'^conflict/(?P<extra>\w+)/(?P<another>\w+)/$', empty_view, name="name-conflict"),

]
