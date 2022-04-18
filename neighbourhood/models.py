from unicodedata import name
from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class NeighbourHood(models.Model):
    name= models.CharField(max_length=50)
    location= models.CharField(max_length=50)
    occupants_count=models.IntegerField(default=0)
    user= models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    neighbourhood_photo= CloudinaryField('image', null=True, blank=True)
    health_no= models.IntegerField(null=True, blank=True)
    police_no=models.IntegerField(null=True, blank=True)

    class Meta:
        ordering=['-pk']
    
    def __str__(self):
        return f'{self.name}'
    
    def create_neighbour(self):
        self.save()
    def delete_neighbour(self):
        self.delete()

    def update_neighbourhood(self, id, name, location, occupants_count, health_no, police_no, neighbourhood_photo):
        update=NeighbourHood.objects.filter(id=id).update(name=name, location=location, occupants_count=occupants_count, health_no=health_no, police_no=police_no, neighbourhood_photo=neighbourhood_photo)
        return update
    
    def find_neighbourhood(self,neighbourhood_id):
        neighbourhood=NeighbourHood.objects.filter(self=neighbourhood_id)
        return neighbourhood

class Profile(models.Model):
    profile_photo = CloudinaryField('image')
    name=models.TextField(max_length=44)
    user=models.OneToOneField(User,on_delete=models.CASCADE, related_name='profile')
    neighborhood=models.ForeignKey(NeighbourHood, on_delete=models.CASCADE, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    email=models.CharField(null=True, max_length=50)
    phone_number=models.IntegerField(null=True)

    @receiver(post_save , sender = User)
    def create_profile(instance,sender,created,**kwargs):
      if created:
        Profile.objects.create(user = instance)

    @receiver(post_save,sender = User)
    def save_profile(sender,instance,**kwargs):
      instance.profile.save()

      def __str__(self):
        return f'{self.user.username} profile'
