from .forms import EmployeeForm
from django.shortcuts import render,redirect
from .models import Employee
from django.views.decorators.http import require_http_methods
from django.utils.decorators import method_decorator
from django.http.response import HttpResponseRedirect, HttpResponse


# Create your views here.
def employee_list(request):
    context ={'employee_list':Employee.objects.all()}
    return render(request, "employee_collation/employee_list.html",context)

def employee_form(request, id=0):
    if request.method == "GET":
        if id==0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form =EmployeeForm(instance=employee)
        return render(request, "employee_collation/employee_form.html",{'form':form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance= employee)
        if form.is_valid():
            form.save()
    return redirect('/employee/list')
        
def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')
