from django.shortcuts import render, redirect
from .models import STUDENT
from .forms import StudentCreate
from django.http import HttpResponse

#DataFlair
def index(request):
    shelf = STUDENT.objects.all()
    return render(request, 'student/library.html', {'shelf': shelf})

def upload(request):
    upload = StudentCreate()
    if request.method == 'POST':
        upload = StudentCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'student/upload_form.html', {'upload_form':upload})

def update_student(request, student_id):
    student_id = int(student_id)
    try:
        student_sel = STUDENT.objects.get(id = student_id)
    except STUDENT.DoesNotExist:
        return redirect('index')
    student_form = StudentCreate(request.POST or None, instance = student_sel)
    if student_form.is_valid():
       student_form.save()
       return redirect('index')
    return render(request, 'student/upload_form.html', {'upload_form':student_form})

def delete_student(request, student_id):
    student_id = int(student_id)
    try:
        student_sel = STUDENT.objects.get(id = student_id)
    except STUDENT.DoesNotExist:
        return redirect('index')
    student_sel.delete()
    return redirect('index')