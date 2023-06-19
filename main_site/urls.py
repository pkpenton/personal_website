from django.conf import settings
from django.urls import include, re_path
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    # re_path(r'^blog/', include('blog.urls')),
    re_path(r'', include('static_pages.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
