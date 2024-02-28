from django.contrib import admin
from django.urls import path

from DjangoApplication import views

urlpatterns = [
    path('ZeroERR/',views.goZero,name='Zero'),
    path('admin/', admin.site.urls),
    path('',views.goHomePage,name='Form1'),
    path('CourseDescription/',views.goCourseTab,name='courseTable'),
    path('UserDetails/<int:user_ID>',views.errFunc,name='Err404'),
    path('statistics/',views.statistics,name='stat'),
    path('statistics1/',views.statistics1,name='stat1'),
    path('emailErr/',views.nameEmailErr,name='NameEmailError')
]
