from django.shortcuts import render
from django.http import HttpResponse
from .models import Job_Detail, Freelancer, Job_Bid, Job_Awarded ,Client



def index(request):
    
    return render(request, 'main/index.html')

def jobsFeed(request):

    jobs = Job_Detail.objects.all()
    
    return render(request, 'main/jobsFeeds.html', { "jobsList" : jobs })

def jobDetails(request, id):
    jobs = Job_Detail.objects.get( id = id)

    return render(request, 'main/jobDetails.html', { 'job': jobs } )

def bid(request, freelancerId, jobId):
    freelancer = Freelancer.objects.get( id = freelancerId)
    job = Job_Detail.objects.get(id = jobId)

    data = {
        'job' : job,
        'freelancer' : freelancer
    }
    print("fre: "+freelancerId)
    print("job: "+jobId)

    return render(request, 'main/bid.html', {'data': data})


def register(request):

    if request.method == 'POST':

        if request.POST.get('name') and request.POST.get('email') and request.POST.get('password') and request.POST.get('skills') :
            name = request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('password')
         
            skills = request.POST.get('skills')
            post=Freelancer.objects.create(name=name, email=email, password=password, balance=0, skills=skills)      
            post.save()

            print("Registration completed")

            return render(request, 'main/jobsFeeds.html') 

    return render(request, 'freelancer/FreelancerReg.html')


def clientregister(request):

    if request.method == 'POST':

        if request.POST.get('name') and request.POST.get('email') and request.POST.get('password')  :
            name = request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('password')
         
            post=Client.objects.create(name=name, email=email, password=password, balance=0)      
            post.save()

            print("Registration completed")

            return render(request, 'main/jobsFeeds.html') 

    return render(request, 'client/clientReg.html')