from django.db import models
from django.contrib.auth.models import User
# Create your models here.


#QUESTIONS
class Poll(models.Model):
    question = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete= models.CASCADE)
    pub_date = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.question



#OPTIONS
class Choice(models.Model):
    poll = models.ForeignKey(Poll, related_name = 'choices', on_delete = models.CASCADE)
    # One question(poll) has several options
    options = models.CharField(max_length=100)

    def __str__(self):
        return self.options

#VOTES
class Vote(models.Model):
    choice = models.ForeignKey(Choice,related_name= 'votes', on_delete = models.CASCADE)
    poll = models.ForeignKey(Poll,on_delete=models.CASCADE)
    voted_by = models.ForeignKey(User, on_delete = models.CASCADE)

    class Meta:
        unique_together = ("poll","voted_by")