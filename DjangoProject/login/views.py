from django.shortcuts import render
from httpresponses import HttpResponses

# Create your views here.
def main(requests):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())