from django.shortcuts import render, get_object_or_404
from .models import Course, Video, Document, Question
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .forms import QuizForm
from django.db.models import Q

def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'courses/register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
        
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'courses/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def dashboard(request):
    enrolled_courses = request.user.enrolled_courses.all()
    return render(request, 'courses/dashboard.html', {
        'enrolled_courses': enrolled_courses
    })

@login_required
def enroll(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    course.students.add(request.user)
    print(course.students.all())
    enrolled_courses = request.user.enrolled_courses.all()
    print(enrolled_courses)
    return render(request, 'courses/dashboard.html', {
        'enrolled_courses': enrolled_courses
    })

@login_required
def unenroll(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    course.students.remove(request.user)
    enrolled_courses = request.user.enrolled_courses.all()
    return render(request, 'courses/dashboard.html', {
        'enrolled_courses': enrolled_courses
    })

def home(request):
    query = request.GET.get('q', '')
    if query:
        courses = Course.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
    else:
        courses = Course.objects.all()

    return render(request, 'courses/home.html', {'courses': courses, 'query': query,})

@login_required
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    videos = course.videos.all()
    documents = course.documents.all()
    questions = course.questions.all()
    is_enrolled = course.students.filter(id=request.user.id).exists()
    context = {
        'course': course,
        'videos': videos,
        'documents': documents,
        'questions': questions,
        'is_enrolled': is_enrolled
    }
    return render(request, 'courses/course_detail.html', context)

@login_required
def attempt_quiz(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    questions = course.questions.all()

    if request.method == "POST":
        form = QuizForm(questions, request.POST)
        if form.is_valid():
            score = 0
            for q in questions:
                user_answer = int(form.cleaned_data.get(f'question_{q.id}'))
                if user_answer == q.correct_option:
                    score += 1
            return render(request, 'courses/quiz_result.html', {
                'score': score,
                'total': questions.count(),
                'course': course
            })
    else:
        form = QuizForm(questions)

    return render(request, 'courses/attempt_quiz.html', {
        'form': form,
        'course': course
    })

def custom_404(request, exception=None):
    return render(request, '404.html', status=404)
