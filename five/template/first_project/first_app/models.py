from django.db import models

# Create your models here.

class Topic(models.Model):
    top_name = models.CharField(max_length=255,unique = True)


    def __str__(self):
        return self.top_name



class webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    url = models.URLField(unique = True)

    def __str__(self):
        return self.name



class AccesRecord(models.Model):
    name = models.ForeignKey(webpage,on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)
