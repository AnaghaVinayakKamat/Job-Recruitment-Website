from asyncio import get_event_loop_policy
import imp
import random
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from myproject.settings import *
from .models import *
from django.http import HttpResponse, JsonResponse
from django.template.loader import get_template
from io import *
from xhtml2pdf import pisa

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


# candidate registration
def candireg(request):
    if request.method == 'GET':
        return render(request, 'candireg.html')
    else:
        ename=request.POST['ename']
        username=request.POST['username']
        epasswd=request.POST['epasswd']
        ephn=request.POST['ephn']
        eaddr=request.POST['eaddr']
        estate=request.POST['estate']
        ecity=request.POST['ecity']
        ezip=request.POST['ezip']
        egen=request.POST['egen']

        error_message = None

        # form after error
        value={'ename': ename, 'username': username, 'eph':ephn, 'eaddr':eaddr, 'estate':estate, 'ecity':ecity, 'ezip':ezip, 'egen':egen}

        # validation
        if len(ephn) <10 or len(ephn) > 10:
            error_message ='Check all your details'
            data={'error': error_message, 'values':value}
            return render(request, 'candireg.html', data)

        elif User.objects.filter(username=username).exists():
            error_message ='Email already exists please login to your account'
            data={'error': error_message, 'values':value}
            return render(request, 'candilogin.html', data)

        elif len(epasswd)<8 or len(epasswd)>16:
            error_message ='maintain the range of password'
            data={'error': error_message, 'values':value}
            return render(request, 'candireg.html', data)
        
        else:
            candet_db=Can_det(ename=ename, username=username, ephn=ephn, eaddr=eaddr, estate=estate, ecity=ecity, ezip=ezip, egen=egen)         # store data into database
            candet=User.objects.create_user(username=username, password=epasswd)  # create user
            candet.first_name=ename
            candet.email=username
            candet_db.save()
            candet.save()
            return render(request, 'candilogin.html')


# candidate login
def candilogin(request):
    if request.method=="POST":
        username = request.POST.get('username')
        epasswd=request.POST.get('epasswd')

        error_message = None
        loguser=authenticate(username=username, password=epasswd)          # user authentication
        if loguser is not None:
            login(request, loguser)
            log_can_det=Can_det.objects.filter(username=username)
            request.session['username'] = username
            return render(request, 'canprof.html', {'edet':log_can_det})
        else:
            error_message = "Incorrect credentials"
            return render(request,'candilogin.html', {'error': error_message})
    else:
        return render(request, 'candilogin.html') 


# candidate profile
@login_required
def canprof(request):
    log_can_det = Can_det.objects.filter(username=request.session['username']) 
    return render(request, 'canprof.html', {'edet': log_can_det})


# company registration
def compreg(request):
    if request.method == 'GET':
        return render(request, 'compreg.html')
    else:
        cname=request.POST['cname']
        cemail=request.POST['cemail']
        cpasswd=request.POST['cpasswd']
        cphn=request.POST['cphn']
        caddr=request.POST['caddr']
        cstate=request.POST['cstate']
        ccity=request.POST['ccity']
        czip=request.POST['czip']

        error_message = None 

        # form after error
        value={'cname': cname, 'cemail': cemail, 'cph':cphn, 'caddr':caddr, 'cstate':cstate, 'ccity':ccity, 'czip':czip}

        # validation
        if len(cphn) <10 or len(cphn) > 10:
            error_message ='Check all your details'
            data={'error': error_message, 'value':value}
            return render(request, 'compreg.html', data)
        elif User.objects.filter(username=cemail).exists():
            error_message ='Email already exists please login to your account'
            data={'error': error_message, 'values':value}
            return render(request, 'complogin.html', data)
        elif len(cpasswd)<8 or len(cpasswd)>16:
            error_message ='maintain the range of password'
            data={'error': error_message, 'values':value}
            return render(request, 'candireg.html', data)
        else:
            comdet_db=Com_det(cname=cname, cemail=cemail, cphn=cphn, caddr=caddr, cstate=cstate, ccity=ccity, czip=czip)
            comdet=User.objects.create_user(username=cemail, password=cpasswd)
            comdet.first_name=cname
            comdet.email=cemail
            comdet_db.save()
            comdet.save()
            return render(request, 'complogin.html')

    
# company login
def complogin(request):
    if request.method=="POST":
        cemail = request.POST.get('cemail')
        cpasswd=request.POST.get('cpasswd')

        error_message = None

        loguser=authenticate(username=cemail, password=cpasswd)
        if loguser is not None:
            login(request, loguser)
            log_com_det=Com_det.objects.filter(cemail=cemail)      # where clause

            request.session['cemail'] = cemail               # session management

            return render(request, 'compprof.html', {'cdet':log_com_det})
        else:
            error_message = "Incorrect credentials"
            return render(request,'complogin.html', {'error': error_message})
    else:
        return render(request, 'complogin.html') 


# company profile
@login_required
def compprof(request):
    log_com_det = Com_det.objects.filter(cemail=request.session['cemail'])
    return render(request, 'compprof.html', {'cdet': log_com_det})


# password updated template
def fgtpasswd_done(request):
    return render(request, 'fgtpasswd_done.html')


# get resume data
@login_required
def resumeform(request):
    if request.method == 'GET':
        return render(request, 'resumeform.html')
    else:
        username = request.POST['username']
        git=request.POST['git']
        lkdn=request.POST['lkdn']
        summary=request.POST['summary']
        iedu=request.POST['iedu']
        dedu=request.POST['dedu']
        pedu=request.POST['pedu']
        sedu=request.POST['sedu']
        workexp=request.POST['workexp']
        skill1=request.POST['skill1']
        skill2=request.POST['skill2']
        skill3=request.POST['skill3']
        skill4=request.POST['skill4']
        skill5=request.POST['skill5']
        skill6=request.POST['skill6']
        skill7=request.POST['skill7']
        skill8=request.POST['skill8']
        skill9=request.POST['skill9']
        skill10=request.POST['skill10']
        pexp=request.POST['pexp']
        achv=request.POST['achv']
        hby1=request.POST['hby1']
        hby2=request.POST['hby2']
        hby3=request.POST['hby3']
        hby4=request.POST['hby4']
        hby5=request.POST['hby5']
        hby6=request.POST['hby6']
        hby7=request.POST['hby7']
        hby8=request.POST['hby8']
        hby9=request.POST['hby9']
        hby10=request.POST['hby10']

        error_message_res = None

        value = {'username':username, 'git':git, 'lkdn':lkdn, 'summary':summary, 'iedu':iedu, 'dedu':dedu, 'pedu':pedu, 'sedu':sedu, 'workexp':workexp, 'skill1':skill1, 'skill2':skill2, 'skill3':skill3, 'skill4':skill4, 'skill5':skill5, 'skill6':skill6, 'skill7':skill7, 'skill8':skill8, 'skill9':skill9, 'skill10':skill10, 'pexp':pexp, 'achv':achv, 'hby1':hby1, 'hby2':hby2, 'hby3':hby3, 'hby4':hby4, 'hby5':hby5, 'hby6':hby6, 'hby7':hby7, 'hby8':hby8, 'hby9':hby9, 'hby10':hby10}

        if Resume.objects.filter(username=username).exists():
            error_message_res="Email already exists. Please edit your existing resume"
            data_res = {'error': error_message_res, 'value': value}
            return render(request, 'resumeform.html', data_res)
        if len(summary)>500:
            error_message_res="EmMAximum 500 words are allowed for summary"
            data_res = {'error': error_message_res, 'value': value}
            return render(request, 'resumeform.html', data_res)
        else:
            resume=Resume(username=username, git=git, lkdn=lkdn, summary=summary, iedu=iedu, dedu=dedu, pedu=pedu, sedu=sedu, workexp=workexp, skill1=skill1, skill2=skill2, skill3=skill3, skill4=skill4, skill5=skill5, skill6=skill6, skill7=skill7, skill8=skill8, skill9=skill9, skill10=skill10, pexp=pexp, achv=achv, hby1=hby1, hby2=hby2, hby3=hby3, hby4=hby4, hby5=hby5, hby6=hby6, hby7=hby7, hby8=hby8, hby9=hby9, hby10=hby10)
            resume.save()
        
        emp_det=Can_det.objects.filter(username=username)
        user_det=Resume.objects.filter(username=username)
        request.session['username'] = username
        res_data={'emp_det':emp_det, 'user_det':user_det}
        return render(request, 'resumetem.html', res_data)


# resume template
@login_required
def resumetem(request):
    emp_det=Can_det.objects.filter(username = request.session['username'])
    user_det=Resume.objects.filter(username = request.session['username'])
    res_data={'emp_det':emp_det, 'user_det':user_det}
    return render(request, 'resumetem.html', res_data)


# download template into pdf format
@login_required
def getpdf(request):
    template_path = "getpdf.html"  # to get the html page in pdf format
    emp_det = Can_det.objects.filter(username = request.session['username'])
    user_det = Resume.objects.filter(username = request.session['username'])
    res_data = {'emp_det':emp_det, 'user_det':user_det}

    response = HttpResponse(content_type='application/pdf')   # it gives the page in pdf format

    # give default filename / attachment specifies that the page is to be downloaded
    response['Content-Disposition'] = 'attachment; filename = "resume.pdf"'  

    # fetch template to be converted using get_template()
    template = get_template(template_path)

    # pass the data to be displayed int the pdf
    html = template.render(res_data)

    # method to create pdf
    pisa_status = pisa.CreatePDF(html, dest = response)
    if pisa_status.err:
        return HttpResponse("Error generating pdf")
    else:
        return response


# get job data
@login_required
def jobdet(request):
    if request.method == 'GET':
        return render(request, 'jobdet.html')
    else:
        jobpost = request.POST.get('jobpost')
        cemail = request.POST.get('cemail')
        cname = request.POST.get('cname')
        jobdes = request.POST.get('jobdes')
        indexp = request.POST.get('indexp')
        workdays = request.POST.get('workdays')
        jskill1 = request.POST.get('jskill1')
        jskill2 = request.POST.get('jskill2')
        jskill3 =request.POST.get('jskill3')
        jskill4 = request.POST.get('jskill4')
        jskill5 = request.POST.get('jskill5')
        jskill6 = request.POST.get('jskill6')
        jskill7 = request.POST.get('jskill7')
        jskill8 = request.POST.get('jskill8')
        jskill9 = request.POST.get('jskill9')
        jskill10 = request.POST.get('jskill10')
        salary = request.POST.get('salary')
        location=request.POST.get('location')

        error_message = None

        value = {'jobpost': jobpost, 'cemail': cemail, 'cname': cname, 'jobdes':jobdes, 'indexp':indexp, 'jskill1':jskill1, 'jskill2':jskill2, 'jskill3':jskill3, 'jskill4':jskill4, 'jskill5':jskill5, 'jskill6':jskill6, 'jskill7':jskill7, 'jskill8':jskill8, 'jskill9':jskill9, 'jskill10':jskill10, 'salary':salary, 'location':location}

        if User.objects.filter(username=cemail).exists() is None:
            error_message = "Enter your company email"
            job_data = {'value':value, 'error': error_message}
            return render(request, 'jobdet.html', job_data)
        else:
            jobdet = Job_det(jobpost=jobpost, cemail=cemail, cname=cname, jobdes=jobdes, indexp=indexp, workdays=workdays, jskill1=jskill1, jskill2=jskill2, jskill3=jskill3, jskill4=jskill4, jskill5=jskill5, jskill6=jskill6, jskill7=jskill7, jskill8=jskill8, jskill9=jskill9, jskill10=jskill10, salary=salary, location=location)
            jobdet.save()

        request.session['cemail'] = cemail
        jobposting = Job_det.objects.filter(cemail=request.session['cemail'])

        return render(request, 'compjobs.html', {'jobs':jobposting})


# display jobs posted by the company
@login_required
def compjobs(request):
    jobposting = Job_det.objects.filter(cemail=request.session['cemail'])
    return render(request, 'compjobs.html', {'jobs':jobposting})


# display all the applications received by the company from candidates
@login_required
def compapp(request):
    if request.method == 'GET':
        applied = Apply_job.objects.filter(cemail=request.session['cemail'])
        return render(request, 'compapp.html', {'applied': applied})


# job search page
@login_required
def jobsearch(request):
    jobs = Job_det.objects.all()
    if request.method == 'POST':
        return render(request, 'jobsearch.html', {'jobs': jobs})
    else:
        post = request.GET.get('jobpost')  # search job functionality
        if post != None:
            jobs = Job_det.objects.filter(jobpost=post)
            return render(request, 'jobsearch.html', {'jobs': jobs})
        else:
            jobs = Job_det.objects.all()
            return render(request, 'jobsearch.html', {'jobs': jobs})


# apply jobs
@login_required
def apply(request):
    if request.method == 'GET':
        jobposting = Com_det.objects.all()
        return render(request, 'apply.html', {'jobs': jobposting})
    else:
        job_id = request.GET.get('jobid')   # storing foreignkey fetched from the html template
        ename = request.POST.get('ename')
        ephn = request.POST.get('ephn')
        username = request.POST.get('username')
        reason = request.POST.get('reason')
        cemail = request.POST.get('cemail')
        upload = request.FILES.get('upload')

        applied = Apply_job(job_id=job_id, ename=ename, ephn = ephn, username=username, reason=reason, cemail=cemail, upload=upload)
        applied.save()

        request.session['username'] = username
        applied_show = Apply_job.objects.filter(username = request.session['username'])
        return render(request, 'candapp.html', {'applied': applied_show})

def select(request):
    if request.method == 'GET':
        return render(request, 'select.html')
    else:
        candidate_id = request.GET.get('jobappid')
        selected = request.POST.get('decision')
        doi = request.POST.get('doi')
        toi = request.POST.get('toi')
        aoi = request.POST.get('aoi')
        loi = request.POST.get('loi')
        cemail = request.POST.get('cemail')
        decision = Decision(candidate_id=candidate_id, selected=selected, doi=doi, toi=toi, aoi=aoi, loi=loi, cemail=cemail)
        decision.save()

        job = Job_det.objects.get(jobid = candidate_id)
        jobposition = job.jobpost
        jobcompany = job.cname
        print(jobposition, jobcompany)
        # send email notification
        
        s1 = "Reply to your application at "
        s2 = jobposition
        s3 = jobcompany
        subject = s1 + s2 + ', ' + s3
        recipient = 'anaghakamat03@gmail.com'
        m1 = 'You are selected for further interviews. Your interview is scheduled at '
        m2 = doi
        m3 = toi
        m4 = '. It is our humble request to be present on time.'
        m5 = ''
        if aoi:
            m51 = 'For your interview you must be present at '
            m52 = aoi
            m53 = ' on time'
            m5 = m51 + m52 + m53
        elif loi:
            m51 = 'For your interview you join the link '
            m52 = loi
            m53 = ' on time. '
            m5 = m51 + m52 + m53
        else:
            pass

        m6 = 'For further queries please contact at '
        success = m1 + m2 + m3 + m4 + m5 + m6 + cemail
        f1 = 'Sorry, you are not selected for further interviews. '
        failure = f1 + m6 + cemail

        if candidate_id:
            message = 'decision already given'
            decide = Decision.objects.filter(cemail=request.session['cemail'])
            return render(request, 'selected.html', {'message':message, 'decide':decide})
        else:
            if selected == '0':
                send_mail(subject, failure, EMAIL_HOST_USER, [recipient], fail_silently=False)
            else:
                send_mail(subject, success, EMAIL_HOST_USER, [recipient], fail_silently=False)
        
        
        request.session['cemail'] = cemail
        
        return redirect('selected')

def selected(request):
        decide = Decision.objects.filter(cemail=request.session['cemail'])
        return render(request, 'selected.html', {'decide': decide})

# candidate logout
@login_required
def can_logout(request):
    logout(request)
    return redirect('candilogin')

# quiz category
# @login_required
# def quizcat(request):
#     if request.method == 'POST':
#         category_name = request.POST.get('category_name')
#         store = Quiz_category(category_name=category_name)
#         store.save()
#     else:
#         categories = Quiz_category.objects.all()
#         return render(request, 'quizcat.html', {'categories':categories})

# def quiz(request):
#     return render(request, 'quiz.html')

# company logout
@login_required
def comp_logout(request):
    logout(request)
    return redirect('complogin')


# applications made by candidate
@login_required
def candapp(request):
    applied = Apply_job.objects.filter(username = request.session['username'])
    return render(request, 'candapp.html', {'applied': applied})


# update candidate details
@login_required
def canprof_update(request):
    context = {}
    if request.method == 'GET':
        can_upd=Can_det.objects.filter(username = request.session['username'])
        return render(request, 'canprof_update.html', {'edet': can_upd})
    else:
        ename = request.POST['ename']
        ephn=request.POST['ephn']
        edob=request.POST['edob']
        eaddr=request.POST['eaddr']
        ecity=request.POST['ecity']
        estate=request.POST['estate']
        ezip=request.POST['ezip']
        egen=request.POST['egen']


        user = User.objects.get(username= request.session['username'])
        user.first_name = ename
        user.save()

        user_db = Can_det.objects.get(username = request.session['username'])
        user_db.ename = ename
        user_db.ephn = ephn
        user_db.edob = edob
        user_db.eaddr = eaddr
        user_db.ecity = ecity
        user_db.estate = estate
        user_db.ezip = ezip
        user_db.egen = egen
        user_db.save()

        context["status"] = "Profile successfully updated"

        return render(request, 'canprof_update.html', context)


# update company details
@login_required
def compprof_update(request):
    context = {}
    if request.method == "GET":
        comp_upd = Com_det.objects.filter(cemail=request.session['cemail'])
        return render(request, 'compprof_update.html', {'cdet': comp_upd})
    else:
        cname = request.POST['cname']
        cphn = request.POST['cphn']
        caddr = request.POST['caddr']
        ccity=request.POST['ccity']
        cstate=request.POST['cstate']
        czip = request.POST['czip']

        cuser = User.objects.get(username=request.session['cemail'])
        cuser.first_name = cname
        cuser.save()

        cuser_db = Com_det.objects.get(cemail=request.session['cemail'])
        cuser_db.cname = cname
        cuser_db.cphn = cphn
        cuser_db.caddr = caddr
        cuser_db.ccity = ccity
        cuser_db.cstate = cstate
        cuser_db.czip = czip
        cuser_db.save()

        context["status"] = "Profile updated successfully"
        return render(request, "compprof_update.html", context)


# update resume details
@login_required
def resumeform_update(request):
    context = {}
    if request.method == 'GET':
        user_det=Resume.objects.filter(username = request.session['username'])
        return render(request, 'resumeform_update.html', {'user_det':user_det})
    else:
        git=request.POST['git']
        lkdn=request.POST['lkdn']
        summary=request.POST['summary']
        iedu=request.POST['iedu']
        dedu=request.POST['dedu']
        pedu=request.POST['pedu']
        sedu=request.POST['sedu']
        workexp=request.POST['workexp']
        skill1=request.POST['skill1']
        skill2=request.POST['skill2']
        skill3=request.POST['skill3']
        skill4=request.POST['skill4']
        skill5=request.POST['skill5']
        skill6=request.POST['skill6']
        skill7=request.POST['skill7']
        skill8=request.POST['skill8']
        skill9=request.POST['skill9']
        skill10=request.POST['skill10']
        pexp=request.POST['pexp']
        achv=request.POST['achv']
        hby1=request.POST['hby1']
        hby2=request.POST['hby2']
        hby3=request.POST['hby3']
        hby4=request.POST['hby4']
        hby5=request.POST['hby5']
        hby6=request.POST['hby6']
        hby7=request.POST['hby7']
        hby8=request.POST['hby8']
        hby9=request.POST['hby9']
        hby10=request.POST['hby10']

        resup = Resume.objects.get(username = request.session['username'])
        resup.git = git
        resup.lkdn = lkdn
        resup.summary = summary
        resup.iedu = iedu
        resup.dedu = dedu
        resup.pedu = pedu
        resup.sedu = sedu
        resup.workexp = workexp
        resup.skill1 = skill1
        resup.skill2 = skill2
        resup.skill3 = skill3
        resup.skill4 = skill4
        resup.skill5 = skill5
        resup.skill6 = skill6
        resup.skill7 = skill7
        resup.skill8 = skill8
        resup.skill9 = skill9
        resup.skill10 = skill10
        resup.pexp = pexp
        resup.achv = achv
        resup.hby1 = hby1
        resup.hby2 = hby2
        resup.hby3 = hby3
        resup.hby4 = hby4
        resup.hby5 = hby5
        resup.hby6 = hby6
        resup.hby7 = hby7
        resup.hby8 = hby8
        resup.hby9 = hby9
        resup.hby10 = hby10
        resup.save()

        context["status"] = "Resume successfully updated"
        return render(request, 'resumeform_update.html', context)


# delete candidate 
@login_required
def canprof_delete(request):
    if request.method == 'POST':
        candel = User.objects.get(username = request.session['username'])
        candel_db = Can_det.objects.get(username = request.session['username'])
        candel_resume = Resume.objects.get(username = request.session['username'])
        candel_jobs = Job_det.objects.get(username = request.session['username'])
        candel.delete()
        candel_db.delete()
        candel_resume.delete()
        candel_jobs.delete()
        return render(request, 'candireg.html')


# delete company 
@login_required
def compprof_delete(request):
    if request.method == 'POST':
        comdel = User.objects.get(cemail=request.session['cemail'])
        comdel_db = Com_det.objects.get(cemail= request.session['cemail'])
        comdel.delete()
        comdel_db.delete()
        return render(request, 'compreg.html')


# delete resume
@login_required
def resume_delete(request):
    if request.method == "POST":
        resdel = Resume.objects.get(username=request.session['username'])
        resdel.delete()
        return render(request, 'canprof.html')


