from django.shortcuts import render, redirect
from app_crudoper.models import Student
from app_crudoper.forms import ImageUploadForm
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def show(request):
    students = Student.objects.all()
    return render(request, 'show.html', {'students': students})


@login_required(login_url='/login/')
def view(request, id):
    student = Student.objects.get(Student_ID=id)
    return render(request, 'view.html', {'student': student})


def update(request, id, user):
    student = Student.objects.get(Student_ID=id)
    user = User.objects.get(username=user)
    if request.method == 'POST':
        name = request.POST['name']
        student_id = request.POST['id']
        email = request.POST['email']
        user_name = request.POST['username']
        passwordd = request.POST['password']
        school = request.POST['school']
        program = request.POST['program']
        batch = request.POST['batch']

        student.Name = name
        student.Student_ID = student_id
        student.Email = email
        student.Username = user_name
        student.password = passwordd
        student.School = school
        student.Program = program
        student.Batch = batch
        student.save()
        user.username = user_name
        user.set_password(passwordd)
        user.save()
        return redirect('/show')

    return render(request, 'update.html', {'student': student})


def image_update(request, id):
    student = Student.objects.get(Student_ID=id)
    photo_upload_form = ImageUploadForm(request.POST, request.FILES)
    if request.method == 'POST':
        avatar = student.Image
        if photo_upload_form.is_valid():
            avatar = photo_upload_form.cleaned_data['profile_photo']
        # image = request.POST['image']
        name = request.POST['name']
        student_id = request.POST['id']
        email = request.POST['email']
        school = request.POST['school']
        program = request.POST['program']
        batch = request.POST['batch']
        # form = StudentForm(request.POST, instance=student)
        student.Image = avatar
        student.Name = name
        student.Student_ID = student_id
        student.Email = email
        student.School = school
        student.Program = program
        student.Batch = batch
        student.save()
        return redirect('/show')

    return render(request, 'image_update.html', {'student': student, 'form': photo_upload_form})


def destro(request, id, username):
    student = Student.objects.get(Student_ID=id)
    student.delete()
    user = User.objects.get(username=username)
    user.delete()
    return redirect('/show')


def register(request):
    photo_upload_form = ImageUploadForm(request.POST, request.FILES)
    if request.method == 'POST':
        name = request.POST['name']
        student_id = request.POST['student_id']
        school = request.POST['school']
        program = request.POST['program']
        batch = request.POST['batch']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken....')
                return redirect('/register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already taken....')
                return redirect('/register')
            else:
                user = User.objects.create_user(username=username, password=password1,
                                                email=email)
                user.save()
                avatar = None
                if photo_upload_form.is_valid():
                    avatar = photo_upload_form.cleaned_data['profile_photo']
                student = Student.objects.create(Name=name, Image=avatar, Student_ID=student_id,
                                                 Username=username, password=password1,
                                                 Email=email, School=school,
                                                 Batch=batch, Program=program)
                student.save()

                messages.info(request, 'User created...')
                return redirect('/login')
        else:
            messages.info(request, 'Password not matching...')
            return redirect('/register')
    return render(request, 'register.html', {'form': photo_upload_form})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username.find(".com") > 0:
            user = auth.authenticate(request, email=username, password=password)
            if user:
                auth.login(request, user)
                return redirect('/show')
            else:
                messages.info(request, 'Invalid credentials.. email')
                return redirect('/login')
        else:
            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('/show')
            else:
                messages.info(request, 'Invalid credentials.. User')
                return redirect('/login')

    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/login')
