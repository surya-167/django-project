from django.shortcuts import render
from httpresponses import HttpResponses

# Create your views here.
def main(requests):
    template = loader.get_template('login.html')
    context={img="media/profile-user.png",
    img2="zzz.jppeg"}
    
    return HttpResponse(template.render(),context)
