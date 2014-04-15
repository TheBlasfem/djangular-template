from django.shortcuts import render_to_response
# Create your views here.
def home(request):
	local = "Hola Mundo"
	return render_to_response('index.html', {"local": local})