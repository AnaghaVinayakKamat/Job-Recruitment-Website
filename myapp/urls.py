# added manually

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('candireg', views.candireg, name='candireg'),
    path('candilogin', views.candilogin, name='candilogin'),
    path('compreg', views.compreg, name='compreg'),
    path('complogin', views.complogin, name='complogin'),
    path('resumeform', views.resumeform, name='resumeform'),
    path('canprof', views.canprof, name='canprof'),
    path('compprof', views.compprof, name='compprof'),
    path('jobdet', views.jobdet, name='jobdet'),
    path('resumetem', views.resumetem, name='resumetem'),
    path('getpdf', views.getpdf, name='getpdf'),
    path('compapp', views.compapp, name='compapp'),
    path('select', views.select, name='select'),
    path('select/<int:jobid>', views.select, name='select'),
    path('selected', views.selected, name='selected'),
    path('jobsearch', views.jobsearch, name='jobsearch'),
    path('apply', views.apply, name='apply'),
    path('apply/<int:jobid>', views.apply, name='apply'),
    path('candapp', views.candapp, name='candapp'),
    path('compjobs', views.compjobs, name='compjobs'),
    path('canprof_update', views.canprof_update, name='canprof_update'),
    path('compprof_update', views.compprof_update, name='compprof_update'),
    path('resumeform_update', views.resumeform_update, name='resumeform_update'),
    path('canprof_delete', views.canprof_delete, name='canprof_delete'),
    path('compprof_delete', views.compprof_delete, name='compprof_delete'),
    path('resume_delete', views.resume_delete, name='resume_delete'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name="fgtpasswd_done.html"), name="password_reset_complete"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)