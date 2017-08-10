from django.http import HttpResponse
from django.template import loader
from .models import financials_2015

def index(request):
   #return HttpResponse("<h2>Details for working list customers:</h2>")
    all_worklist = financials_2015.objects.all()
    template = loader.get_template('table/index.html')
    context = {
       'all_worklist': all_worklist,
   }
    return HttpResponse(template.render(context,request))

def detail(request, financials_2015_id):
    return HttpResponse("<h2>Details for working list customers:  " + str(financials_2015_id) + "</h2>")