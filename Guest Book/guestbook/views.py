from django.shortcuts import render, redirect

# Create your views here.

from .models import Comment #used in index
from .forms import CommentForm #used in sign

def index(request):
    comments = Comment.objects.order_by('-date_added')
    context = {'comments':comments}
    return render(request, 'index.html',context)

def sign(request):
    if request.method == 'POST':
       form = CommentForm(request.POST)
       if form.is_valid():
           new_comment = Comment(name=request.POST['name'], comment=request.POST['comment'])
           new_comment.save()
           return redirect('index')
    else:
        form = CommentForm()
    context = {'form':form}
    return render(request,'sign.html',context)