from django.shortcuts import render,get_object_or_404
from .models import Post,Comment
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .forms import commentForm
from django.views.generic import TemplateView
from .models import book

# Create your views here

# def displayTime(request):
#     now = datetime.datetime.now()
#     html="time  is{}".format(now)
#     return HttpResponse( html)

# def welcome(request):
#     return HttpResponse("welcome to my contact page")
#     #classbased views
    
class Myview(TemplateView):
    template_name="index.html"

def book_list(request):
     Book= book.objects.all() 
     return render(request,"book_list.html",{"books":Book})

# def book_details(request,id):
#     context ={
#         "detail":get_objects_or_404(book,pk=id)
#     }
#     return render(request,  "details.html",context)
# 
def Post_list(request):
    posts=Post.objects.all()
    paginator = Paginator(posts,1)
    page = request.GET.get('page')
    try:
        posts=paginator.page(page)
    except PageNotAnInteger:
        posts=paginator.page(1)
    except EmptyPage:
        posts=paginator.page(paginator.num_pages)

    return render(request,'index.html',{'page':page,  'posts':posts})    
    # view for single post

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status="published", publish__year=year, publish__month=month, publish__day=day)
    comments=post.Comments.filter(active =True)
    new_comment = None
    if request.method=='POST':
        comment_Form=commentForm(data =request.POST)
        if comment_Form.is_valid():
            new_comment = comment_Form.save(commit=False)
            new_comment.post=post
            new_comment.save()
    else:
        comment_Form=commentForm()
    return render(request,'post_detail.html',{'post':post,'comments':comments,'new_comment':new_comment,'comment_form':comment_Form})

