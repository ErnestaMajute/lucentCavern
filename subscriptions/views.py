from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages

from .models import SubscriptionUser


def subscriptions_join(request):
    redirect_url = request.POST.get('redirect_url')

    if request.method == "POST":
        email = request.POST.get('subscription_email')
        if email:
            try:
                if_in_subscriptions_list = get_object_or_404(
                    SubscriptionUser, email=email)
                messages.error(
                    request, f'{email} already subscribing our newsletter.')
            except:
                new_subscription = SubscriptionUser(email=email)
                new_subscription.save()
                messages.success(
                    request,
                    f'Thanks! {email} added to our subscription list!')
        else:
            messages.error(request, 'Please insert a valid email address.')

    return redirect(redirect_url)
