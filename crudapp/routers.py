from rest_framework import routers
from article.viewsets import ArticleViewSet

router = routers.DefaultRouter()

# Api would be somewhat like /article linked to ArticleViewSet.
router.register(r'article', ArticleViewSet)
