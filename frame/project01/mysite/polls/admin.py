from django.contrib import admin
from .models import Question, Choice
# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'publish_date')
    list_filter = ('publish_date',)     #guo lv qi
    date_hierarchy = 'publish_date'     #shi jian zhou
    search_fields = ('question',)  #sou suo kuang
    ordering = ('-publish_date', 'question_text')

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question', 'choice_text', 'votes')
    raw_id_fields = ('question', )     #bi xu shi wai jian

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)