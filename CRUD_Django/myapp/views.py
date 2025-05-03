from django.shortcuts import render, redirect
from myapp.models import studentModel
# Create your views here.

def display_all(request):
    all_data = studentModel.objects.all()
    return render(request, 'html/display.html', {'data':all_data})



def add_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('pass')
        
        
     
        
        studentModel.objects.create(
            name = name,
            email = email,
            phone = int(phone),
            password = int(password)
        )
        
    return render(request, 'html/add.html')




def delete_view(request,id):
    spec_student = studentModel.objects.get(id=id)
    spec_student.delete()
    
    return redirect('dis')



def update_view(request,id):
    spec_student = studentModel.objects.get(id=id)
    if request.method == 'POST':
        spec_student.name = request.POST.get('name')
        spec_student.email = request.POST.get('email')
        spec_student.phone = request.POST.get('phone')
        spec_student.Password = request.POST.get('pass')
        spec_student.save()
        
        return redirect('dis')
    return render(request, 'html/update.html', {'data':spec_student} )