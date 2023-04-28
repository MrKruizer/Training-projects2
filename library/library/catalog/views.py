from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from .models import *
from .forms import *
import datetime

def index(request):
	"""
	Function display for home page
	"""
	num_books = Book.objects.all().count()

	num_instances = BookInstance.objects.all().count()
	num_instances_available = BookInstance.objects.filter(status__exact='a').count()
	num_authors=Author.objects.count()

	return render(request, 'index.html', context={ 
		'num_books': num_books, 'num_instances' : num_instances, 'num_instances_available' : num_instances_available, 'num_authors' : num_authors })

@login_required
def book_detail_view(request,pk):
	try:
		book_id = Book.objects.get(pk=pk)
	except Book.DoesNotExist:
		raise Http404("Book does not exist")

	return render(request,'books/book_detail_template.html', context={'book':book_id})

@login_required
def author_detail_view(request,pk):
	try:
		author_id = Author.objects.get(pk=pk)
	except Author.DoesNotExist:
		raise Http404('Author does not exist')
	return render(request, 'author/author_detail_template.html', context={'author':author_id})

@login_required
def renew_book_librarian(request, pk):
	book_inst = get_object_or_404(BookInstance,pk=pk)
	if request.method == 'POST':
		form = RenewBookForm(request.POST)
		if form.is_valid():
			book_inst.due_back=form.cleaned_data['renewal_date']
			book_inst.save()
			return HttpResponseRedirect('/')
	else:
		proposed_renewal_date = datetime.date.today()+ datetime.timedelta(weeks=3)
		form = RenewBookForm(initial={'renewal_date': proposed_renewal_date})
	return render(request, 'books/book_renew_librarian.html',{'form': form, 'bookinst':book_inst})

class AuthorListView(LoginRequiredMixin, generic.ListView):
	model = Author
	context_object_name = 'all_author_list'
	template_name = 'authors/all_author_template.html'
	paginate_by = 5
	login_url = '/accounts/login/'
	redirect_field_name = 'redirect_to'
	def get_queryset(self):
		return Author.objects.all()

class AuthorDetailView(LoginRequiredMixin, generic.DetailView):
	model = Author
	template_name = 'authors/author_detail_template.html'
	login_url = '/accounts/login/'
	redirect_field_name = 'redirect_to'

class BookListView(LoginRequiredMixin, generic.ListView):
	model = Book
	context_object_name = 'all_book_list'
	template_name = 'books/all_book_template.html'
	paginate_by = 5
	login_url = '/accounts/login/'
	redirect_field_name = 'next'
	def get_queryset(self):
		# query
		return Book.objects.all()

	def get_context_data(self, **kwargs):
		# context
		context = super(BookListView,self).get_context_data(**kwargs)
		context['some']= 'some data'
		return context

class BookDetailView(LoginRequiredMixin, generic.DetailView):
	model = Book
	template_name = 'books/book_detail_template.html'
	login_url = '/accounts/login/'
	redirect_field_name = 'redirect_to'

class AuthorCreate(LoginRequiredMixin, CreateView):
	model = Author
	template_name = 'authors/author_form.html'
	fields = '__all__'
	initial={'date_of_death': '12/10/2016'}

class AuthorUpdate(LoginRequiredMixin, UpdateView):
	model = Author
	template_name = 'authors/author_form.html'
	fields = ['first_name','last_name','date_of_birth', 'date_of_death']

class AuthorDelete(LoginRequiredMixin, DeleteView):
	model = Author

	template_name = 'authors/author_confirm_delete.html'
	success_url = reverse_lazy('authors')