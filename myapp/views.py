from django.shortcuts import render

# Create your views here.
from .models import MyModel

def create_instance(request):
    # This will trigger the post_save signal
    MyModel.objects.create(name="Test Signal")
    return render(request, 'myapp/index.html')
