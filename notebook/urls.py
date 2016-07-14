from django.conf.urls import include, url
from django.contrib import admin

import note.views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', note.views.note_list, name='note_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', note.views.note_detail, name='note_detail'),
    url(r'^post/new/$', note.views.note_new, name='note_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', note.views.note_edit, name='note_edit'),
    url(r'^post/delete/(?P<pk>[0-9]+)/', note.views.delete, name='delete'),
]
