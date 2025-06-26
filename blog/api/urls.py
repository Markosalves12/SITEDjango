from blog.api.views import api_datail_blog_view, api_delete_blog_view, api_create_blog_view, api_update_blog_view, ApiBlogListView
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('<str:slug>/', api_datail_blog_view, name="detailapi"),
    path('<str:slug>/update/', api_update_blog_view, name="updateapi"),
    path('<str:slug>/delete/', api_delete_blog_view, name="deleteapi"),
    path('create', api_create_blog_view, name="createapi"),
    path('list', ApiBlogListView.as_view(), name="list"),
 ]