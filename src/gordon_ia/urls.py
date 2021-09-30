from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls.conf import include
from tests.views import HomeView,PreguntasIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomeView.as_view(),name= 'home'),
    path('<int:pk>/',PreguntasIView.as_view(),name= 'preguntas_i')
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)