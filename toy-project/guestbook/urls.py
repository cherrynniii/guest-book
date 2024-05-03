from django.urls import path
from guestbook.views import *

urlpatterns = [
    # path('', post_list, name="post_list"),
    # path('<int:id>/', post_detail, name="post_detail")
    path('', PostList.as_view()),
    path('<int:id>', PostDetail.as_view())
]