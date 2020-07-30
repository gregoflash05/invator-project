from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.download_to_pdf, name="download_to_pdf",)
    path('/preview/<slug:id>', views.preview_template, name="preview_template")
]