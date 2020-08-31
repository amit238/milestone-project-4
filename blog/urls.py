from django.urls import path
from blog.views import blog, add_post, edit_post, delete_post

urlpatterns = [
       path('blog/', blog, name='blog'),
       path('add_post', add_post, name='add_post'),
       path('edit/<post_id>', edit_post, name='edit_post'),
       path('delete/<post_id>', delete_post, name='delete_post')
]
