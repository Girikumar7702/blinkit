from django.http import HttpResponse
# create your views here
def home(request):
    return HttpResponse("Hello,world! this is the home page of blinkitapp.")

# Create your views here.
