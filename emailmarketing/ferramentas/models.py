from django.db import models
from django.utils import timezone
import datetime, os
from .contents.model_0002 import send_email

# Create your models here.
class Campaign(models.Model):
    status_choice = [
        ('Created', 'Created'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled')
    ]
    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=255)
    start_date = models.DateField('Start Date', default=datetime.date.today)
    finish_date = models.DateField('Finish Date', default=datetime.date.today)
    status = models.CharField(max_length=12, choices=status_choice, default='Created')
    group_contacts = models.ForeignKey("GroupContacts", on_delete=models.CASCADE)
    content = models.ForeignKey("EmailContent", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def send(self):
        for contact in self.group_contacts.emails.all():
            email = contact.email
            nome = email.split("@")[0]
            self.content.send(nome, email)
        return 0

    def save(self, *args, **kwargs):
        #send_email(self.subject, self.content)
        self.send()
        super(Campaign, self).save(*args, **kwargs)

class Clients(models.Model):
    SEXO_CHOICES = (
        ("F", "Feminino"),
        ("M", "Masculino"),
        ("N", "Nenhuma das opções")
    )

    nome = models.CharField(max_length=100, null=False, blank=False)
    data_nascimento = models.DateField("Data de nascimento",null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    cargo = models.CharField(max_length=50, null=False, blank=False)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=False, null=False)
    #endereco = models.OneToOneField("Adresses", on_delete=models.SET_NULL, null=True)
    CEP = models.CharField(max_length=8, null=False, blank=False)
    numero = models.IntegerField(null=False, blank=False)
    complemento = models.CharField(max_length=200, null=False, blank=True)

    def __str__(self):
        return self.nome

class Contact(models.Model):
    email = models.EmailField(null=False, blank=False)
    def __str__(self):
        return self.email

class GroupContacts(models.Model):
    nome = models.CharField(max_length=12, null=False, blank=False)
    emails = models.ManyToManyField(Contact)

    def __str__(self):
        return self.nome

class EmailContent(models.Model):
    nome = models.CharField(max_length=25, null=False, blank=False)
    created_at = models.DateField('Created At', default=datetime.date.today)
    script = models.FilePathField(path="ferramentas/contents/", blank=False, default="")
    htmlpath = models.FilePathField(path="ferramentas/contents/")
    #message = models.TextField(help_text='Write your email here', default='Ola')

    def __str__(self):
        return self.nome

    def send(self, nome, email):
        import importlib.util
        spec = importlib.util.spec_from_file_location("contents", self.script)
        foo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(foo)
        print(f"Enviando email para {nome}.")
        foo.send_email(nome, email, self.htmlpath)


class Reports(models.Model):
    pass



#class Adresses(models.Model):
#    CEP = models.IntegerField(unique=True)
#    logradouro = models.CharField(max_length=200, null=False, blank=False)
#    numero = models.IntegerField(null=False, blank=False)
#    complemento = models.CharField(max_length=200, null=False, blank=False)
#    bairro = models.CharField(max_length=50, null=False, blank=False)
#    cidade = models.CharField(max_length=100, null=False, blank=False)
#    pais = models.CharField(max_length=50, null=False, blank=False)
#
#    def __str__(self):
#        return self.logradouro

