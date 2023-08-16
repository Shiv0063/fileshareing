from django.db import models
from django.utils import timezone
from datetime import datetime
import os
# Create your models here.
class files(models.Model):
    dt=datetime.now().strftime('%B%d%Y')
    name = models.FileField(upload_to=f'{dt}',null=True,blank=True)
    status = models.IntegerField(default=0)
    date = models.DateTimeField(default=datetime.now())

    def filename(self):
        x = str(self.name)
        x = x.split("/")
        x=str(x[1])
        return x

    def filex(self):
        x = str(self.name)
        x = x.split(".")
        x=str(x[-1])
        return x

    def filesize(self):
        filename = f'./media/{self.name}'
        filename=str(filename)
        stats = os.stat(filename)
        vlu=int(stats.st_size)
        vlu= vlu /(1024)
        vlu= vlu /(1024)
        if  0.9<=vlu:
            x=str(round(vlu,2))
            x=x+' MB'
            return x
        else:
            x=str(round(vlu,4))
            x=x+' KB'
            return x

    def filedate(self):
            return self.date.strftime('%B %d %Y')

    def delete(self, *args, **kwargs):
        self.name.delete()
        super().delete(*args, **kwargs)


class systmfile(models.Model):
    files = models.FileField(upload_to='systm',null=True,blank=True)
    status = models.IntegerField(default=0)
    date = models.DateTimeField(default=datetime.now())

    def delete(self, *args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)

    def filedate(self):
            return self.date.strftime('%B %d %Y')
