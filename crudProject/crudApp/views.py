import django
from django.shortcuts import redirect, render
from .forms import StudentForm
from .models import StudentData
# from django.messages import messages

# Create your views here.




def form(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/display/')
            except:
                pass
    else:
        form = StudentForm()
    return render(request,"form.html",{'form':form})
    




def display(request):
    student = StudentData.objects.all() 
    return render(request,'display.html',{'student':student})


def edit(request, id):
    student_edit = StudentData.objects.get(id=id)
    return render(request, 'edit.html',{'student_edit': student_edit})
    


def update(request, id):
    student_update = StudentData.objects.get(id=id)
    form = StudentForm(request.POST, instance=student_update)
    if form.is_valid():
        form.save()
        return redirect('display')
    return render(request, 'edit.html', {'student_update':student_update})


def delete(request, id):
    student_delete = StudentData.objects.get(id=id)
    student_delete.delete()
    return redirect('display')