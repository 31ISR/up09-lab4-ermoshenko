from django.shortcuts import render
from .models import community

def communities(req):
    communities = community.objects.all().order_by('-date')
    return render(req, 'communities/communities.html', {'communities':communities})
# Create your views here.
def community_page(request, slug):
    _community = community.objects.get(slug=slug)
    return render(request, 'communities/community_page.html', {'community': _community})