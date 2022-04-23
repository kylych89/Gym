from django.db import models

class User(models.Model):
    username = models.CharField(max_length=55)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    message = models.TextField()


    def str(self) -> str:
        return self.username


    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'




