
from django.shortcuts import render,get_object_or_404
from .models import Post

from django.views.generic import ListView,DetailView
from .forms import CommentForm

from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.






class StartingPage(ListView):
    template_name="blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"
    def get_queryset(self):
        query = super().get_queryset()
        data = query[:3]
        return data



    





# def starting_page(request):

#     latest_post=Post.objects.all().order_by("-date")[:3]
#     return render(request,"blog/index.html",{
#         "posts":latest_post
#     })




class AllPostsView(ListView):
    template_name = "blog/all_posts.html"
    model = Post
    context_object_name = "all_posts"
    ordering = ["-date"]
    
    

# def posts(request):

#     all_posts=Post.objects.all().order_by("-date")
#     return render(request,"blog/all_posts.html",{
#         "all_posts":all_posts
#     })


# class PostDetailView(View):  
#     def get(self,request,slug):
#         post = Post.objects.get(slug=slug)
#         stored_posts = request.session.get("stored_posts")

#         if stored_posts is not None:
#             is_saved = post.id in stored_posts
#         else:
#             is_saved=False
#         context = {
#             "posts":post,
#             "post_tags":post.tags.all(),
#             "comment_form":CommentForm(),
#             "comments":post.comments.all().order_by("-id"),
#             "is_saved":is_saved

#         }
#         return render(request,"blog/post-details.html",context)



#     def post(self,request,slug):
#         comment_form=CommentForm(request.POST)
#         post = Post.objects.get(slug=slug)
#         stored_posts = request.session.get("stored_posts")

#         if stored_posts is not None:
#             is_saved = post.id in stored_posts
#         else:
#             is_saved=False
#         if comment_form.is_valid():
#             comment=comment_form.save(commit=False)  # we add commit to make an instance..so that it will not saved to the database
#             comment.post=post
#             comment.save()
#             return HttpResponseRedirect(reverse("posts-details-page",args=[slug]))
#         else:
            
#             context = {
#             "posts":post,
#             "post_tags":post.tags.all(),
#             "comment_form":comment_form,
#             "comments":post.comments.all().order_by("-id"),
#             "is_saved":is_saved

#             }
#             return render(request,"blog/post-details.html",context)




# class ReadLaterView(View):


#     def get(self,request):
        

#         stored_posts = request.session.get("stored_posts")
#         context={}

#         if stored_posts is None or len(stored_posts)==0:
#             context['posts']=[]
#             context['have_posts']=False

#         else:
#            posts= Post.objects.filter(id__in=stored_posts)
#            context['posts']=posts
#            context['have_posts']=True

#         return render(request,"blog/read-later.html",context)





#     def post(self,request):
#         stored_posts = request.session.get("stored_posts")

#         if stored_posts is None:
#             stored_posts = []


#         post_id = int(request.POST["post_id"])

#         if post_id not in stored_posts:
#             stored_posts.append(post_id)
#             request.session["stored_posts"]=stored_posts


#         return HttpResponseRedirect("/")


class SinglePostView(View):
    def is_stored_post(self, request, post_id):
        stored_posts = request.session.get("stored_posts")
        if stored_posts is not None:
          is_saved = post_id in stored_posts
        else:
          is_saved = False

        return is_saved

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        
        context = {
            "posts": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id"),
            "is_saved": self.is_stored_post(request, post.id)
        }
        return render(request, "blog/post-details.html", context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()

            return HttpResponseRedirect(reverse("posts-details-page", args=[slug]))

        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": comment_form,
            "comments": post.comments.all().order_by("-id"),
            "saved_for_later": self.is_stored_post(request, post.id)
        }
        return render(request, "blog/post-details.html", context)




class ReadLaterView(View):
    def get(self, request):
        stored_posts = request.session.get("stored_posts")

        context = {}

        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["have_posts"] = False
        else:
          posts = Post.objects.filter(id__in=stored_posts)
          context["posts"] = posts
          context["have_posts"] = True

        return render(request, "blog/read-later.html", context)


    def post(self, request):
        stored_posts = request.session.get("stored_posts")

        if stored_posts is None:
          stored_posts = []

        post_id = int(request.POST["post_id"])

        if post_id not in stored_posts:
          stored_posts.append(post_id)
        else:
          stored_posts.remove(post_id)

        request.session["stored_posts"] = stored_posts
        
        return HttpResponseRedirect("/")






    

# def post_detail(request,slug):

#     identified_post = get_object_or_404(Post,slug=slug)
#     return render(request,"blog/post-details.html",{
#         "posts":identified_post,
#         "post_tags":identified_post.tags.all()
#     })
    
