from django.shortcuts import render
from django.core.paginator import Paginator

from courses.models import Course


def CourseListView(request):
    courses_qs = Course.objects.order_by('start_date').all()
    per_page = 6
    paginator = Paginator(courses_qs, per_page)
    page = request.GET.get('page')
    courses = paginator.get_page(page)
    context = {
        'courses': courses,
        'title': 'Courses'
    }
    return render(request, 'courses/course_list.html', context)
