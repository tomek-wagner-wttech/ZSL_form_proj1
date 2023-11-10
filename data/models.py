from django.db import models

class Data(models.Model):
    data = models.CharField("Data", max_length=240)
    data2 = models.CharField("Data2", max_length=240)

    def __str__(self):
        return data
        #return " ".join("Data:", self.data, "Data2", self.data2)