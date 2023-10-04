from django.urls import path
from . import views


urlpatterns = [

    path("",views.StartingPage.as_view(),name="starting-page"),
  
    path("posts",views.AllPostsView.as_view(),name="posts-page"),

    path("posts/<slug:slug>",views.SinglePostView.as_view(),name="posts-details-page"),
    path("read-later",views.ReadLaterView.as_view(),name="read-later")
]


#urlpatterns = [
#   path("",views.starting_page,name="starting-page"),
 #   path("posts",views.posts,name="posts-page"),

# path("posts/<slug:slug>",views.post_detail,name="posts-details-page")
# ]