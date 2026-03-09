from django.db import models
from django.contrib.auth.models import User


# -------------------------------
# USER PROFILE MODEL
# (Teacher / Student)
# -------------------------------
class Profile(models.Model):

    ROLE_CHOICES = [
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES
    )

    def __str__(self):
        return self.user.username


# -------------------------------
# CATEGORY MODEL
# (Python, Java, AI, etc.)
# -------------------------------
class Category(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# -------------------------------
# RESOURCE MODEL
# (Uploaded Study Materials)
# -------------------------------
class Resource(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField()

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    file = models.FileField(upload_to='resources/')

    uploaded_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    downloads = models.IntegerField(default=0)

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title