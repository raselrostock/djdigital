from django.urls import path
from pages.views import faqView

app_name = 'pages'

urlpatterns = [
    path('', faqView, name='faqs'),
]
