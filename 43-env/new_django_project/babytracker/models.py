from django.db import models

# heslo123


class BabyInfo(models.Model):
    name = models.CharField(max_length=50, default="My baby")
    birth_date = models.DateField()
    weight = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, help_text="Enter weight in kg"
    )
    height = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, help_text="Enter height in cm"
    )
    notes = models.TextField(blank=True)
