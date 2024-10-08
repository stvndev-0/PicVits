from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.cache import cache_page
from .models import Picture, Comment
from .forms import PictureForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
# @cache_page(60 * 15)
def home_view(request):
    picts = Picture.objects.all()
    return render(request, 'picvits/home.html', {'picts': picts})

def pict_view(request, pict_id):
    pict = get_object_or_404(Picture, id=pict_id)
    context = {
        'pict_url': pict.image.url,
        'pict_title': pict.title,
        'pict_author': pict.author.username,
        'pict_author_image_url': pict.author.profile.image.url,
        'pict_comments': pict.comment.all(),
    }
    return render(request, 'picvits/pict_view.html', context)

@login_required
def new_picture_view(request):
    if request.method == 'POST':
        picture_form = PictureForm(request.POST, request.FILES)
        if picture_form.is_valid():
            

            picture = picture_form.save(commit=False)
            picture.author = request.user
            picture.save()
            return redirect('home')
    else:
        picture_form = PictureForm()
    return render(request, 'picvits/crud/picture_form.html', {'picture_form': picture_form})

@login_required
def update_picture_view(request, pict_id):
    picture = get_object_or_404(Picture, id=pict_id, author=request.user)
    if request.method == 'POST':
        picture_form = PictureForm(request.POST or None, request.FILES or None, instance=picture)
        if picture_form.is_valid():
            picture_form.save()
            return redirect('profile')
    else:
        picture_form = PictureForm(instance=picture)
    return render(request, 'picvits/crud/picture_form.html', {'picture_form': picture_form})

@login_required
def delete_picture_view(request, pict_id):
    user = request.user.username
    pict = get_object_or_404(Picture, id=pict_id)
    if request.method == 'POST':
        pict.delete()
        return redirect(request, user)

@login_required
def add_comment_view(request, pict_id):
    pict = get_object_or_404(Picture, id=pict_id)
    if request.method == 'POST':
        comment_text = request.POST['comment-text']
        new_comment = Comment(text=comment_text, author=request.user, pict=pict)
        new_comment.save()
        return redirect('pict', pict_id)

@login_required
# solo el dueño del post y el author del comentario, pueden eliminar un comentario
def delete_comment_view(request, pict_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, pict_id=pict_id)
    if request.user == comment.pict.author or request.user == comment.author:
        comment.delete()
        return redirect('pict', pict_id)

def search_view(request):
    searched = request.POST['searched']
    picts = Picture.objects.only('title', 'created_at').filter(title__icontains=searched)
    return render(request, 'picvits/search.html', {'searched': searched, 'picts': picts})