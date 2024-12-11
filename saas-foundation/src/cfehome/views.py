from django.http import HttpResponse
import pathlib
from django.shortcuts import render

# this_dir = pathlib.Path(__file__).resolve().parent
def home_page_view(request, *args, **kwargs): 
    # print("This is file path", this_dir)
    html_ = ""
    # html_file_path = this_dir/ "home.html"
    # html_ = html_file_path.read_text()
    # return HttpResponse(html_)
    # return "hello world" # security issue are happend -> wrong 200 request
    name = "Rakib"
    my_title = {
        "myname" : name
    }
    html_ = "home.html"
    return render(request, html_,my_title)