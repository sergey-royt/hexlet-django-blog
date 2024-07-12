from django.urls import path

from hexlet_django_blog.article import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='articles'),
    path('<int:id>/edit/', views.ArticleFormEditView.as_view(), name='articles_update'),
    path('<int:id>/delete/', views.ArticleFormDeleteView.as_view(), name='articles_delete'),
    path('<int:id>/', views.ArticleView.as_view(), name="article"),
    path('<int:article_id>/comments/', views.ArticleCommentsView.as_view(), name='article_comments'),
    path('create/', views.ArticlesCreateView.as_view(), name='articles_create'),
]
