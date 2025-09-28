from django.db import models

class GSTEntry(models.Model):
    category = models.CharField(max_length=100)
    subcategory = models.CharField(max_length=200)
    gst_rate = models.CharField(max_length=10)
    notes = models.TextField()

    class Meta:
        app_label = 'chat'  # 👈 This tells Django it's part of the 'chat' app

    def __str__(self):
        return f"{self.subcategory} ({self.gst_rate})"