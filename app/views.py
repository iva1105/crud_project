from django.shortcuts import render, redirect
from .models import Student

# Create your views here.

def index(request):
    data=Student.objects.all()
    contex= {"data":data }


    return render(request, 'index.html',contex)



def insertData(request):
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        query = Student(name=name, email=email, age=age, gender=gender)
        query.save()
        return redirect('/')
                                
    return render(request, 'index.html', )

def updateData(request, id):
     
     if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')

        edit=Student.objects.get(id=id)
        edit.name = name
        edit.email = email
        edit.age = age
        edit.gender = gender
        edit.save()
        return redirect('/')
        
     d=Student.objects.get(id=id)
     contex= {"d":d}

     return render(request, 'edit.html',contex)

def deleteData(request, id):
    d=Student.objects.get(id=id)
    d.delete()

    return redirect("/")



def about (request):
    return render(request, 'about.html')


 