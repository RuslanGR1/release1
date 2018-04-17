from django.db import models


class Gmailt1(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.login

    def my_str(self):
        return '{}:{}\r\n'.format(self.login, self.password)


class Gmailt2(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.login

    def my_str(self):
        return '{}:{}\r\n'.format(self.login, self.password)


class Gmailt3(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.login

    def my_str(self):
        return '{}:{}\r\n'.format(self.login, self.password)
