from django.urls import path
from quizes.views import QuizView

app_name = 'quizes'
urlpatterns = [
    path('', QuizView, name='quiz')
]
