from django.db import models

class Cron(models.Model):
    name = models.CharField(max_length=256)
    minute = models.CharField(max_length=64)
    hour = models.CharField(max_length=64)
    day_of_month = models.CharField(max_length=64)
    month = models.CharField(max_length=64)
    day_of_week = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class CheckListTemplate(models.Model):
    SHIFT_CHOICES = (
        (1,"Day"),
        (2,"Night")
    )

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    lists = models.ManyToManyField("self", symmetrical=False, blank=True, null=True)
    repeat_rule = models.ForeignKey(Cron, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class CheckList(models.Model):
    template = models.ForeignKey(CheckListTemplate, on_delete=models.CASCADE)
    date_time = models.DateTimeField()

    def __str__(self):
        return self.template.title

class CheckTemplate(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    lists = models.ManyToManyField(CheckListTemplate)

    def __str__(self):
        return self.title

class Check(models.Model):
    STATUS_CHOICES = (
        (1,'Okay'),
        (2,'Problem'),
        (3,'Follow Up')
    )
    template = models.ForeignKey(CheckTemplate, on_delete=models.CASCADE)
    proof_file = models.FileField(upload_to="check_files", null=True, blank=True)
    checklist = models.ForeignKey(CheckList, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS_CHOICES, null=True, blank=True)

    def __str__(self):
        return " - ".join([self.template.title, self.checklist.template.title])