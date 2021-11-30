from django.shortcuts import render

from web.models import Contact, Subscribe, Testimonial


def index(request):
    testimonials = Testimonial.objects.all()
    contacts = Contact.objects.all()
    subscribes = Subscribe.objects.all()

    context = {
        "testimonials" : testimonials,
        "contacts" : contacts,
        "subscribes" : subscribes  
    }
    
    return render(request,"index.html", context=context)