from django.urls import path
from .views import index,category,contact,single
urlpatterns = [
    path('',index,name='home'),
    path('category',category,name='category'),
    path('contact',contact,name='contact'),
    path('detail/<int:id>',single,name='detail')
]

