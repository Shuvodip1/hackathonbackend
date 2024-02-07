from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/appointment/', views.AppointmentView.as_view()),
    path('api/contact/', views.ContactView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
