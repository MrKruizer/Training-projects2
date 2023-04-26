from django.urls import reverse
from django.db import models
import uuid

class Genre(models.Model):
	"""
	Model representing a book genre (e.g. Science Fiction, Non Fiction).
	"""
	name = models.CharField(max_length=200,help_text='Enter a book genre (e.g. Science Fiction, French Poetry etc.)')

	def __str__(self):
		return self.name

class Author(models.Model):
	"""
	Model representing an author
	"""
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	date_of_birth = models.DateField(null=True, blank=True)
	date_of_death = models.DateField('Died', null=True, blank=True)

	def get_books(self):
		return Book.objects.filter(author_id=self.pk)

	def get_absolute_url(self):
		return reverse('author-detail', args=[str(self.id)])

	def __str__(self):
		return f'{self.last_name} {self.first_name}'

class Book(models.Model):
	"""
	Model representing a book (but not a specific copy of a book).
	"""
	title = models.CharField(max_length=200)
	author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
	summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
	isbn = models.CharField('ISBN',max_length=13,help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
	genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')

	LANGUAGE = (
			('ru', 'Russian'),
			('en', 'English'),
			('ger', 'German'),
			('fr', 'French'),
		)
	lang = models.CharField('Language',max_length=3,choices=LANGUAGE, default='ru', help_text='Language of book')

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('book-detail', args=[str(self.id)])

	def display_genre(self):
		"""
		Creates a string for the Genre. This is required to display genre in Admin.
		"""
		return ', '.join([ genre.name for genre in self.genre.all()[:3] ])
		display_genre.short_description = 'Genre'

class BookInstance(models.Model):
	"""
	Model representing a specific copy of a book (i.e. that can be borrowed from the library).
	"""
	id = models.UUIDField(primary_key=True,default=uuid.uuid4,help_text='Unique ID for this particular book across whole library')
	book = models.ForeignKey('Book', on_delete=models.SET_NULL,null=True)
	imprint = models.CharField(max_length=200)
	due_back = models.DateField(null=True,blank=True)

	LOAN_STATUS = (
			('m', 'Maintenance'),
			('o', 'On loan'),
			('a', 'Avaible'),
			('r', 'reserved'),
		)

	status = models.CharField(max_length=1, choices=LOAN_STATUS,blank=True, default='m',help_text='Book avaibility')

	class Meta:
		ordering = ["due_back"]

	def __str__(self):
		return f'{self.id} {self.book.title}'

	def title(self):
		return self.book.title