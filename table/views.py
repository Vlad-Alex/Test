from django.http import HttpResponse
from django.template import loader
from .models import Worklist

def index(request):
   #return HttpResponse("<h2>Details for working list customers:</h2>")
    all_worklist = Worklist.objects.all()
    template = loader.get_template('worklist/index.html')
    context = {
       'all_worklist': all_worklist,
   }
    return HttpResponse(template.render(context,request))

def detail(request, worklist_id):
    return HttpResponse("<h2>Details for working list customers:  " + str(worklist_id) + "</h2>")