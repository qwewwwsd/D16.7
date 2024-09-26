from django.urls import path
from .views import PostList, PostUpdate, PostCreate, ResponseList, ResponseCreate, ResponseDelete, PostDelete, \
    response_status_update, IdPostList, PersonalPost, ConfirmUser, ProfileView

urlpatterns = [
    path('post/', PostList.as_view(), name='post'),
    path('post/personal/', PersonalPost.as_view(), name='personal_post'),
    path('post/<int:pk>', IdPostList.as_view(), name='post_id'),
    path('post/create/', PostCreate.as_view(), name='post_create'),
    path('post/edit/<int:pk>/', PostUpdate.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('response/', ResponseList.as_view(), name='response'),
    path('response/create/', ResponseCreate.as_view(), name='response_create'),
    path('response/<int:pk>/delete/', ResponseDelete.as_view(), name='response_delete'),
    path('response/<int:pk>/status', response_status_update, name='response_status'),

    path('confirm/', ConfirmUser.as_view(), name='confirm_user'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
