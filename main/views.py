from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Job_Detail, Freelancer, Job_Bid, Job_Awarded ,Client
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout




def index(request):
    
    return render(request, 'public/test.html')

def jobsFeed(request):

    print(request.user.username)
    username = request.user.username

    jobs = Job_Detail.objects.all()
    
    return render(request, 'public/jobsFeeds.html', { "jobsList" : jobs, "username": username })

def jobDetails(request, id):
    jobs = Job_Detail.objects.get( id = id)

    return render(request, 'public/jobDetails.html', { 'job': jobs } )

def bid(request, jobId):
    
    job = Job_Detail.objects.get(id = jobId)
    current_user = request.user
    
    freelancer = Freelancer.objects.all()

    print (current_user.email);
    
    free_id = None;

    for x in freelancer:
        if(current_user.username==x.email):
            free_id = x.id;
            break;
    
    print (free_id);

    if request.method == 'POST':
        if request.POST.get('proposed_message') and request.POST.get('proposed_amount') :
            proposed_message = request.POST.get('proposed_message')
            proposed_amount = request.POST.get('proposed_amount')
            bid = Job_Bid.objects.create(freelancer_iD=free_id,proposal_message=proposed_message,proposed_amount=proposed_amount,job_id=jobId)
            bid.save()
            print("Bid completed")
            return render(request, 'public/bid.html')
    data = {
        'job' : job,
        # 'freelancer' : freelancer
    }
    # print("fre: "+freelancerId)
    print("job: "+jobId)

    return render(request, 'public/bid.html')


def freelancerRegister(request):
    if request.method == 'POST':
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
    if request.method == 'POST':
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
    return redirect(clientLogin) 