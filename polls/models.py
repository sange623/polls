from django.db import models

# Create your models here.

class Poll(models.Model):
    user_name = models.CharField(max_length=20)

    def __str__(self):
        return self.user_name

class PollTable(models.Model):
    user = models.ForeignKey(Poll, on_delete=models.CASCADE)
    question = models.TextField()

    def __str__(self):
        return self.question

class PollHaveOptions(models.Model):
    user_option = models.ForeignKey(PollTable, on_delete=models.CASCADE, related_name='options', null=True)
    option = models.CharField(max_length=50)

    def __str__(self):
        return self.option

class Vote(models.Model):
    user_id = models.ForeignKey(Poll, on_delete=models.CASCADE)
    user_question = models.ForeignKey(PollTable, on_delete=models.CASCADE, null=True)
    user_option = models.ForeignKey(PollHaveOptions, on_delete=models.CASCADE)

    def __str__(self):
        return f"Vote by {self.user_id} for option {self.user_option}"
