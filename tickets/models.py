from django.db import models

class Client(models.Model):
    client_name = models.CharField(max_length=200)
    client_email = models.EmailField()
    date_registered = models.DateTimeField('Date Registered')
    contracted_monthly_service_hours = models.FloatField(default=1)
    contracted_monthly_SEM_hours = models.FloatField(default=0)
    paid_extra_hours = models.FloatField(default=0)
    hours_used_this_month = models.FloatField(default=0)
    discontented_client = models.BooleanField(default=False)
    priority_client = models.BooleanField(default=False)
    def __str__(self):
        return self.client_name

class Ticket(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    issue = models.TextField()
    severity = models.CharField(
        max_length=2,
        choices = [
        ('ST', 'Standard'),
        ('HI','High'),
        ('VH','Very High'),
        ('CR','Critical')
        ]
    )
    hours_predicted = models.FloatField(default=0)
    hours_used = models.FloatField(default=0)
    customer_feedback_required = models.BooleanField(default=False)
    resolved = models.BooleanField(default=False)
    date_created = models.DateTimeField('Date Created')
    def __str__(self):
        return f'{self.client} - {self.issue}'

class FeedbackRequest(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    requested_information = models.TextField()
    date_sent = models.DateTimeField('Date Sent')
    client_responded = models.BooleanField(default=False)
    response = models.TextField(blank=True)
    def __str__(self):
        return f'{self.ticket.client} - {self.ticket.issue} - Response Requested: {self.date_sent:%d-%m-%Y}'
