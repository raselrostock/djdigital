from .utility_functionality import *
from django.contrib import messages
from django.shortcuts import reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView

from memberships.models import Membership


class MembershipListView(ListView):
    model = Membership
    context_object_name = 'memberships'
    template_name = 'memberships/membership_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_membership_type = get_user_membership(self.request).membership
        context["current_membership"] = str(current_membership_type)
        return context

    def post(self, request, *args, **kwargs):
        user_membership = get_user_membership(self.request)
        user_subscription = get_user_subscription(self.request)
        selected_membership_type = request.POST.get('membership_type')
        selected_membership = Membership.objects.get(
            membership_type=selected_membership_type)
        if user_membership.membership == selected_membership:
            if user_subscription is not None:
                messages.warning(
                    request, 'You already subscribed this membership')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        request.session['selected_membership_type'] = selected_membership.membership_type
        return HttpResponseRedirect(reverse('memberships:payment'))
