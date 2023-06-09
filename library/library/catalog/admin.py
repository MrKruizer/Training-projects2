from .models import *
from django.contrib import admin

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
	list_filter = ('status', 'due_back', 'book')
	fieldsets = (
		(None, {
			'fields': ('book','imprint', 'id')
		}),
		('Availability', {
			'fields': ('status', 'due_back')
		}),
	)

class BooksInstanceInline(admin.TabularInline):
	model = BookInstance
	fk_name = 'book'

class BooksInline(admin.TabularInline):
	model = Book
	fk_name = 'author'

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'display_genre')
	inlines = [BooksInstanceInline]

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	 list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
	 fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
	 inlines = [BooksInline]

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
	pass
