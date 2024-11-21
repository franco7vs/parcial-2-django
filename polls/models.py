from django.db import models
from django.utils import timezone
import datetime
from django.contrib import admin

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    author_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.question_text

    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices")
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    pub_date = models.DateTimeField("date published", null=True, blank=True) 

    def __str__(self):
        return self.choice_text

    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return self.pub_date is not None and now - datetime.timedelta(days=1) <= self.pub_date <= now

    class Meta:
        verbose_name = "Choice"
        verbose_name_plural = "Choices"
