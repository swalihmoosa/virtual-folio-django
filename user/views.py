from django.shortcuts import render

from user.models import Address, Client, Education, Experience, Profile, Skill, SkillItems

def index(request):
    profiles = Profile.objects.all()
    addresses = Address.objects.all()
    skills = Skill.objects.all()
    skillitems = SkillItems.objects.all()
    educations = Education.objects.all()
    experiences = Experience.objects.all()
    clients = Client.objects.all()

    context = {
        "profiles" : profiles,
        "addresses" : addresses,
        "skills" : skills,
        "skillitems" : skillitems,
        "educations" : educations,
        "experiences" : experiences,
        "clients" : clients
    }
    
    return render(request,"index.html", context=context)
