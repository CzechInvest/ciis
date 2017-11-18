from django.db import models

# Create your models here.

class ContactPerson(models.Model):

    first_name = models.CharField(
            help_text="First name",
            max_length = 20)

    middle_name = models.CharField(
            help_text="Middle name",
            null=True,
            max_length = 20)


    last_name = models.CharField(
            help_text="Last name",
            max_length = 20)

    titles = models.CharField(
            help_text="Mgr., PhDr., MUDr., Ing., PhD., ...",
            null=True,
            max_length = 20)

    email = models.EmailField()

    phone = models.CharField(
            max_length=20)

    role = models.CharField(
            help_text="Director, HR Manager, ...",
            max_length=20)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

