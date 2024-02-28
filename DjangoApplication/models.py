from django.db import models

class TableCreation(models.Model):
    Name_COL = models.CharField(max_length=100)
    FathersName_COL = models.CharField(max_length=100)

    Gender_COL = models.CharField(max_length=20)

    Qualification_COL = models.CharField(max_length=100)
    Institution_COL = models.CharField(max_length=200)
    YearOfPassedOut_COL = models.IntegerField()

    EmailID_COL = models.CharField(max_length=50)
    MobileNumber_COL = models.BigIntegerField()

    OptedField_COL = models.CharField(max_length=200)
    OptedCourse_COL = models.CharField(max_length=200)

    ModeOfClass_COL = models.CharField(max_length=10)

    DateOfEntry_COL = models.CharField(max_length = 50)
