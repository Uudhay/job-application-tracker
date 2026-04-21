from django.db import models

class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('Applied', 'Applied'),
        ('Interview Scheduled', 'Interview Scheduled'),
        ('Selected', 'Selected'),
        ('Rejected', 'Rejected'),
    ]

    company_name = models.CharField(max_length=100)
    job_role = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    applied_date = models.DateField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.company_name