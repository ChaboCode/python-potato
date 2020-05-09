from django.db import models
from django.db.models import CASCADE


class Group(models.Model):
    name = models.CharField(max_length=16, default='')

    def __str__(self):
        return '{}'.format(self.name)


class Student(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    list = models.ForeignKey(
        Group,
        on_delete=CASCADE,
        default=None
    )

    def __str__(self):
        return '{} {}'.format(self.last_name, self.first_name)


class Teacher(models.Model):
    key = models.CharField(max_length=64)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)

    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)


class Subject(models.Model):
    name = models.CharField(max_length=20, default='')
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        default=None,
        related_name='subjects'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name='groups'
    )

    def __str__(self):
        return '{}'.format(self.name)


class GroupRegisters(models.Model):
    name = models.CharField(max_length=24)
    details = models.CharField(max_length=64)
    date = models.DateField()
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        default=None
    )
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        default=None
    )

    def __str__(self):
        return '{}'.format(self.name)
