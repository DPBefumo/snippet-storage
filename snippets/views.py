from django.shortcuts import render, redirect, get_object_or_404
from .models import Snippet
from users.models import User
from django.contrib.auth.decorators import login_required
from .forms import SnippetForm


def home_page(request):
    if request.user.is_authenticated:
        return redirect(to='list_snippet')

    return render(request, "snippets/home_page.html")


@login_required
def list_snippet(request):
    snippets = request.user.snippets.all()
    return render(request, "snippets/list_snippet.html", {'snippets': snippets})


@login_required
def snippet_detail(request, snippet_pk):
    snippets = get_object_or_404(request.user.snippets, pk=snippet_pk)
    return render(request, "snippets/snippet_detail.html", {'snippets': snippets})


@login_required
def add_snippet(request):
    if request.method == "POST":
        form = SnippetForm(data=request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.user = request.user
            snippet.save()
            return redirect(to='snippet_detail', snippet_pk=snippet.pk)
    else:
        form = SnippetForm()
    
    return render(request, 'snippets/add_snippet.html', {'form': form})


@login_required
def edit_snippet(request, snippet_pk):
    snippets = get_object_or_404(request.user.snippets, pk=snippet_pk)
    
    if request.method == "POST":
        form = SnippetForm(instance=snippets, data=request.POST)
        if form.is_valid():
            snippets = form.save()
            return redirect(to='snippet_detail', snippet_pk=snippet.pk)

    else:
        form = SnippetForm()
    
    return render(request, "snippets/edit_snippet.html", {'snippets': snippets, 'form': form})


@login_required
def delete_snippet(request, snippet_pk):
    snippets = get_object_or_404(request.user.snippets, pk=snippet_pk)

    if request.method == 'POST':
        snippets.delete()
        return redirect(to='list_snippets')

    return render(request, "snippets/delete_snippet.html", {'snippets': snippets})