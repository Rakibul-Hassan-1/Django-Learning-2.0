from django.http import HttpResponse
import pathlib
from django.shortcuts import render
from visits.models import PageVisit
# this_dir = pathlib.Path(__file__).resolve().parent
def home_page_view(request, *args, **kwargs): 
    # print("This is file path", this_dir)
    html_ = ""
    # html_file_path = this_dir/ "home.html"
    # html_ = html_file_path.read_text()
    # return HttpResponse(html_)
    # return "hello world" # security issue are happend -> wrong 200 request
    qs = PageVisit.objects.all()
    name = "Rakib"
    my_title = {
        "myname" : name,
        "page_visits_count": qs.count(),
        "percent": ((qs.count()*100.0)/100)
    }
    html_ = "home.html"
    PageVisit.objects.create()
    return render(request, html_,my_title)