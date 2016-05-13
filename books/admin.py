from django.contrib import admin
from .models import Book, Author

@admin.register(Book)
# Register your models here.
class BookAdmin(admin.ModelAdmin):
	fieldsets= [
		("Book details",{"fields":["title","authors"]}),
		("Review",{"fields":["is_favourite","review","date_review"]})
	]

	readonly_fields = ('date_review',)

	def book_authors(self, obj):
		return obj.list_authors()

	list_display = ("title","book_authors","date_review","is_favourite")

	book_authors.short_description = "Author(s)"
	list_editable = ("is_favourite",)
	list_display_links = ("title","date_review",)
	list_filter = ("is_favourite",)
	search_fields = ("title","authors__name",)


admin.site.register(Author)