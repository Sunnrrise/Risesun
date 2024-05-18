from django.db import models

class ProseModel(models.Model):
    prose_text = models.TextField(verbose_name="نص النثر")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء")

    class Meta:
        app_label = 'bookmodule'

    def __str__(self):
        return self.prose_text
