from django.db import models

# Create your models here.

class ProductContact(models.Model):
    full_name=models.CharField(max_length=150,verbose_name='نام و نام خانوادگی')
    email=models.EmailField(max_length=100,verbose_name='ایمیل')
    subject=models.CharField(max_length=200,verbose_name='عنوان')
    text=models.TextField(verbose_name='متن پیام')
    is_read=models.BooleanField(default=False,verbose_name='خوانده شده/ نشده')

    def __str__(self):
        return self.subject
    
    class Meta:
        verbose_name='تماس با ما'
        verbose_name_plural='تماس های کاربران'