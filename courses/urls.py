from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path("/about", views.about, name="abouts"),

    # Auth
    path('about/',views.about,name='about'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # path('about/', views.about_view, name='about'),


    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
    path('course/<int:course_id>/quiz/', views.attempt_quiz, name='attempt_quiz'),
    path('enroll/<int:course_id>/', views.enroll, name='enroll'),
    path('unenroll/<int:course_id>/', views.unenroll, name='unenroll'),
    path('course/<int:course_id>/quiz/', views.attempt_quiz, name='attempt_quiz'),
]
