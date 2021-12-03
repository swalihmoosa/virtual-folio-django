import json

from django.http.response import HttpResponse

from django.shortcuts import redirect, render

from web.forms import ContactForm, SignupForm, SubscribeForm

from user.models import Address, Client, Education, Experience, Profile, Skill, SkillItems

from web.models import Contact, Login, Signup, Subscribe, Testimonial

from works.models import Category, Project, Service
from django.contrib.auth import authenticate


def index(request):
    category_name = request.GET.get("category")

    profiles = Profile.objects.all()
    addresses = Address.objects.all()
    skills = Skill.objects.all()
    skillitems = SkillItems.objects.all()
    educations = Education.objects.all()
    experiences = Experience.objects.all()

    testimonials = Testimonial.objects.all()
    contacts = Contact.objects.all()
    subscribes = Subscribe.objects.all()

    services = Service.objects.all()
    categories = Category.objects.all()
    projects = Project.objects.all()
    clients = Client.objects.all()
    client_count = Client.objects.all().count
    project_complete = projects.filter(is_completed=True).count()
    project_ongoing = projects.filter(is_completed=False).count()
    client_satisfied = projects.filter(is_satisfied=True).count()
    form = ContactForm()
    subscribe_form = SubscribeForm()

    if category_name:
        projects = projects.filter(category__name=category_name)
    else:
        projects = projects.filter()[:6]



    context = {
        "profiles" : profiles,
        "addresses" : addresses,
        "skills" : skills,
        "skillitems" : skillitems,
        "educations" : educations,
        "experiences" : experiences,
        "clients" : clients,
        "client_count" : client_count,
        "project_complete" : project_complete,
        "project_ongoing" : project_ongoing,
        "client_satisfied" : client_satisfied,
        "testimonials" : testimonials,
        "contacts" : contacts,
        "subscribes" : subscribes,
        "services" : services,
        "categories" : categories,
        "projects" : projects,
        "form" : form,
        "subscribe_form" : subscribe_form,
    }
    
    return render(request,"index.html", context=context)


def contact(request):
    form = ContactForm(request.POST)

    if form.is_valid():
        if not Contact.objects.filter(email=request.POST.get('email')).exists():
            form.save()

            response_data = {
                "status" : "success",
                "title" : "Successfully Registered",
                "message" : "You are Subscribed to the News Letter"
            }
        else:
            response_data = {
                "status" : "error",
                "title" : "Already Registered",
                "message" : "You are Already Subscribed to the News Letter,no need to Subscribe again"
            }
    else:
        response_data = {
                "status" : "error",
                "title" : "Your Form is Not Valid",
                "message" : "Your Form is Not Valid,Try again"
            }

    return HttpResponse(json.dumps(response_data),content_type="application/javascript")


def subscribe(request):
    subscribe_form = SubscribeForm(request.POST)

    if subscribe_form.is_valid():
        if not Subscribe.objects.filter(email=request.POST.get('email')).exists():
            subscribe_form.save()

            response_data = {
                "status" : "success",
                "title" : "Successfully Registered",
                "message" : "You are Subscribed to the News Letter"
            }
        else:
            response_data = {
                "status" : "error",
                "title" : "Already Registered",
                "message" : "You are Already Subscribed to the News Letter,no need to Subscribe again"
            }
    else:
        response_data = {
                "status" : "error",
                "title" : "Your Form is Not Valid",
                "message" : "Your Form is Not Valid,Try again"
    }

    return HttpResponse(json.dumps(response_data),content_type="application/javascript")


def login(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = Signup.objects.filter(username=username,password=password)

    if user:
        return redirect("/")
    else:
        print("######################################################","error")

    return render(request,"login.html")


def signup_page(request):
    signup_form = SignupForm()

    context = {
        "form" : signup_form
    }

    return render(request,"signup.html",context=context)



def signup(request):
    signup_form_model = SignupForm(request.POST)

    if signup_form_model.is_valid():
        if not Signup.objects.filter(username=request.POST.get('username')).exists():
            signup_form_model.save()

            response_data = {
                "status" : "success",
                "title" : "Successfully Registered",
                "message" : "You are Subscribed to the News Letter"
            }
        else:
            response_data = {
                "status" : "error",
                "title" : "Already Registered",
                "message" : "You are Already Subscribed to the News Letter,no need to Subscribe again"
            }
    else:
        response_data = {
                "status" : "error",
                "title" : "Your Form is Not Valid",
                "message" : "Your Form is Not Valid,Try again"
    }

    return HttpResponse(json.dumps(response_data),content_type="application/javascript")
