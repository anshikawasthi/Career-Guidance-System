from django.contrib import admin

# Register your models here.
from careerguidance.models import StudentModel, CourseModel, TestModel, QuestionModel, ScholarshipModel, SoftSkillsModel

admin.site.register(StudentModel)
admin.site.register(CourseModel)
admin.site.register(TestModel)
admin.site.register(QuestionModel)
admin.site.register(ScholarshipModel)
admin.site.register(SoftSkillsModel)
