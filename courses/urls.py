from django.urls import path, include
from .models import Course
from courses import views
from quizes.views import QuizView, QuizSubmitView


app_name = 'courses'

urlpatterns = [
    path('', views.CourseListView, name='courselist'),
    path('<course_slug>/', views.CourseDetailView.as_view(), name='course-detail'),
    path('<course_slug>/like/',
         views.CourseLikeToggleVIew, name='course-like'),
    path('<course_slug>/add-review/',
         views.AddReviewView, name='add-review'),
    path('<str:course_slug>/<str:lesson_slug>/',
         views.LessonDetailView, name='lesson-detail'),
    path('<str:course_slug>/<str:lesson_slug>/add-comment/',
         views.AddCommentView, name='add-comment'),
    path('<str:course_slug>/<str:lesson_slug>/quiz/',
         QuizView, name='quiz'),
    path('<str:course_slug>/<str:lesson_slug>/quizresult/',
         QuizSubmitView, name='quizresult')
]
