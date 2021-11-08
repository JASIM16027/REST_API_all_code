from django.urls import path
from django.urls.resolvers import URLPattern 
from . import views

# urlpatterns = [
#     #path('studentapi/', views.StudentList.as_view()),
#     #path('studentapi/<int:pk>', views.StudentAPI.as_view()),
#     #path('studentapic/', views.StudentCreate.as_view()),
#     #path('studentapi/<int:pk>/', views.StudentRetrieve.as_view()),
#     #path('studentapi/<int:pk>', views.StudentUpdate.as_view()),
#     #path('studentapi/<int:pk>/', views.StudentDestroy.as_view()),
#     path('studentapi/',views.LCStudentAPI.as_view()),
#     path('studentapi/<int:pk>/',views.RUDStudentAPI.as_view())

# ]

urlpatterns = [
    path('studentapi/',views.StudentL.as_view()),
    #path('studentapi/',views.StudentC.as_view()),
    #path('studentapi/<int:pk>/',views.StudentU.as_view()),
    #path('studentapi/<int:pk>/',views.StudentR.as_view()),
    path('studentapi/<int:pk>/',views.StudentD.as_view())

]


# urlpatterns = [
#     path('studentapi/',views.StudentLC.as_view()),
#     path('studentapi/<int:pk>/',views.StudentRUD.as_view())
# ]
