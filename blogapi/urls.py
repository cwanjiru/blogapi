from django.urls import path
from .views import PostList, PostDetail
app_name = 'blogapi'

urlpatterns = [
    path('',PostList.as_view()),
    path('<int:pk>/', PostDetail.as_view())

]