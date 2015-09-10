from django.contrib import admin
from Blogger_gender_and_age.models import Author
# Register your models here.


class authorAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['id']}),
        ('Predicted', {'fields': ['age', 'gender']}),
        ('Submetted', {'fields': ['predictedAge', 'predictedGender']}),
        ('Date',               {'fields': ['date']})
    ]
    list_display = ('id', 'age', 'gender', 'predictedAge', 'predictedGender', 'date')
    list_filter = ['date']
    search_fields = ['id']

admin.site.register(Author, authorAdmin)
