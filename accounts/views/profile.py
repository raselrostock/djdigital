from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.forms import UserUpdateForm, ProfileUpdateForm

from courses.models import Course
from instructors.models import Instructor


@login_required
def ProfileView(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(
                request, 'Your account has been updated')
            return redirect('memberships:dashboard')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    courses = Course.objects.order_by('start_date').all()[:3]
    instructors = Instructor.objects.order_by('dofb').all()[:3]
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'courses': courses,
        'instructors': instructors
    }
    return render(request, 'accounts/profile.html', context)
