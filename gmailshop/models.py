from django.db import models


class gmailt1(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.login

    def my_str(self):
        return '{}:{}\r\n'.format(self.login, self.password)


class gmailt2(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.login

    def my_str(self):
        return '{}:{}\r\n'.format(self.login, self.password)


class gmailt3(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.login

    def my_str(self):
        return '{}:{}\r\n'.format(self.login, self.password)
