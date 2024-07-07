from django.db import models

# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=20)

    def __str__(self):
        return self.user_name

class PoleTable(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.TextField()

    def __str__(self):
        return self.question

class PoleHaveOptions(models.Model):
    option = models.CharField(max_length=50)

    def __str__(self):
        return self.option

class Vote(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    user_question = models.ForeignKey(PoleTable, on_delete=models.CASCADE, null=True)
    user_option = models.ForeignKey(PoleHaveOptions, on_delete=models.CASCADE)

    def __str__(self):
        return f"Vote by {self.user_id} for option {self.user_option}"
