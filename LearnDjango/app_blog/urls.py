from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import HomePageView, ArticleDetail, ArticleList, ArticleCategoryList

urlpatterns = [
	path(r'', HomePageView.as_view(), name='home'),
	path('articles', ArticleList.as_view(), name='articles-list'),
	path(r'articles/category/<slug>',ArticleCategoryList.as_view(),name='articles-category-list'),
	path('articles/<year>/<month>/<day>/<slug>', ArticleDetail.as_view(), name='news-detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)