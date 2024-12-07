from django.shortcuts import render

from . import models

# Create your views here.
def index(request):
    """The Student Dashboard page."""
    return render ("reviews/student-dashboard/student-dashboard.html")
