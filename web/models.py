from django.db import models


INTEREST = (
    ("1","STARTER"),
    ("2","MEDIUM"),
    ("3","COMPLETE"),
)

class Team(models.Model):
    image = models.FileField(upload_to="team/images/")
    name = models.CharField(max_length=255)
    job_role= models.CharField  (max_length=255)

    class Meta:
        db_table ="web_team"
        ordering=["id"]

    def __str__(self):
        return self.name

class Customer(models.Model):
    image = models.FileField(upload_to="customer/images/")

    class Meta:
        db_table ="web_customers"
        ordering=["id"]
    
    def __str__(self):
        return str(self.image)

class Contact(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=128)
    number = models.CharField(max_length=128)
    interest = models.CharField(max_length=128, choices=INTEREST)
    user_agreement = models.BooleanField(default=False)

    class Meta:
        db_table ="web_contact"
        ordering = ["id"]

    def __str__(self):
        return self.name