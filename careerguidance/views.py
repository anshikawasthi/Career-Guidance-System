from careerguidance.forms import StudentForm
from careerguidance.models import StudentModel, CourseModel, TestModel, QuestionModel
from django.shortcuts import render, redirect
from .models import ScholarshipModel,SoftSkillsModel

import pandas as pd
from sklearn.preprocessing import LabelEncoder
import os

PROJECT_PATH = os.path.abspath(os.path.dirname(__name__))

from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import smtplib

def send_email(subject, body, email):
    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("atifabatool21@gmail.com", "uafopzmvjwdrtmjg")
        message = f"Subject: {subject}\n\n{body}"
        s.sendmail("atifabatool21@gmail.com", email, message)
        s.quit()
    except Exception as e:
        print("Email Error:", e)


@csrf_exempt
def submit_consultation(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        subject = "New Consultation Request"
        body = f"Name: {name}\nEmail: {email}\nMessage:\n{message}"

        send_email(subject, body, email)
        return render(request, "consultation_form.html", {"message": "Consultation submitted successfully!"})

    return render(request, "consultation_form.html")

def studentregistration(request):

    if request.method == "POST":

        registrationForm = StudentForm(request.POST)

        if registrationForm.is_valid():

            regModel = StudentModel()
            regModel.name = registrationForm.cleaned_data["name"]
            regModel.email = registrationForm.cleaned_data["email"]
            regModel.mobile = registrationForm.cleaned_data["mobile"]
            regModel.username = registrationForm.cleaned_data["username"]
            regModel.password = registrationForm.cleaned_data["password"]

            user = StudentModel.objects.filter(username=regModel.username).first()

            if user is not None:
                return render(request, 'studentregistration.html', {"message": "User All Ready Exist"})
            else:
                try:
                    regModel.save()
                    return render(request, 'studentregistration.html', {"message": "Student Added Successfully"})
                except:
                    return render(request, 'studentregistration.html', {"message": "Registration Failed"})
        else:
            return render(request, 'studentregistration.html', {"message": "Invalid Form"})

    return render(request, 'studentregistration.html', {"message": "Invalid Request"})

#===============================================================================================
def deletestudent(request):
    student=request.GET['studentid']
    StudentModel.objects.get(id=student).delete()
    return render(request, 'students.html', {'students': StudentModel.objects.all()})

def getstudents(request):
    return render(request, "students.html", {"students":StudentModel.objects.all()})
#===============================================================================================
def login(request):

    uname = request.GET["username"]
    upass = request.GET["password"]

    if uname == "Admin123" and upass == "Admin123":
        request.session['username'] = "Admin123"
        request.session['role'] = "admin"
        return render(request, 'viewcourses.html', {"courses": CourseModel.objects.all()})
    else:
        student = StudentModel.objects.filter(username=uname, password=upass).first()

        if student is not None:
            request.session['username'] = uname
            request.session['role'] = "student"
            return render(request, 'viewcourses.html', {"courses": CourseModel.objects.all()})
        else:
            return render(request, 'index.html', {"message": "Invalid Username and Password"})

def logout(request):
    try:
        del request.session['username']
    except:
        pass
    return render(request, 'index.html', {})
#==================================================================================================
def postCourse(request):
    CourseModel(name=request.GET['name'],
                base=request.GET['base'],
                website_link=request.GET['website_link'],
                ).save()
    return render(request, 'viewcourses.html', {"courses":CourseModel.objects.all()})

def getCourses(request):
    return render(request, 'viewcourses.html', {"courses":CourseModel.objects.all()})

def getCourseByCategory(request):
    category=request.GET['type']
    return render(request, 'viewcourses.html', {"courses":CourseModel.objects.filter(base=category)})

def deleteCourse(request):
    CourseModel.objects.filter(id=request.GET['course']).delete()
    return render(request, 'viewcourses.html', {"courses":CourseModel.objects.all()})
#==================================================================================================
def postTest(request):
    return render(request, 'addtest.html', {"courseid":request.GET['courseid']})

def postTestAction(request):
    TestModel(name=request.GET['name'], courseid=request.GET['courseid']).save()
    return render(request, 'viewtests.html', {"tests": TestModel.objects.filter(courseid=request.GET['courseid'])})

def getTestByCourse(request):
    courseid=request.GET['courseid']
    return render(request, 'viewtests.html', {"tests":TestModel.objects.filter(courseid=courseid)})

def deleteTest(request):
    test=TestModel.objects.get(id=request.GET['test'])
    courseid=test.courseid
    test.delete()
    return render(request, 'viewtests.html', {"tests":TestModel.objects.filter(courseid=courseid)})

def writeTest(request):
    testid=request.GET['testid']
    return render(request, 'writetest.html', {"questions":QuestionModel.objects.filter(testid=testid)})

def writeTestAction(request):

    parameters = request.GET.dict()

    rating=0
    count=0

    for key,value in parameters.items():
        rating=rating+int(value)
        count=count+1

    res=0
    if count!=0:
        res=rating/count

    message=""
    if res>=4:
        message="Excellent"
    elif res==3:
        message="Good"
    elif res == 2:
        message = "Average"
    elif res == 1:
        message = "Poor"

    return render(request, 'viewcourses.html', {"courses":CourseModel.objects.all(),"message":message})

#==================================================================================================
def postQuestion(request):
    return render(request, 'addquestion.html', {"testid":request.GET['testid']})

def postQuestionAction(request):
    QuestionModel(name=request.GET['name'], testid=request.GET['testid']).save()
    return render(request, 'viewquestions.html', {"questions": QuestionModel.objects.filter(testid=request.GET['testid'])})

def getQuestionByTest(request):
    testid=request.GET['testid']
    return render(request, 'viewquestions.html', {"questions":QuestionModel.objects.filter(testid=testid)})

def deleteQuestion(request):
    question=QuestionModel.objects.get(id=request.GET['question'])
    testid=question.testid
    question.delete()
    return render(request, 'viewquestions.html', {"questions":QuestionModel.objects.filter(testid=testid)})
#==================================================================================================

def jobroleprediction(request):

    sslc = int(request.POST["sslc"])
    hsc = int(request.POST["hsc"])
    cgpa = int(request.POST["cgpa"])
    school_type = int(request.POST["school_type"])
    no_of_miniprojects = int(request.POST["no_of_miniprojects"])
    no_of_projects = int(request.POST["no_of_projects"])
    coresub_skill = int(request.POST["coresub_skill"])
    aptitude_skill = int(request.POST["aptitude_skill"])
    problemsolving_skill = int(request.POST["problemsolving_skill"])
    programming_skill = int(request.POST["programming_skill"])
    abstractthink_skill = int(request.POST["abstractthink_skill"])
    design_skill = int(request.POST["design_skill"])
    lab_programs = int(request.POST["lab_programs"])
    ds_coding = int(request.POST["ds_coding"])
    technology_used = int(request.POST["technology_used"])
    sympos_attend = int(request.POST["sympos_attend"])
    sympos_won = int(request.POST["sympos_won"])
    extracurricular = int(request.POST["extracurricular"])
    learning_style = int(request.POST["learning_style"])
    college_performence = int(request.POST["college_performence"])
    college_skills = int(request.POST["college_skills"])

    dataset = pd.read_csv(PROJECT_PATH+"/dataset/career_compute_dataset.csv")
    labelencoder = LabelEncoder()
    df = dataset
    label = df.iloc[:49, -1]
    original = label.unique()
    label = label.values
    label2 = labelencoder.fit_transform(label)
    y = pd.DataFrame(label2, columns=["ROLE"])
    numeric = y["ROLE"].unique()
    y1 = pd.DataFrame({'ROLE': original, 'Associated Number': numeric})
    print(y1)

    import pickle
    loaded_model = pickle.load(open(PROJECT_PATH+"/model/final_model.pkl", "rb"))

    cols_when_model_builds = loaded_model.get_booster().feature_names
    print(cols_when_model_builds)

    x_new = [sslc, hsc, cgpa, school_type, no_of_miniprojects,
       no_of_projects, coresub_skill, aptitude_skill,
       problemsolving_skill, programming_skill, abstractthink_skill,
       design_skill, lab_programs, ds_coding, technology_used,
       sympos_attend, sympos_won, extracurricular, learning_style,
       college_performence, college_skills]

    l = ['f0', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12', 'f13', 'f14', 'f15', 'f16',
         'f17', 'f18', 'f19', 'f20']
    df = pd.DataFrame([x_new],columns=l)

    new_pred = loaded_model.predict(df)
    label=y1.loc[y1['Associated Number'] == new_pred[0], 'ROLE'].tolist()[0]

    return render(request, "jobroleprediction.html",{"result":"Suggested Job Role : {}".format(label)})

#-------------------------------------------------------------------------------------------------------
def postScholarship(request):
    ScholarshipModel.objects.create(
        name=request.GET['name'],
        stateorcentral=request.GET['stateorcentral'],
        tenthper=request.GET['tenthper'],
        twelvethper=request.GET['twelvethper'],
        cast=request.GET['cast'],
        sport=request.GET['sport'],
        gender=request.GET['gender'],
        income=request.GET['income'],
        isdisable=request.GET['isdisable'],
        lastdate=request.GET['lastdate'],
    )
    return render(request, 'viewscholarships.html', {"scholarships": ScholarshipModel.objects.all()})

def getScholarships(request):
    return render(request, 'viewscholarships.html', {"scholarships": ScholarshipModel.objects.all()})

def deleteScholarship(request):
    ScholarshipModel.objects.filter(id=request.GET.get('scholarship')).delete()
    return render(request, 'viewscholarships.html', {"scholarships": ScholarshipModel.objects.all()})

#-------------------------------------------------------------------------------------------------------mh
def postSoftSkill(request):
    if request.method == 'GET':
        SoftSkillsModel.objects.create(
            title=request.GET['title'],
            link=request.GET['link'],
        )
        return redirect('get_soft_skills')

def getSoftSkills(request):
    skills = SoftSkillsModel.objects.all()
    return render(request, 'viewsoftskills.html', {"skills": skills})

def getSoftSkillByTitle(request):
    title = request.GET.get('title')
    skills = SoftSkillsModel.objects.filter(title__icontains=title)
    return render(request, 'viewsoftskills.html', {"skills": skills})

def deleteSoftSkill(request):
    skill_id = request.GET.get('skill')
    SoftSkillsModel.objects.filter(id=skill_id).delete()
    return redirect('get_soft_skills')

