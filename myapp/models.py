from xml.parsers.expat import model
from django.db import models
import uuid
from django.db.models.fields import UUIDField

# Create your models here.

# class BaseModel(models.Model):
#     id=models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
#     # when we don't want to display the class in table and only use as parent class use this
#     class Meta:
#         abstract=True

#candidate registration
class Can_det(models.Model):
    ename=models.CharField(max_length=50, default=None)
    username=models.EmailField(unique=True, primary_key=True)
    ephn=models.BigIntegerField()
    eaddr=models.CharField(max_length=200)
    ecity=models.CharField(max_length=50)
    estate=models.CharField(max_length=50)
    ezip=models.IntegerField()
    egen=models.CharField(max_length=20)

    @staticmethod
    def get_candet_by_email(username):
        try:
            return Can_det.objects.get(username=username)
        except:
            return False

    def isExists(self):
        if Can_det.objects.filter(username = self.username):
            return True
        else:
            return False

    class Meta:
        verbose_name_plural = "candidate_details"

#company registration
class Com_det(models.Model):
    cname=models.CharField(max_length=50)
    cemail=models.EmailField(unique=True, primary_key=True)
    cphn=models.BigIntegerField()
    caddr=models.CharField(max_length=200)
    ccity=models.CharField(max_length=50)
    cstate=models.CharField(max_length=50)
    czip=models.IntegerField()

    @staticmethod
    def get_comdet_by_email(cemail):
        try:
            return Com_det.objects.get(cemail=cemail)
        except:
            return False

    def isExists(self):
        if Com_det.objects.filter(cemail = self.cemail):
            return True
        else:
            return False
    
    class Meta:
        verbose_name_plural = "company_details"

#resume details
class Resume(models.Model):
    resid = models.AutoField(primary_key=True, editable=False, unique=True)
    git=models.URLField(max_length=200, default='', null=True, blank=True)
    lkdn=models.URLField(max_length=200, default='', null=True, blank=True)
    summary=models.CharField(max_length=500, default='')
    iedu=models.CharField(max_length=100, default='')
    dedu=models.CharField(max_length=100, default='')
    pedu=models.CharField(max_length=20, default='')
    sedu=models.CharField(max_length=20, default='')
    workexp=models.CharField(max_length=20, null=True, blank=True)
    skill1=models.CharField(max_length=50, null=True, default='', blank=True)
    skill2=models.CharField(max_length=50, null=True, default='', blank=True)
    skill3=models.CharField(max_length=50, null=True, default='', blank=True)
    skill4=models.CharField(max_length=50, null=True, default='', blank=True)
    skill5=models.CharField(max_length=50, null=True, default='', blank=True)
    skill6=models.CharField(max_length=50, null=True, default='', blank=True)
    skill7=models.CharField(max_length=50, null=True, default='', blank=True)
    skill8=models.CharField(max_length=50, null=True, default='', blank=True)
    skill9=models.CharField(max_length=50, null=True, default='', blank=True)
    skill10=models.CharField(max_length=50, null=True, default='', blank=True)
    pexp=models.URLField(max_length=200, null=True, blank=True)
    achv=models.URLField(max_length=200, null=True, blank=True)
    username=models.EmailField(max_length=50, unique=True)
    hby1=models.CharField(max_length=50, default='')
    hby2=models.CharField(max_length=50, default='')
    hby3=models.CharField(max_length=50, default='')
    hby4=models.CharField(max_length=50, default='')
    hby5=models.CharField(max_length=50, default='')
    hby6=models.CharField(max_length=50, default='')
    hby7=models.CharField(max_length=50, default='')
    hby8=models.CharField(max_length=50, default='')
    hby9=models.CharField(max_length=50, default='')
    hby10=models.CharField(max_length=50, default='')

    def isExist(self):
        if Resume.objects.filter(username = self.username):
            return True
        else:
            return False

class Job_det(models.Model):
    jobid = models.AutoField(primary_key=True, editable=False, unique=True)
    jobpost = models.CharField(max_length=100)
    cemail = models.EmailField(max_length=50)
    cname = models.CharField(max_length=50, default='')
    jobdes = models.CharField(max_length=900)
    indexp = models.CharField(max_length=50)
    workdays = models.CharField(max_length=50)
    jskill1 = models.CharField(max_length=50, null=True, default='', blank=True)
    jskill2 = models.CharField(max_length=50, null=True, default='', blank=True)
    jskill3 = models.CharField(max_length=50, null=True, default='', blank=True)
    jskill4 = models.CharField(max_length=50, null=True, default='', blank=True)
    jskill5 = models.CharField(max_length=50, null=True, default='', blank=True)
    jskill6 = models.CharField(max_length=50, null=True, default='', blank=True)
    jskill7 = models.CharField(max_length=50, null=True, default='', blank=True)
    jskill8 = models.CharField(max_length=50, null=True, default='', blank=True)
    jskill9 = models.CharField(max_length=50, null=True, default='', blank=True)
    jskill10 = models.CharField(max_length=50, null=True, default='', blank=True)
    salary = models.CharField(max_length=50, null=True, default='', blank=True)
    location = models.CharField(max_length=50)


    class Meta:
        verbose_name_plural="Job_Post_details"

class Apply_job(models.Model):
    jobappid = models.AutoField(primary_key=True, editable=False, unique=True)
    job = models.ForeignKey(Job_det, related_name="applications", on_delete=models.CASCADE)
    username = models.EmailField(max_length=50, default='')
    reason = models.CharField(max_length=900)
    ename = models.CharField(max_length=50, default='')
    ephn = models.BigIntegerField()
    cemail = models.EmailField(default='')
    upload = models.FileField(null=True, blank=True)

class Decision(models.Model):
    did = models.AutoField(primary_key=True, editable=False, unique=True)
    candidate = models.ForeignKey(Apply_job, on_delete=models.CASCADE, default='')
    selected = models.BooleanField(default=False)
    doi = models.CharField(max_length=20, null=True, blank=True)
    toi = models.CharField(max_length=20, null=True, blank=True)
    aoi = models.CharField(max_length=200, null=True, blank=True)
    loi = models.URLField(null=True, blank=True)
    cemail = models.EmailField(default='')