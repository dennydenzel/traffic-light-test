from django.shortcuts import render

from posts.services import delete_data, get_posts, load_data


def posts_view(request):
    if request.method == 'POST':
        if request.POST['action'] == 'delete':
            delete_data()
        if request.POST['action'] == 'load':
            load_data()
    posts = get_posts()
    context = {'posts': posts}
    return render(request, 'posts/index.html', context)
