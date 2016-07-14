from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse , reverse_lazy

def note_list(request):
    print(timezone.now())
    posts = Post.objects.filter(end_time__gte=timezone.localtime(timezone.now())).order_by('end_time')
    return render(request, 'site/note_list.html', {'posts':posts})

def note_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'site/note_detail.html', {'post': post})

def note_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():

            post = form.save(commit=False)
            post.author = request.user
            print("ddddd")
            post.end_time = form.cleaned_data.get('end_time')
            post.save()
            return redirect('note.views.note_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'site/note_edit.html', {'form': form})

def note_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.end_time = form.cleaned_data.get('end_time')
            post.save()
            return redirect('note.views.note_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'site/note_edit.html', {'form': form})

def delete(self,pk):
    Obje = Post.objects.get(pk=pk)
    Obje.delete()
    return HttpResponseRedirect(reverse('note_list'))
