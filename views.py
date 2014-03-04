from django.contrib.auth.models import User
from myEfforts.models import *
from django.shortcuts import render, get_object_or_404
from django.http import StreamingHttpResponse,HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.decorators.csrf import csrf_protect
from myEfforts.forms import *
from django.shortcuts import render_to_response
import time

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render(RequestContext(request,'')))

def signup(request):
    template = loader.get_template('signup.html')
    return HttpResponse(template.render(RequestContext(request,'')))

def success(request):
    template = loader.get_template('success.html')
    return HttpResponse(template.render(RequestContext(request,'')))

def work(request):
    template = loader.get_template('work.html')
    return HttpResponse(template.render(RequestContext(request,'')))

def eventList(request):
    eventList=[]
    currDate=time.strftime('%Y-%m-%d')
    for ev in event.objects():
        date=unicode(ev.eventDate.date())
        if date >= currDate:
            eventList.append(ev)

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = signupForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                    username=form.cleaned_data['username'],
                    email=form.cleaned_data['email'],
                    password = form.cleaned_data['password1'],
                )
            choice=form.cleaned_data['choice_field']
            if choice == '2':
                return HttpResponseRedirect('/register/user/'+user.email)
            else:
                return HttpResponseRedirect('/register/ngo/'+user.email)
        
        else:
            variables = RequestContext(request, {
                    'form':form
                })
    else:
        form = signupForm()
        variables = RequestContext(request, {
                'form':form
            })
    return render_to_response(
            'register.html',
            variables,
        )

def regCustomer(request,email):
    print email
    if request.method == 'POST':
        form = commonUserRegistration(request.POST,request.FILES)
        if form.is_valid():
            print "no error"
            p=''
            if form.cleaned_data['profession']=='1':
                p='student'
            else:
                p='proffessional'
            g=''
            if form.cleaned_data['gender']=='1':
                g='M'                                 
            else:
                g='F'
            emailID=email
            print User.objects.get(email=emailID)
            customer = commonUser.objects.create(
                    user=User.objects.get(email=emailID),
                    firstName=form.cleaned_data['firstName'],
                    lastName=form.cleaned_data['lastName'],
                    contactNumber = form.cleaned_data['contactNumber'],
                    profession=p,
                    gender=g,
                    dob=form.cleaned_data['dob'],
                    profilePic=form.cleaned_data['profilePic'],                    
                )
            return HttpResponseRedirect('/register/success/')
        else:
            print "Error occurred"
            variables = RequestContext(request, {
			'form': form
			})
            return render_to_response(
                'regCustomer.html',
                variables,
            )
    else:
        form=commonUserRegistration()
        variables = RequestContext(request,{
                'form':form
            })
        return render_to_response(
                'regCustomer.html',
                variables,
            )

def regNgo(request,email):
    print email
    if request.method == 'POST':
        form = ngoRegistration(request.POST,request.FILES)
        if form.is_valid():
            print "No error"
            emailID=email
            customer = commonUser.objects.create(
                    user=User.objects.filter(email=emailID),
                    ngoName=form.cleaned_data['ngoName'],
                    manFirstName=form.cleaned_data['manFirstName'],
                    manLastName=form.cleaned_data['manLastName'],
                    manContactNumber = form.cleaned_data['manContactNumber'],
                    ngoAddress=form.cleaned_data['ngoAddress'],
                    ngoContactNum=form.cleand_data['ngoContactNumber'],
                    ngoDetails=form.cleaned_data['ngoDetails'],
                    ngoUrl=form.cleaned_data['ngoURL'],
                    ngoProfilePic=form.cleaned_data['profilePic'],                    
                )
            return HttpResponseRedirect('/register/success/')
        else:
            variables = RequestContext(request, {
			'form': form
			})
            return render_to_response(
                'regCustomer.html',
                variables,
            )
    else:
        form=ngoRegistration()
        variables = RequestContext(request,{
                'form':form
            })
        return render_to_response(
                'regNGO.html',
                variables,
            )
