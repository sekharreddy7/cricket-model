from django.db import models

# Create your models here.

class game(models.Model):
    team1=models.CharField(max_length=100,primary_key=True)
    
class cricket(models.Model):
    team1=models.ForeignKey(game, on_delete=models.CASCADE)
    player_name1=models.CharField(max_length=100,primary_key=True)
    url=models.URLField(max_length=200)
class csk(models.Model):
    player_name1=models.ForeignKey(cricket, on_delete=models.CASCADE)
    player_age=models.IntegerField()

    

    



