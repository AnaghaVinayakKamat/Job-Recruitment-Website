from django.contrib import admin

# Register your models here.

from .models import *

class AdminCompany(admin.ModelAdmin):
    List_display = ['cname', 'cemail']

class Can_detAdmin(admin.ModelAdmin):
    List_display = ['ename', 'eemail']


admin.site.register(Com_det, AdminCompany)
admin.site.register(Can_det, Can_detAdmin)
admin.site.register(Resume)
admin.site.register(Job_det)


# class AnswerAdmin(admin.StackedInline):
#     model = Answer

# class QuestionAdmin(admin.ModelAdmin):
#     inlines=[AnswerAdmin]


# admin.site.register(Question, QuestionAdmin)
# admin.site.register(Answer)
# admin.site.register(Quiz)
admin.site.register(Apply_job)
admin.site.register(Decision)