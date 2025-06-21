from django.db import models

# Step 1
# Defining our database schema here using Django Models
# Each model = one table in the database
# Each field = one column in the table
class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

# For step 2, go to admin.py file to register model
