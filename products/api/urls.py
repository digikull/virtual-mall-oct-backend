from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView
)

urlpatterns = [
    path('', ProductListView.as_view()),
    path('create/', ProductCreateView.as_view()),
    path('<pk>', ProductDetailView.as_view()),
    path('<pk>/update/', ProductUpdateView.as_view()),
    path('<pk>/delete/', ProductDeleteView.as_view())
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
