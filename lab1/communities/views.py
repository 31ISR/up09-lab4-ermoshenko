from django.shortcuts import render
from .models import community

def communities(req):
    communities = community.objects.all().order_by('-date')
    return render(req, 'communities/communities.html', {'communities':communities})
# Create your views here.
