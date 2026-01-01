from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateForm


def about_me(request):
    """  
        View to render the about me page.
    **Context**
    ``About`` model is designed to store and manage information about an individual or entity.
    It includes fields for the title, content, profile image, and the last updated timestamp.
    ``collaborate_form`` 
        An instance of :form:`CollaborateForm` is used to handle collaboration requests from users.
    **Template:**
    :template:`about/about.html`
    """
    about = About.objects.all().order_by('-updated_on').first()

    if request.method == "POST":
        collaborate_form = CollaborateForm(request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Collaboration request received! I endeavor to respond within 2 working days."
            )

    collaborate_form = CollaborateForm()

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "collaborate_form": collaborate_form},
    )
