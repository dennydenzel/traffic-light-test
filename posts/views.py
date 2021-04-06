from django.shortcuts import render


def posts_view(request):
    return render(request, 'posts/index.html')
