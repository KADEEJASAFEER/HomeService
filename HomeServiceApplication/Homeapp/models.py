from django.db import models

# Create your models here.

class skill(models.Model):
    skillname=models.CharField(max_length=100)

    def __str__(self):
        return self.skillname


class addSkill(models.Model):
    skill=models.ForeignKey(skill,on_delete=models.CASCADE)
    user=models.CharField(max_length=120)

class addWork(models.Model):
    workname=models.ForeignKey(skill,on_delete=models.CASCADE)
    estimatedamount=models.IntegerField()
    location=models.CharField(max_length=120)
    user=models.CharField(max_length=120)
    choice=(
        ('notassigned','notassigned'),
        ('assigned','assigned'),
        ('completed','completed')
    )

    workstatus=models.CharField(max_length=50,choices=choice)

    def __str__(self):
        return self.workname