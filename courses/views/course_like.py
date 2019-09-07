# from rest_framework.views import APIView
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from courses.models import Course
from django.contrib import messages


def CourseLikeToggleVIew(request, course_slug):
    course = get_object_or_404(Course, slug=request.POST.get('course_slug'))
    user = request.user
    is_liked = False
    if user.is_authenticated:
        if course.likes.filter(id=user.id).exists():
            course.likes.remove(user)
            is_liked = False
        else:
            course.likes.add(user)
            is_liked = True
    context = {
        'course': course,
        'is_liked': is_liked,
        'total_likes': course.get_total_like()
    }
    if request.is_ajax():
        html = render_to_string(
            'courses/course_like.html', context, request=request)
        return JsonResponse({'form': html})
