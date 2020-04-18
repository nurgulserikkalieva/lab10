from django.db import models
import json
# Create your models here.

class Company(models.Model):
    name = models.CharField('name of the catgory', max_length=200)
    description = models.TextField('description of the company')
    city = models.CharField('city of the company', max_length=200)
    address = models.TextField('address of the company')
    def __str__(self):
        return  self.name

    def short(self):
        return {
            'name':self.name,
            'description': self.description,
            'city':self.city,
            'address':self.address,
        }

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

class Vacancy(models.Model):
    name = models.CharField('name of the vacancy', max_length = 200)
    description = models.TextField('description of the company')
    salary = models.FloatField('salary')
    company = models.ForeignKey(Company, on_delete = models.CASCADE, related_name = 'vacancies')

    def __str__(self):
        return  self.name

    def short(self):
        return{
            'name':self.name,
            'description':self.description,
            'salary':self.salary,
            'company':self.company.name
        }
    class Meta:
        verbose_name = "Vacancy"
        verbose_name_plural = "Vacancies"