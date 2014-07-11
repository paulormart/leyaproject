
from django.db import models
from django.contrib.auth.models import User


# Helpers
def get_file_upload_path(instance, filename):
    return "image/%s" % (filename)

class Hello(models.Model):
    #user = models.ForeignKey(User)
    title = models.CharField(max_length=64)
    file = models.ImageField(upload_to=get_file_upload_path)

    def delete(self, *args, **kwargs):
        storage, path = self.file.storage, self.file.path
        super(Hello, self).delete(*args, **kwargs)
        storage.delete(path)