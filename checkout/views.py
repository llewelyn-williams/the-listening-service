from django.shortcuts import render, redirect

from .forms import OrderForm


def checkout(request):
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KhfwzBX1dPqJdtCcXX5ImiYoa9nRV8lJy8DJqm8kuSS4ZtTbaxzEruqX1MRbEl0tVE7WAl4bzjOrCObRHR9hOm000vjkaR9dv',
        'client_secret': 'test_client_secret',
    }

    return render(request, template, context)
