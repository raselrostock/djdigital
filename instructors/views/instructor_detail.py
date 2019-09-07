from django.shortcuts import render
from django.views.generic import DetailView
from instructors.models import Instructor
from instructors.forms import RatingForm


class InstructorDetailView(DetailView):
    # model = Course
    # context_object_name = 'course'
    # template_name = 'courses/course_detail.html'

    def get(self, *args, **kwargs):
        username = kwargs['instructor_name']
        instructor = Instructor.objects.get(username=username)
        form = RatingForm()
        context = {
            'instructor': instructor,
            'form': form
        }
        return render(self.request, 'instructors/instructor_detail.html', context)
