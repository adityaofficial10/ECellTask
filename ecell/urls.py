from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.index,name = "index"),
    path('student/',views.student,name = "student"),
    path('startup/',views.startup,name = "startup"),
    path('thanks/',views.thanks,name = "thanks"),
    path('student/readytoanswer/',views.readytoanswer,name = "readytoanswer"),
    path('startup/question/role<int:pk>/appl<str:roll>/',views.question,name="question"),
    path('startup/current/',views.current,name="current"),
    path('startup/current/role_detail/role<int:pk>/',views.internshiprole_detail,name="role_detail"),
    path('startup/addQuestion/',views.addQuestion,name = "addQuestion"),
    path('startup/addQuestion/more/',views.more,name = "more"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
