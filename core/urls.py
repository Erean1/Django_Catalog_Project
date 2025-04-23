from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path('',views.Home.as_view(),name="home"),
    path('create_post/',views.CreatePostView.as_view(),name="create_post"),
    path('<slug:slug>/category_detail/',views.CategoryDetailPageView.as_view(),name="category_detail"),
    path('<slug:slug>/post_detail/',views.PostDetailView.as_view(),name="post_detail"),
    path('<slug:slug>/update/',views.PostEditView.as_view(),name="post_edit"),
    path('<slug:slug>/delete/',views.PostDeleteView.as_view(),name="post_delete"),
    path('<slug:slug>/comment/',views.AddCommentView.as_view(),name="add_comment"),

] 