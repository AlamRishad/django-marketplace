from ast import Return
from queue import Empty
from tkinter.messagebox import NO
from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Job_Detail, Freelancer, Job_Bid, Job_Awarded, Job_Bid, Client , Blog ,Blog_Comment

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def firstpage(request):
    return render(request, 'public/firstpage.html')

def home(request):

    return render(request, 'public/test.html')

def jobsFeed(request):
    jobs = Job_Detail.objects.all()
    return render(request, 'public/jobsFeeds.html', { "jobsList" : jobs })

def jobDetails(request, id):
    jobs = Job_Detail.objects.get(id = id)
   
    session_email = request.user.email
    freelancer = Freelancer.objects.all()
    biddingData = Job_Bid.objects.filter(job_id_id = id)
    free_id = -1
    for x in freelancer:
        if(session_email== x.email):
            free_id = x.id
            break

    is_freelancer=True
    if(free_id == -1):
      is_freelancer=False; 
   
    is_Bidden=False
  
    if(is_freelancer == True):
       if(Job_Bid.objects.filter(freelancer_id_id = free_id ).filter(job_id_id=jobs).all().count() > 0):
         is_Bidden=True
       
    return render(request, 'public/jobDetails.html', { 'job': jobs, "is_freelancer": is_freelancer, "biddingData": biddingData, "is_Bidden": is_Bidden } )

def bid(request, jobId):
    job = Job_Detail.objects.get(id = jobId)

    session_email = request.user.email
    
    freelancer = Freelancer.objects.all()

    free_id = None
    for x in freelancer:
        if(session_email== x.email):
            free_id = x.id;
            break;

    is_freelancer = free_id is not None if True else False

    if not is_freelancer:
        return render(request, 'freelancer/freelancerLogin.html')    
   
    print (free_id);

    if request.method == 'POST':
        if request.POST.get('proposed_message') and request.POST.get('proposed_amount') :
            proposed_message = request.POST.get('proposed_message')
            proposed_amount = request.POST.get('proposed_amount')
            bid = Job_Bid.objects.create(freelancer_id_id = free_id, proposal_message=proposed_message,proposed_amount=proposed_amount, job_id_id = jobId)
            bid.save()
            print("Bid completed")

    print("job: "+jobId)

    return redirect(jobDetails)


def freelancerRegister(request):
    if request.method == 'GET':
        return render(request, 'freelancer/FreelancerReg.html')

    elif request.method == 'POST':
        if request.POST.get('name') and request.POST.get('email') and request.POST.get('password') and request.POST.get('skills') :
            name = request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            skills = request.POST.get('skills')

            user = User.objects.create_user(email, email, password)
            user.save()
         
            post = Freelancer.objects.create(name=name, email=email, password=password, balance=0, skills=skills)      
            post.save()

            print("Registration completed")

            return redirect(freelancerLogin) 
    return render(request, 'freelancer/FreelancerReg.html')


def clientRegister(request):
    if request.method == 'GET':
        return render(request, 'client/clientReg.html')

    elif request.method == 'POST':
        if request.POST.get('name') and request.POST.get('email') and request.POST.get('password')  :
            name = request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('password')

            user = User.objects.create_user(email, email, password)
            user.save()

            client = Client.objects.create(name = name, email = email, password = password, balance = 0)
            client.save() 

            print("Registration completed")
            return  redirect(clientLogin) 
    return render(request, 'client/clientReg.html')

def clientLogin(request):

    if request.method == 'GET':
        return render(request, 'client/clientLogin.html')

    elif request.method == 'POST':
        if request.POST.get('email') and request.POST.get('password') :
            email = request.POST.get('email')
            password = request.POST.get('password')
            print(email, password)
            user = authenticate(request, username = email, password = password)

            if user is not None:
                login(request, user)
                print("Logged in")
                return redirect(jobsFeed)
                # Redirect to a success page.
                ...
            else:
                print("Ah Snap!")
                # Return an 'invalid login' error message.           
                return render(request, 'client/clientLogin.html')
           
def freelancerLogin(request):

    if request.method == 'GET':
        return render(request, 'freelancer/freelancerLogin.html')

    if request.method == 'POST':
        if request.POST.get('email') and request.POST.get('password') :
            email = request.POST.get('email')
            password = request.POST.get('password')
            print(email, password)
            user = authenticate(request, username = email, password = password)

            if user is not None:
                login(request, user)
                print("Logged in")
                return redirect(jobsFeed)
                # Redirect to a success page.
                ...
            else:
                print("Ah Snap!")
                # Return an 'invalid login' error message.           
                return render(request, 'freelancer/freelancerLogin.html')            


def logoutUser(request):
    logout(request)
    return redirect(firstpage) 

def jobCreate(request):
    session_email = request.user.email
    client = Client.objects.all()

    client_id = None
    for x in client:
        if(session_email== x.email):
            client_id = x.id;
            break;

    awarded = False;
    if request.method == 'GET':
        return render(request, 'client/clientJobCreate.html')

    if request.method == 'POST':
        if request.POST.get('job_title') and request.POST.get('job_desc') and request.POST.get('job_budget'):
            Job_title = request.POST.get('job_title')
            Job_desc = request.POST.get('job_desc')
            Job_Budget=request.POST.get('job_budget')
            job_details = Job_Detail.objects.create(Job_title=Job_title ,Job_desc = Job_desc ,Job_Budget=Job_Budget ,Job_Created_id = client_id  , Job_Awarded = awarded );
            job_details.save()
            return  redirect(jobsFeed)

    return render(request, 'client/clientJobCreate.htm')

     
def blogCreate(request):
    session_name = request.user.username
    session_email = request.user.email

    print(session_name);
    client = Client.objects.all()
    if request.method == 'GET':
        return render(request, 'Blog/CreateBlog.html')

    if request.method == 'POST':
        if request.POST.get('blog_title') and request.POST.get('blog_desc') :
            blog_title = request.POST.get('blog_title')
            blog_desc = request.POST.get('blog_desc')
           
            blog_details = Blog.objects.create(blog_title=blog_title ,blog_desc = blog_desc ,blog_writer=session_name );
            blog_details.save()
            return  redirect(blogs)

    return render(request, 'Blog/createBlog.html')

def blogs(request):
    blogs = Blog.objects.all()
    session_id = request.user.id
    return render(request, 'Blog/blogs.html', { "blogList" : blogs ,"user" : session_id})


def blogDetail(request,blogid):
    blogs = Blog.objects.get(id = blogid)
    print(blogs)
    session_id = request.user.id
    session_name = request.user.username
    if request.method == 'POST':
        print("Comment completed")
        if request.POST.get('comment_desc'):
            comment_desc = request.POST.get('comment_desc')
            comment = Blog_Comment.objects.create(blog_comment_id = blogid, comment_writer=session_name,comment_desc=comment_desc)
            comment.save()
            print("Comment completed")
    
    commentData = Blog_Comment.objects.filter(blog_comment_id = blogid)     
    return render(request, 'Blog/blogDetail.html', { "blog" : blogs ,"user" : session_id , "commentData":commentData })
   
    