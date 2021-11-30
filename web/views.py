from django.shortcuts import render

from user.models import Address, Client, Education, Experience, Profile, Skill, SkillItems

from web.models import Contact, Subscribe, Testimonial

from works.models import Category, Project, Service

def index(request):
    profiles = Profile.objects.all()
    addresses = Address.objects.all()
    skills = Skill.objects.all()
    skillitems = SkillItems.objects.all()
    educations = Education.objects.all()
    experiences = Experience.objects.all()

    testimonials = Testimonial.objects.all()
    contacts = Contact.objects.all()
    subscribes = Subscribe.objects.all()

    service = Service.objects.all()
    category = Category.objects.all()
    project = Project.objects.all()
    clients = Client.objects.all()
    client_count = Client.objects.all().count
    project_complete = project.filter(is_completed=True).count()
    project_ongoing = project.filter(is_completed=False).count()
    client_satisfied = project.filter(is_satisfied=True).count()



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
        "service" : service,
        "category" : category,
        "project" : project

    }
    
    return render(request,"index.html", context=context)
