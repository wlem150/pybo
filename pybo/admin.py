from django.contrib import admin
from .models import Answer, Question


class QuestionAdmin(admin.ModelAdmin) :
  search_fields = ['subject']
  

class SampleAdmin(admin.ModelAdmin) :
  search_fields = ['content']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, SampleAdmin)

