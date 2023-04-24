from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponseNotFound, HttpResponseBadRequest, HttpResponseForbidden, JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.template import RequestContext
from django.shortcuts import render
from .async_access_to_db import acreate_person
from .forms import UserForm
import asyncio

def index(request):
	cookies = request.COOKIES
	if ("name" not in cookies or "age" not in cookies or "password" not in cookies):
		return HttpResponseRedirect("/login")
	return HttpResponseRedirect("/home")

def home(request):
	name = request.get_signed_cookie("name", salt="salt")
	asyncio.run(acreate_person("Bond", "James")) 
	return render(request, "home.html", context= {'name':name, 'arr':range(1,60)})

def login(request):
	
	if request.method == "POST":
		post = request.POST
		userform = UserForm(request.POST)
		if (userform.is_valid()):
			name = request.POST.get('name')
			age = request.POST.get('age')
			password = request.POST.get('password')
			response = HttpResponseRedirect('/home', content={'name':name, 'arr':range})
			response.set_signed_cookie("name", name, salt="salt")
			response.set_signed_cookie("age", age, salt="salt")
			response.set_signed_cookie("password", password, salt="salt")
			return response
		else:
			return HttpResponse("Invalid data")
	userform = UserForm()
	return render(request, "login.html", {'login_form': userform})

def about(request, name, age):
	return HttpResponse(f"""<h2>What you're mean about us, duude?</h2>
		<p>About</p>
		<p>Name: {name}</p>
		<p>Age:{age}</p>""")

def contact(request):
	return HttpResponse("Call me maybe, sweety")

def user(request, name='Undefined', age= 0):
	return HttpResponse(f"<h2>Dudde name: {name}</h2><h3>Dudde age: {age}")

def access(request,age):
	age = int(age)
	if age not in range(1,111):
		return HttpResponseBadRequest('Incorrect age')
	elif age > 17:
		return HttpResponse("Access accept")
	else:
		return HttpResponseForbidden('Access denied')

def products(request):
	return HttpResponse(f"<h1>Product list</h1>")

def product(request, id):
	prods = ['sousege', 'milk','eggs']
	if id in prods:
		return HttpResponse(f"<h1>Product {id}</h1>")
	else:
		return HttpResponseNotFound("nope")

def new(request):
	return HttpResponse(f"<h1>New products</h1>")

def top(request):
	return HttpResponse(f"<h1>Top products</h1>")

def comments(request, id):
	return HttpResponse(f"<h1>Comments about product {id}</h1>")

def questions(request, id):
	return HttpResponse(f"<h1>Questions about product {id}</h1>")

def set_cookie(request):
	cookie = request.GET.get('cookie', 'no cookies')
	response = HttpResponseRedirect('/get_cookie')
	response.set_signed_cookie('cookie', cookie, salt='salt', max_age = 3600)
	return response

def get_cookie(request):
	cookie = request.get_signed_cookie('cookie', 'no send cookie?', 'salt')
	return HttpResponse(f"cookie: {cookie}")

def getter(request):
	dudde = request.GET.get('name','Undefined')
	response = HttpResponse(f"<h2>Name: {dudde}</h2>")
	response.set_cookie('name', dudde)
	return response

def go_out(request):
	return HttpResponseRedirect('/')

def json_resp(request):
	return JsonResponse({'name':'Tom','race':'cat'})