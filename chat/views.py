from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Thread

# Create your views here.
@login_required
def messages_page(request):
    threads = Thread.objects.by_user(user=request.user).prefetch_related('chatmessage_thread').order_by('timestamp')
    context = {
        'Threads': threads
    }
    return render(request, 'messages.html', context)

# def messages_page(request):
#     return render(request, 'messages.html')