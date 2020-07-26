from django.urls import path
from blog.views import blog, add_post

urlpatterns = [
       path('blog/', blog, name='blog'),
       path('add_post', add_post, name='add_post')
]