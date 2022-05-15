from django.shortcuts import render
from django.http import HttpResponse
from .models import Job_Detail, Freelancer, Job_Bid, Job_Awarded



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
            print(request.POST.get('name'))
            if request.POST.get('name') and request.POST.get('email') and request.POST.get('password') and request.POST.get('balance') and request.POST.get('skills'):
                print(request.POST.get('name'))
                name = request.POST.get('name')
                email = request.POST.get('email')
                password = request.POST.get('password')
                balance = request.POST.get('balance') 
                skills = request.POST.get('skills')
                post=Freelancer.objects.create(name=name,email=email,password=password,balance=balance,skills=skills)      
                post.save()
       
                
                return render(request, 'main/jobsFeeds.html')  

            else:
                return render(request,'main/register.html')

        else:
                return render(request,'main/register.html')

