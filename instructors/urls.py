from django.urls import path
from instructors.models import Instructor
from instructors import views

app_name = 'instructors'
urlpatterns = [
    path('', views.InstructorListView.as_view(), name='instructor-list'),
    path('<instructor_name>/', views.InstructorDetailView.as_view(),
         name='instructor-detail'),
    path('<instructor_name>/add-rating/',
         views.AddRatingView, name='add-rating'),
]
