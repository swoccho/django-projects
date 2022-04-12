from dataclasses import fields
from pyexpat import model
from django.contrib import admin
from.models import Question, Choice
# Register your models here.



class ChoiceInLine(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets= [
        (None ,               {'fields':['question_text']}),
        ("Date informantion", {'fields':['pub_date'] , 'classes': ['collapse']}),
        
    ]

    inlines = [ChoiceInLine]

    list_display = ('question_text' , 'pub_date' , 'recently_published')

    list_filter = ['pub_date']
    search_fields = ['question_text']




admin.site.register(Question , QuestionAdmin)
