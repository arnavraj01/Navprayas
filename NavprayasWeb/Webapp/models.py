from django.db import models


# Create your models here.
class Participant(models.Model):
    name = models.TextField();
    fathersName = models.TextField();
    mothersName = models.TextField();
    pClass = models.IntegerField();
    school = models.TextField();
    address = models.TextField();
    language = models.TextField();
    contact = models.IntegerField();
    registrationNo = models.TextField();
    dataOfBirth = models.DateField();

    def __unicode__(self):
        return u"%s" % self.name

    def __str__(self):
        return self.name
