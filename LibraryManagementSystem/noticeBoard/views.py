from django.shortcuts import render

from .models import Notice

# Create your views here.


def notice(request):
    data = Notice.objects.all()
    notice = {'details': data}

    return render(request, 'noticeBoard/notice.html', notice)
