from .utility_functionality import *
from django.views.generic import View
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from decouple import config
import stripe

from memberships.models import Membership


class PaymentView(View):
    def get(self, *args, **kwargs):
        context = {
            'selected_membership': get_selected_membership(self.request)
        }
        return render(self.request, 'memberships/membership_payment.html', context)

    def post(self, *args, **kwargs):
        token = self.request.POST.get('stripeToken')
        user_membership = get_user_membership(self.request)
        try:
            selected_membership = get_selected_membership(self.request)
        except:
            return redirect('memberships:select')
        amount = int(selected_membership.price)
        try:
            customer = stripe.Customer.retrieve(
                user_membership.stripe_customer_id)
            customer.source = token
            customer.save()

            '''
            Now we can create the subscription using only the customer as we don't need to pass their
            credit card source anymore
            '''
            subscription = stripe.Subscription.create(
                customer=user_membership.stripe_customer_id,
                items=[
                    {"plan": selected_membership.stripe_plan_id},
                ]
            )
            return redirect(reverse('memberships:update-transactions',
                                    kwargs={
                                        'subscription_id': subscription.id
                                    }))

        except stripe.error.CardError as e:
            body = e.json_body
            err = body.get('error', {})
            messages.warning(self.request, f"{err.get('message')}")
            return redirect('memberships:select')

        except stripe.error.RateLimitError as e:
            # Too many requests made to the API too quickly
            messages.warning(self.request, "Rate limit error")
            return redirect('memberships:select')

        except stripe.error.InvalidRequestError as e:
            # Invalid parameters were supplied to Stripe's API
            messages.warning(self.request, "Invalid parameters")
            return redirect('memberships:select')

        except stripe.error.AuthenticationError as e:
            # Authentication with Stripe's API failed
            # (maybe you changed API keys recently)
            messages.warning(self.request, "Not authenticated")
            return redirect('memberships:select')

        except stripe.error.APIConnectionError as e:
            # Network communication with Stripe failed
            messages.warning(self.request, "Network error")
            return redirect('memberships:select')

        except stripe.error.StripeError as e:
            # Display a very generic error to the user, and maybe send
            # yourself an email
            messages.warning(
                self.request, "Something went wrong. You were not charged. Please try again.")
            return redirect('memberships:select')

        except Exception as e:
            # send an email to ourselves
            messages.warning(
                self.request, "A serious error occurred. We have been notifed.")
            return redirect('memberships:select')
