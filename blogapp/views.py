from django.shortcuts import render,redirect # type: ignore
from blogapp.models import MyBlog
from blogapp.forms import BlogForm

# Create your views here.
def home(request):
    AllBlogs=MyBlog.objects.all()
    context={
        'blogs':AllBlogs,
    }
    print(AllBlogs)
    return render(request,'home.html',context)

def add(request):
    form=BlogForm()
    if request.method=='POST':
        form=BlogForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/home')
    context={
        'form':form,
    }
    return render(request,'add.html',context)


def destroy(request, id):
    AllBlogs = MyBlog.objects.get(id=id)
    AllBlogs.delete()
    return redirect("/home")

def edit(request, id):
    AllBlogs = MyBlog.objects.get(id=id)
    return render(request,'edit.html', {'AllBlogs':AllBlogs})

def update(request,id):
    AllBlogs=MyBlog.objects.get(id=id)
    print(id)
    print(AllBlogs)
    if request.method=='POST':
        print("hi")
        form = BlogForm(request.POST, instance=AllBlogs)
        print("blogs")
        if form.is_valid():
            print("newblog")
            form.save()
            return redirect('/home')
    return render(request,"edit.html",{'AllBlogs':AllBlogs})

def land(request):
    return render(request,'land.html')



