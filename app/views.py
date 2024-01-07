from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
from django.db.models.functions import Length
from django.db.models import Q

# Create your views here.
def Display_Dept(request):
    QuerySet_List_Dept_Object=Dept.objects.all()
    QuerySet_List_Dept_Object=Dept.objects.all().order_by('DName')
    QuerySet_List_Dept_Object=Dept.objects.all().order_by('-DName')
    QuerySet_List_Dept_Object=Dept.objects.all().order_by(Length('DName'))
    QuerySet_List_Dept_Object=Dept.objects.exclude()   
    d={'dept':QuerySet_List_Dept_Object}
    return render(request,'Display_Dept.html',d)
    

def Display_Emp(request):
    QuerySet_List_Emp_Object=Emp.objects.all()
    QuerySet_List_Emp_Object=Emp.objects.all().order_by('EName')
    QuerySet_List_Emp_Object=Emp.objects.all().order_by(Length('Job'))
    QuerySet_List_Emp_Object=Emp.objects.filter(EName__startswith='A')
    QuerySet_List_Emp_Object=Emp.objects.filter(EName__endswith='N')
    QuerySet_List_Emp_Object=Emp.objects.filter(EName__contains='A')
    QuerySet_List_Emp_Object=Emp.objects.filter(Hiredate__gt='1981-01-21')
    QuerySet_List_Emp_Object=Emp.objects.filter(Hiredate__gte='1981-01-21')
    QuerySet_List_Emp_Object=Emp.objects.filter(Hiredate__lt='1981-01-21')
    QuerySet_List_Emp_Object=Emp.objects.filter(Hiredate__lte='1981-01-21')
    QuerySet_List_Emp_Object=Emp.objects.filter(Hiredate__year__gt='1981')
    QuerySet_List_Emp_Object=Emp.objects.filter(Hiredate__year='1981')
    QuerySet_List_Emp_Object=Emp.objects.filter(Hiredate__day='19')
    QuerySet_List_Emp_Object=Emp.objects.all()
    QuerySet_List_Emp_Object=Emp.objects.filter(EName__endswith='n', Job='Salesman')
    QuerySet_List_Emp_Object=Emp.objects.filter(Q(EName__endswith='n') | Q(Job='Salesman'))
    QuerySet_List_Emp_Object=Emp.objects.filter(Q(EName__endswith='n') & Q(Job='Salesman'))
    d={'emp':QuerySet_List_Emp_Object}
    return render(request,'Display_Emp.html',d)


def insert_dept(request):
    DN=input('Enter DeptNo')
    Dn=input('Enter DName')
    L=input('Enter Loc')
    DO=Dept.objects.get_or_create(DeptNo=DN,DName=Dn,Loc=L)[0]
    DO.save()
    return HttpResponse('Data inserted Sucessfully')

def insert_emp(request):
    ENo=input('Enter EmpNo')
    En=input('Enter emp name')
    J=input('Enter job')
    M=input('Enter mgrno')
    HD=input('Enter hiredate')
    S=input('Enter Sal')
    C=input('Enter comm')
    dn=input('Enter deptno')
    DO=Dept.objects.get(DeptNo=50)
    EO=Emp.objects.get_or_create(EmpNo=ENo,EName=En,Job=J,Mgr=M,Hiredate=HD,Sal=S,Commision=C,DeptNo=DO)[0]
    EO.save()
    return HttpResponse('Data inserted Sucessfully')

