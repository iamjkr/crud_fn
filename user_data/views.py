from django.shortcuts import render, redirect
from .models import Employee


# Create your views here.
def index(request):
    emp_data = Employee.objects.all()
    return render(request, 'account/index.html', context={'emp': emp_data})


def addemployee(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp_data = Employee(
            name=name,
            email=email,
            address=address,
            phone=phone
        )
        emp_data.save()
        return redirect('homepage')

    return render(request, 'account/index.html')


def editEmployee(request):
    emp = Employee.objects.all()
    context = {
        'emp': emp
    }
    return render(request, 'account/index.html', context)


def updateEmployee(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp = Employee(
            id=id,
            name=name,
            email=email,
            address=address,
            phone=phone
        )
        emp.save()

    return redirect('homepage')


def deleteEmployee(request, id):
    # Filter and get both retun same
    ds = Employee.objects.get(id=id)
    # ds = Employee.objects.filter(id=id)
    print(ds)
    ds.delete()
    return redirect('homepage')


from django.shortcuts import render

# Create your views here.
