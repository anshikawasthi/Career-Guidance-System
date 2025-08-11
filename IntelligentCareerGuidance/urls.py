"""
URL configuration for IntelligentCareerGuidance project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from careerguidance.views import login, getCourses, deleteCourse, getCourseByCategory, getTestByCourse, deleteTest, \
    getQuestionByTest, deleteQuestion, postQuestion, postQuestionAction, postTest, postTestAction, postCourse, \
    studentregistration, logout, jobroleprediction, writeTest, writeTestAction, postScholarship, getScholarships, \
    deleteScholarship, postSoftSkill, getSoftSkills, deleteSoftSkill, submit_consultation

urlpatterns = [

    path('admin/', admin.site.urls),

    path('',TemplateView.as_view(template_name = 'index.html'),name='login'),

    path('login/',TemplateView.as_view(template_name = 'login.html'),name='login'),
    path('loginaction/',login,name='loginaction'),

    path('studentregistration/',TemplateView.as_view(template_name = 'studentregistration.html'),name='registration'),
    path('studentregaction/',studentregistration,name='regaction'),

    path('postcourse/',TemplateView.as_view(template_name = 'addcourse.html'),name='addcourse'),
    path('postcourseaction/',postCourse,name='addcourse'),
    path('getcourses/',getCourses,name='view courses'),
    path('getcoursesbycategory/',getCourseByCategory,name='view courses'),
    path('deletecourse/',deleteCourse,name='delete courses'),

    path('posttest/',postTest,name='addtest'),
    path('posttestaction/',postTestAction,name='addtest'),
    path('gettestsbycourse/',getTestByCourse,name='view tests'),
    path('deletetest/',deleteTest,name='delete tests'),

    path('postquestion/',postQuestion,name='addquestion'),
    path('postquestionaction/',postQuestionAction,name='addquestion'),
    path('getquestionsbytest/',getQuestionByTest,name='view questions'),
    path('deletequestion/',deleteQuestion,name='delete questions'),

    path('jobroleprediction/', TemplateView.as_view(template_name='jobroleprediction.html'), name='predict'),
    path('jobrolepredictionaction/', jobroleprediction, name='predict'),

    path('starttest/',writeTest, name='predict'),
    path('writetestaction/', writeTestAction, name='predict'),


    path('post-scholarship/', TemplateView.as_view(template_name='addscholarship.html'), name='predict'),
    path('post-scholarship-action/', postScholarship, name='post_scholarship'),
    path('get-scholarships/', getScholarships, name='get_scholarships'),
    path('delete-scholarship/', deleteScholarship, name='delete_scholarship'),

    path('post-soft-skill/', TemplateView.as_view(template_name='addsoftskills.html'), name='predict'),
    path('post-soft-skill-action/', postSoftSkill, name='post_soft_skill'),
    path('get-soft-skills/', getSoftSkills, name='get_soft_skills'),
    path('delete-soft-skill/', deleteSoftSkill, name='delete_soft_skill'),

    path('consultation/', TemplateView.as_view(template_name='consultation_form.html'), name='submit_consultation'),
    path('submitconsultation/', submit_consultation, name='submit_consultation'),

    path('logout/',logout,name='logout'),
]
