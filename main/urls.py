from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from main_page import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about_me/', views.about_me),
    path('about_pets/', views.about_pets),
    path('showtime/', views.show_time),
    path('', include('main_page.urls')),
    path('', include('hashtags.urls')),
    path('basket/', include('basket.urls')),

]
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,
                      document_root=settings.STATIC_ROOT)

