from django.db import models
from django.contrib.auth.models import User

# Create your models here.
Gender_Choice = (
    ('M','Male'),
    ('F','Female')
)

class Tinder_Account(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    facebook_id = models.ForeignKey("core.Facebook",on_delete=models.CASCADE)
    first_name = models.CharField(max_length=64)
    age = models.PositiveSmallIntegerField()
    interests = models.CharField(max_length=512)
    gender = models.CharField(max_length=1, choices=Gender_Choice)
    #fb friends
    about = models.TextField(blank=True)
    work = models.CharField(max_length=32,blank=True,null=True)
    max_distance = models.IntegerField()
    location = models.ForeignKey("core.Location",on_delete=models.SET_NULL,blank=True,null=True)
    age_range = models.PositiveSmallIntegerField()
    privacy = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id)

class Facebook(models.Model):
    profile = models.CharField(max_length=512)

    def __str__(self):
        return self.profile

class Location(models.Model):
    gps = models.FloatField(max_length=32)
    name = models.CharField(max_length=128)

    def __str__(self):
        return str(self.id)

class Instagram_Account(models.Model):
    instagram_user_id = models.CharField(max_length=64);
    Photos = models.ImageField()

Like_Choices= (
    ('L','Like'),
    ('SL','Super Like'),
    ('NI','Not Interested')
)

class Like(models.Model):
    liked_user = models.ForeignKey("core.Tinder_Account",on_delete=models.CASCADE,related_name='LikeGivenTo')
    response = models.CharField(max_length=2, choices=Like_Choices)
    user = models.ForeignKey("core.Tinder_Account",on_delete=models.CASCADE,related_name='LikeGivenBy')
    match = models.ForeignKey("core.Match",on_delete=models.CASCADE)

Super_Like_Choices= (
    ('L','Like'),
    ('NI','Not Interested')
)

class Super_Like(models.Model):
    liked_user = models.ForeignKey("core.Tinder_Account",on_delete=models.CASCADE,related_name='SuperLikeGivenTo')
    response = models.CharField(max_length=2, choices=Super_Like_Choices)
    user = models.ForeignKey("core.Tinder_Account",on_delete=models.CASCADE,related_name='SuperLikeGivenBy')
    match = models.ForeignKey("core.Match",on_delete=models.CASCADE)

class Match(models.Model):
    msg_id = models.CharField(max_length=64)
    location_id = models.CharField(max_length=64)
    timeStamp = models.DateTimeField(auto_now_add=True)
    message = models.ForeignKey("core.Message",on_delete=models.CASCADE)

class Message(models.Model):
    receiver = models.CharField(max_length=64)
    message_content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True)
    match_id = models.ForeignKey("core.UnMatch",on_delete=models.CASCADE,null=True,blank=True)
    report_user_id = models.ForeignKey("core.ReportUser",on_delete=models.CASCADE,null=True,blank=True)

class UnMatch(models.Model):
    cause_id = models.CharField(max_length=64)

class ReportUser(models.Model):
    cause_id = models.CharField(max_length=64)