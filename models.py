from django.db import models
from django.contrib.auth.models import User

class userLogin(models.Model):
    #user is the user who is going to login
    user = models.OneToOneField(User)
    #emailID is the email id of the user who is logging in / siging up
    emailID = models.EmailField(max_length=75)
    #choices include the way user wants to signup
    USER_TYPES = (
            ('0','NGO'),
            ('1','Non NGO')
        )
    user_type = models.CharField(max_length=1, choices = USER_TYPES)

class commonUser(models.Model):
    #user of the user
    user = models.OneToOneField(User)
    #firstname hold the first name of the user
    firstName = models.CharField(max_length = 32)
    #lastname hold the last name of the user
    lastName = models.CharField(max_length = 32)
    #conatct number is user's contact number
    contactNumber = models.IntegerField()
    #address holds user's address
    address = models.CharField(max_length = 100)
    #user's Proffession
    PROFESSION_TYPES = (
            ('student','Student'),
            ('professional','Professional')
        )
    profession = models.CharField(max_length = 12, choices = PROFESSION_TYPES)
    #user's date of birth
    dob = models.DateField()
    #user's gender
    GENDER_TYPES = (
            ('M','Male'),
            ('F','Female')
        )
    gender = models.CharField(max_length = 1, choices = GENDER_TYPES)
    #profile Picture
    profilePic = models.ImageField(upload_to = 'userImage/' ,default = 'userImage/None/no-img.jpg')

    def __unicode__(self):
        return self.firstName
    
class ngoUser(models.Model):
    #user of the ngo
    user = models.OneToOneField(User)
    #ngo name will be used for ngo's Login
    ngoName = models.CharField(max_length= 100)
    #manager's details start here with first name
    manFirstName = models.CharField(max_length=50)
    #manager's last name
    manLastName = models.CharField(max_length=50)
    #manager's contact number
    manConactNum = models.IntegerField()
    #ngo head office address
    ngoAddress = models.CharField(max_length = 100)
    #ngo's head office contact number
    ngoConactNum = models.IntegerField()
    #ngo's details
    ngoDetails = models.CharField(max_length = 1000)
    # ngo's URL
    ngoUrl = models.URLField()
    #ngo Image
    ngoProfilePic = models.ImageField(upload_to = 'ngoImage/' ,default='ngoImage/no-img.jpg')

    def __unicode__(self):
        return self.ngoName

class userFollow(models.Model):
    #followerID is the id of the follower
    followerID = models.ForeignKey(commonUser,related_name="userflr_fID")
    #followedID is the id the person being followed
    follwedID = models.ForeignKey(commonUser,related_name="userfld_fID")

class ngoFollow(models.Model):
    #followerID is the id of the follower
    followerID = models.ForeignKey(commonUser,related_name="ngoflr_fID")
    #followedID is the id of the NGO being followed
    followedID = models.ForeignKey(ngoUser,related_name="ngofld_fID")

class event(models.Model):
    #ngoID is the id of the ngo who's event is being posted
    ngoID = models.ForeignKey(ngoUser)
    #eventDate is the date of event
    eventDate = models.DateField()
    #eventName is the name of the event that is being organised
    eventName = models.CharField(max_length = 100)
    #eventDetails is the detail of the event
    eventDetail = models.CharField(max_length = 1000)

class eventFollower(models.Model):
    #eventId id the id of the event which is being followed
    eventID = models.ForeignKey(event)
    #followerdID is the id the person who is following the event
    followID = models.ForeignKey(commonUser)
