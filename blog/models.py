from django.db import models

class AboutUs(models.Model):
    name = models.CharField(max_length=255)
    profession = models.CharField(max_length=299)
    email = models.EmailField()
    image = models.ImageField()
    insta = models.URLField(null=True, blank=True)
    whatsapp = models.URLField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta: 
        verbose_name = 'About Us'
        verbose_name_plural = 'About Us'

class Class(models.Model):
    class_name = models.CharField(max_length=255)
    trainer_name = models.ForeignKey(AboutUs, on_delete=models.CASCADE)
    class_image = models.ImageField()
    class_price = models.IntegerField()
    opisanie = models.TextField()

    def __str__(self) -> str:
        return self.class_name

    class Meta: 
        verbose_name = 'Class'
        verbose_name_plural = 'Classes'

class Schedules(models.Model):
    name = models.OneToOneField(Class, on_delete=models.CASCADE, unique=True)
    date = models.DateField()
    time_begining = models.TimeField()
    time_ending = models.TimeField()


    def __str__(self) -> str:
        return str(self.name)

    class Meta: 
        verbose_name = 'Schedules'
        verbose_name_plural = 'Schedules'

class Contact(models.Model):
    title = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self) -> str:
        return self.title

    class Meta: 
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'


class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name


    class Meta: 
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'