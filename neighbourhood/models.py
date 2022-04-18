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
    neighbourhood=models.ForeignKey(NeighbourHood, on_delete=models.CASCADE, null=True)
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


class Business(models.Model):
    name = models.CharField(max_length=150, verbose_name='Business Name', null=True, blank=True)
    description = models.TextField(blank=True, verbose_name='Description')
    email = models.CharField(max_length=150, verbose_name='Business Email Address', null=True, blank=True)
    neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE, verbose_name='NeighbourHood')
    picture=CloudinaryField('image', blank=True)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Business Owner')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created')
    
    def __str__(self):
        return str(self.name)

    def get_businesses(self):
        businesses = Business.objects.all()
        return businesses

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    def find_business(self,business_id):
        business = Business.objects.filter(self = business_id)
        return business

    def update_business(self, id, name, description, email, neighbourhood):
        update = NeighbourHood.objects.filter(id = id).update(name = name , description = description, email = email, neighbourhood = neighbourhood)
        return update
    
    class Meta:
        verbose_name_plural = 'Businesses'