from django.db import models
from django.conf import settings
from django.utils.text import slugify

class RevportalUserProfile(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = 'profile')
    is_teacher = models.BooleanField(verbose_name = 'Teacher?', default = False)


class RevportalTeacherProfile(models.Model):

    profile = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = 'teacher')
    display_name = models.CharField(verbose_name = 'Display Name', null = True, max_length = 30)
    description = models.CharField(
        verbose_name = 'About Me', 
        max_length = 90, 
        default = 'You can change this text and make it something personal for other public users to see'
    )
    profile_pic = models.ImageField(
        upload_to = 'user_profile_pics/',
        default = 'user_profile_pics/default-avatar.jpg'
    )
    is_teacher = models.BooleanField(verbose_name = 'Teacher', default = False)
    subjects = models.ManyToManyField('RevportalSubjects', blank = True)


    class Meta:
        verbose_name = 'Revportal Profile'
        verbose_name_plural = 'Revportal Profiles'
    

class RevportalStudentProfile(models.Model):

    profile = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = 'student')



class RevportalSubjects(models.Model):

    subject_id = models.IntegerField(verbose_name = 'Subject ID', unique = True, primary_key = True)
    name = models.CharField(max_length = 50)
    slug = models.SlugField()
    description = models.TextField(max_length = 2000)
    image = models.ImageField(upload_to = 'subject_images/', null = True)

    class Meta:
        verbose_name = 'Revportal Subject'
        verbose_name_plural = 'Revportal Subjects'

    def __str__(self): 
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)









