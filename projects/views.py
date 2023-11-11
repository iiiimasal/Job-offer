from collections import Counter
from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Company , Job  , Message
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User ,Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .form import JobForm ,CompanyForm ,NormalUserForm
from django.views.generic.edit import CreateView
from django.utils.decorators import method_decorator
from .utils import create_user



def loginPage(request):
    page='login'
    if request.user.is_authenticated:
        return redirect('home-page')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user=User.objects.get(username=username)
        except:

         user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home-page')
        

    context = {'page':page}
    return render(request, 'login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home-page')

def registerPage(request):
    # page='register'
    # context = {'page':page}
    form=UserCreationForm()
    return render(request, 'login_register.html', {'form':form})


def home(request):
    q = request.GET.get('q') if request.GET.get('q') is not None else ''
    companies=Company.objects.filter(Q(city__icontains=q
                              ))
    # Retrieve a list of unique cities from your Company model
    cities = Company.objects.values('city').distinct().order_by('city')

    # companies=Company.objects.all()
    context={'companies':companies,'cities': [city['city'] for city in cities]}
    return render(request, 'home.html', context) 




def Jobs(request,pk):
    jobs=Job.objects.get(id=pk)

def company(request,pk):
    company=Company.objects.get(id=pk)
    messages = Message.objects.filter(company=company)
    participants=company.participants.all()

    if request.method=='POST':
        message=Message.objects.create(
            user=request.user,
            company=company,
            body=request.POST.get('body')
            

        )
        return redirect ('companies',pk=company.pk)

    # messages=Company.messages.all()
    context={'company':company,'messages':messages ,'participants':participants}        
    return render(request,'company.html',context)


def create_normal_user(request):
    if request.method == 'POST':
        form = NormalUserForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            is_employer = form.cleaned_data.get('is_employer', False)
            is_employee = form.cleaned_data.get('is_employee', False)

            if is_employer and is_employee:
                # You may want to handle this case based on your application's logic
                return render(request, 'error_page.html', {'message': 'Please choose either employer or employee.'})
            
            user = create_user(username, email, password, is_employer=is_employer, is_employee=is_employee)

            if is_employer:
                # Redirect to the employer-specific page
                return render(request, 'employer_page.html', {'user': user})
            elif is_employee:
                # Redirect to the employee-specific page
                return render(request, 'employee_page.html', {'user': user})
            else:
                # Redirect to a default page or handle as needed
                return render(request, 'home.html', {'user': user})

    else:
        form = NormalUserForm()

    return render(request, 'user-registeration.html', {'form': form})


def userProfile(request, pk):
    user=User.objects.get(id=pk)
    companies=user.company_set.all()
    context={'user':user,'companies':companies}
    return render(request,'profile.html',context)

@login_required(login_url='login')
def createCompany(request):
    if not request.user.groups.filter(name='Employees').exists():
        # If not, redirect them to another page or show an error message
        messages.error(request, "You don't have permission to create a company.")
        return redirect('home-page')
    
    form = CompanyForm()
    if request.method == 'POST':
       form = CompanyForm(request.POST)
       if form.is_valid():
            form.save()
            return redirect('home-page')

    context = {'form': form}
    return render(request, 'Company-form.html', context)





def updatecompany(request,pk):
    company=Company.objects.get(id=pk)
    form=CompanyForm(instance=company)
    
    if request.user != company.user:
        return HttpResponse('You are not the user of this company')

    if request.method == 'POST':
       form = CompanyForm(request.POST,instance=company)
       if form.is_valid():
            form.save()
            return redirect('home-page')
    
    context = {
        'form' : form
    }

    return render(request ,"Company-form.html", context)

@login_required(login_url='login')
def deletecompany(request , pk):
    job=Job.objects.get(id=pk)
    if request.method == 'POST':
        job.delete()
        print("hello")
        return redirect('home-page')
    print("hello")
    
    return render(request,'delete.html',{'obj':job})

@login_required(login_url='login')
def deleteMessage(request , pk):
    message=Message.objects.get(id=pk)
    if request.user!=message.user:
        return HttpResponse( "You are not allowed ")
    
    if request.method == 'POST':
        message.delete()
        
        return redirect('home-page')
    
    
    return render(request,'delete.html',{'obj':message})

@login_required(login_url='login')
def create_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            # job.company = request.user.emoloyer.company  # Assign the current user's company to the job
            job.save()
            return redirect('home-page')  # Replace 'jobs-list' with the URL of the job listings page

    else:
        form = JobForm()

    return render(request, 'create-job.html', {'form': form})



def job_page(request):
    query = request.GET.get('q', '')
    jobs = Job.objects.all()
    titles = Job.objects.values('title').distinct()
    cities = Company.objects.values('city').distinct()

    if query:
        # Split the query into words
        words = query.split()

        # Create a Q object to build the filter dynamically
        q_objects = Q()

        for word in words:
            # You can define how to filter the job listings here
            # For example, you can search in job titles and company cities
            q_objects |= Q(title__icontains=word) | Q(company__city__icontains=word)

        # Apply the filter
        jobs = jobs.filter(q_objects)

    context = {'jobs': jobs, 'query': query, 'titles': titles, 'cities': cities}

    return render(request, 'jobs-list.html', context)

    

