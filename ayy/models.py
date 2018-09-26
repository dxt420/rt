# from django.db import models
# import datetime
# # Create your models here.

# YEAR_CHOICES = [(r,r) for r in range(2000,datetime.date.today().year+1)]
    
# class Artist(models.Model):
#     artist_name = models.CharField(max_length=50)
#     label = models.CharField(max_length=50)

#     def __str__(self):
#         return self.artist_name

# class Song(models.Model):
#     title = models.CharField(max_length=50)
#     artist_name = models.ForeignKey(Artist,  on_delete=models.CASCADE)
#     duration = models.CharField(max_length=10)
#     album = models.CharField(max_length=50,default="Single")
#     year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)
#     producer = models.CharField(max_length=50)
#     plays = models.IntegerField()
#     song_file = models.FileField(upload_to='media/', max_length=100)

#     def __str__(self):
#         return self.title 

# class Genre(models.Model):
#     name = models.CharField(max_length=50)
#     short_description = models.CharField(max_length=50)
#     def __str__(self):
#         return self.name

    
# class Album(models.Model):
#     name = models.CharField(max_length=50)
#     artist = models.ForeignKey(Artist,  on_delete=models.CASCADE)
#     year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)
#     cover_art = models.ImageField(upload_to='media/')
#     song_file = models.FileField(upload_to='media/', max_length=100)

#     def __str__(self):
#         return self.name
