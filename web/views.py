from django.shortcuts import render

from user.models import Address, Client, Education, Experience, Profile, Skill, SkillItems

from web.models import Contact, Subscribe, Testimonial

from works.models import Category, Project, Service

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
        "projects" : projects

    }
    
    return render(request,"index.html", context=context)
