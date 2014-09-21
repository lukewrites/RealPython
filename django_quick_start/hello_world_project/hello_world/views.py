from django.template import Context, loader
from datetime import datetime
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<html><body>Hello, world!</body></html>')


def about(request):
    return HttpResponse('This is the About Page. Want to return home? <a href="/">Back Home</a>')


def help(request):
    return HttpResponse('<html><body><h1>So you need help?</h1><p>Christ, so do we all.</body></html>')


def better(request):
    t = loader.get_template('betterhello.html')
    c = Context({'current_time': datetime.now(),})
    return HttpResponse(t.render(c))
