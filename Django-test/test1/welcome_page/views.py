from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponseNotFound, HttpResponseBadRequest, HttpResponseForbidden
import timer

def index(request):
    host = request.META["HTTP_HOST"] # получаем адрес сервера
    user_agent = request.META["HTTP_USER_AGENT"]    # получаем данные бразера
    path = request.path     # получаем запрошенный путь
     
    return HttpResponse(f"""
        <p>Host: {host}</p>
        <p>Path: {path}</p>
        <p>User-agent: {user_agent}</p>
    """)

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
def getter(request):
	dudde= request.GET.get('name','Undefined')
	return HttpResponse(f"<h2>Name: {dudde}</h2>")

def go_out(request):
	return HttpResponseRedirect('/')