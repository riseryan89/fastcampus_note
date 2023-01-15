from django.db import models


class ImageModel(models.Model):
    note = models.ForeignKey("Note", on_delete=models.CASCADE, related_name="images")
    image = models.CharField(max_length=256, null=False)

    def __str__(self):
        return self.note
