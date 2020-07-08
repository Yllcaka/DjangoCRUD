from django.urls import path
from .views import ( 
		PostListView,
		PostDetailView, 
		PostCreateView,
		PostUpdateView,
		PostDeleteView,
		UserPostListView
)
from . import views
urlpatterns = [
	path("", PostListView.as_view(), name = "blogHome"),
	path("user/<str:username>", UserPostListView.as_view(), name = "userPost"),
	path("post/<int:pk>/", PostDetailView.as_view(), name = "postDetail"),
	path("post/new/", PostCreateView.as_view(), name="postCreate"),
	path("post/<int:pk>/update/", PostUpdateView.as_view(), name = "postUpdate"),
	path("post/<int:pk>/delete/", PostDeleteView.as_view(), name = "postDelete"),
	path("about/", views.about, name = "blogAbout"),
]