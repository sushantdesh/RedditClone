from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from . import views

# router = routers.DefaultRouter()
# router.register(r'posts', views.getPosts, basename='Posts')
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('', views.getPosts, name="api_overview"),
    # path('postcreate/', views.createPost, name="post_Create"),
    # path('getComment/', views.getComments, name="post_Create"),
    # path('register/', views.create_auth, name="post_Create"),
path('u/', views.UserList.as_view()),
path('users/<int:pk>/', views.UserDetail.as_view()),
path('posts/', views.PostList.as_view()),
path('posts/<int:pk>/', views.PostDetail.as_view()),
path('comments/', views.CommentList.as_view()),
path('comments/<int:pk>/', views.CommentDetail.as_view()),
    # path('postComment/', views.postComment, name="post_Comment"),
    # path('getDetailedPost/<str:pk>/', views.getDetailedPost, name="post_Detailed_post"),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
