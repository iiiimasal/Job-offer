from collections import Counter
from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Company , Job ,Employee , Message
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User ,Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .form import JobForm ,CompanyForm ,EmployerRegistrationForm
from django.views.generic.edit import CreateView
from django.utils.decorators import method_decorator



#  q=request.GET.get('q') if request.GET.get('q') !=None else ''

#  Companies=Company.objects.filter(
#                               Q(name__icontains=q)|
#                               Q(city__icontains=q)
#                               )

#  context={'Companies':Companies}
# Companies=Company.objects.all()
# context={'companies':Companies}

# return render(request,'home.html',context) 

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

# def home(request):
#     q = request.GET.get('q', '') if request.GET.get('q') is not None else ''
#     # jobs=Job.objects.filter(Q(topic__name__icontains=q)|
#     #                           Q(name__icontains=q)|
#     #                           Q(description__icontains=q)
#     #                           )
#     # Retrieve a list of unique cities from your Company model
#     cities = Company.objects.values('city').distinct().order_by('city')

#     jobs=Job.objects.all()
#     context = {'jobs':jobs,'cities': [city['city'] for city in cities], 'q': q }
#     print(jobs)
#     return render(request, 'home.html', context) 

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





def employer_registration(request):
    if request.method == 'POST':
        form = EmployerRegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                first_name=form.cleaned_data['first_name'],  # Add first name field
                last_name=form.cleaned_data['last_name'],    # Add last name field
                # gender=form.cleaned_data['gender'],
                city=form.cleaned_data['city'],
                certificate=form.cleaned_data['certificate'],
                degree=form.cleaned_data['degree'],
                age=form.cleaned_data['age'],
                job=form.cleaned_data['job'],
            )

            # Check if the user chose to be an employee
            if form.cleaned_data.get('is_employer'):
                employee_group, created = Group.objects.get_or_create(name='Employers')
                user.groups.add(employer_group)
            else:
                employer_group, created = Group.objects.get_or_create(name='Employees')
                user.groups.add(employee_group)
            return redirect('login')  # Use the correct name of your login view

    else:
        form = EmployerRegistrationForm()

    return render(request, 'employer-register.html', {'form': form})


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
    q = request.GET.get('q') if request.GET.get('q') is not None else ''
    city = request.GET.get('city', '')
    jobs = Job.objects.filter(title__icontains=q, company__city__icontains=city)
    titles = Job.objects.values('title').distinct()
    cities = Company.objects.values('city').distinct()
    
    context = {'jobs': jobs, 'titles': titles, 'cities': cities}

    # companies=Company.objects.all()
    context={'jobs':jobs,'titles':titles,'cities':cities}
    print(context)
    return render(request, 'jobs-list.html', context) 
