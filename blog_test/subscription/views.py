from django.shortcuts import render, redirect
from .forms import SubscriptionForm


def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
    else:
        form = SubscriptionForm()
    return render(request, 'subscription/subscribe.html', {'form': form})


def thank_you(request):
    return render(request, 'subscription/thank_you.html')