from django.contrib import admin
from django.urls import path
from . import views,teacherviews
from django.conf import settings
from django.conf.urls.static import static





admin.site.site_header="Amir developer"
admin.site.site_title="Welcome to dashboard"
admin.site.index_title="Welcome to this Portal"

app_name="myapp"
urlpatterns = [
   path('',views.contact),
   path('showmyForm/',views.showmyForm,name='showmyForm'),
   path('amir/',views.amir,name='amir'),
   path('Signup', views.handleSignup,name='handleSignup'),
   path('Login', views.handleLogin,name='handleLogin'),
   path('Logout', views.handleLogout,name='handleLogout'),
   path('myapp/myclassroom/', views.showclasses,name='showclasses'),
   path('detail/<int:id>/',views.detail,name='detail'),   
   path('addreview/<int:id>/',views.add_review,name='add_review'),
   path('editreview/<int:classroom_id>/<int:review_id>/',views.edit_review,name='edit_review'),
    path('deletereview/<int:classroom_id>/<int:review_id>/',views.delete_review,name='delete_review')


   

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)