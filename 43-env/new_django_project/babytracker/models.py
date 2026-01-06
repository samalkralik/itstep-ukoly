from django.db import models

# heslo123


class BabyInfo(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name


class GrowthRecord(models.Model):
    baby = models.ForeignKey(BabyInfo, on_delete=models.CASCADE)
    date = models.DateField()
    weight_kg = models.DecimalField(max_digits=4, decimal_places=2)
    height_cm = models.DecimalField(max_digits=5, decimal_places=2)
    head_circumference_cm = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.baby.name} growth on {self.date}"
