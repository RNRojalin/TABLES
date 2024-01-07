from django.db import models

# Create your models here.
class Dept(models.Model):
    DeptNo=models.IntegerField(primary_key=True)
    DName=models.CharField(max_length=50)
    Loc=models.CharField(max_length=50)

    def __str__(self):
        return self.DName


class Emp(models.Model):
    EmpNo=models.IntegerField(primary_key=True)
    EName=models.CharField(max_length=30)
    Job=models.CharField(max_length=15)
    Mgr=models.IntegerField()
    Hiredate=models.DateField()
    Sal=models.PositiveIntegerField()
    Commision=models.IntegerField()
    DeptNo=models.ForeignKey(Dept,on_delete=models.CASCADE)

    def __str__(self):
        return self.EName



class Salgrade(models.Model):
    Grade=models.IntegerField()
    Losal=models.PositiveIntegerField()
    Hisal=models.PositiveIntegerField()

class Bonus(models.Model):
    Empno=models.ForeignKey(Emp,on_delete=models.CASCADE)
    Bamount=models.PositiveIntegerField()
