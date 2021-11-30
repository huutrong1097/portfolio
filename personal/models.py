from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from ckeditor.fields import RichTextField
# Create your models here.

class About(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False)
    date_of_birth = models.DateField(blank=False, null=False)
    avatar = models.ImageField(upload_to="image/", blank=False, null=False)
    address = models.CharField(max_length=200, blank=False, null=False)
    phone = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    position = models.CharField(max_length=100, blank=False, null=False)
    description = RichTextField(blank=False, null=False)
    cv = models.FileField(upload_to='file/', blank=False, null=False)
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    
    def __str__(self) -> str:
        return self.name

class Skill(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)
    year_of_experience = models.SmallIntegerField()

    def __str__(self) -> str:
        return self.title

class SubSkill(models.Model):
    title = models.ForeignKey(Skill, related_name='sub_skill', on_delete=models.CASCADE)
    skill = models.CharField(max_length=30, blank=False, null=False)
    percentage = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])
    
    class Meta:
        ordering = ['-percentage']

    def __str__(self) -> str:
        return self.skill


class Education(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    university = models.CharField(max_length=100, blank=False, null=False)
    date = models.DateField()

    def __str__(self) -> str:
        return self.title

class Company(models.Model):
    position = models.CharField(max_length=20, blank=False, null=False)
    name = models.CharField(max_length=50, blank=False, null=False)
    date = models.DateField()

    def __str__(self) -> str:
        return self.name

class Service(models.Model):
    title = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self) -> str:
        return self.title

class Experience(models.Model):
    title = models.ForeignKey(Service, related_name='services_exp', on_delete=models.CASCADE)
    description = models.CharField(max_length=200, blank=False, null=False)


class Project(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    slug = models.SlugField(max_length=200, blank=True, null=True)
    description = RichTextField(blank=False, null=False)
    image = models.ImageField(upload_to="projects/", blank=False, null=False)
    tools = models.CharField(max_length=200, blank=False, null=False)
    demo = models.URLField()
    github = models.URLField()
    show_in_slider = models.BooleanField(default=False)

class Contact(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField(null=False)
    company = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField()
    send_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


