from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from blog.views import BlogListView, BlogCreateView,BlogDetailView,BlogUpdateView,BlogDeleteView
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('',BlogListView.as_view(), name="list"),
    path('create/', BlogCreateView.as_view(), name="create"),
    path('<slug>/', BlogDetailView.as_view(), name="detail"),
    path('<slug>/update/', BlogUpdateView.as_view(), name="update"),
    path('<slug>/delete/', BlogDeleteView.as_view(), name="delete"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
