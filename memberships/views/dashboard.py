from .utility_functionality import *
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required

from notifications.models import Notification
from courses.models import Course
from instructors.models import Instructor


@login_required
def DashboardView(request):
    courses = Course.objects.order_by('start_date').all()[:3]
    instructors = Instructor.objects.order_by('dofb').all()[:3]
    notifications = Notification.objects.filter(
        user=request.user, viewed=False)
    user_membership = get_user_membership(request)
    user_subscription = get_user_subscription(request)
    context = {
        'user_membership': user_membership,
        'user_subscription': user_subscription,
        'notifications': notifications,
        'courses': courses,
        'instructors': instructors
    }

    return render(request, 'memberships/dashboard.html', context)
