from django.db import models
from django.utils import timezone
from django.core import validators as v
from .validators import validate_name
from move_app.models import Move
from django.core.exceptions import ValidationError

# Create your models here.
class Pokemon(models.Model):
    # CharField is a character field and has a default max length of 255 characters
    name = models.CharField(max_length=255,unique=True,blank=False,null=False,validators=[validate_name])
    # IntegerField will allow only solid numerical values as input
    level = models.IntegerField(default=1,validators=[v.MinValueValidator(1),v.MaxValueValidator(100)])
    date_encountered = models.DateField(default="2008-01-01")
    date_captured = models.DateTimeField(default=timezone.now)
    
    # date_of_birth = models.DateTimeField()
    # daily_allowance = models.DecimalField(decimal_places=2)
    # year_of_schooling = models.IntegerField()
    description = models.TextField(default="Unkown",validators=[v.MinLengthValidator(25), v.MaxLengthValidator(150)])
    # good_pokmon = models.BooleanField()
    captured = models.BooleanField(default=False)
    
    moves = models.ManyToManyField(Move,default=1)
    
 # DUNDER METHOD
    def __str__(self):
        return f"{self.name} {'has been captured' if self.captured else 'is yet to be caught'}"

    # RAISES POKEMON'S LEVEL
    def level_up(self, new_level):
        self.level = new_level
        self.save()

    # Switches Pokemon's captured status from True to False and vise versa
    def change_caught_status(self, status):
        self.captured = status
        self.save()
        
    def clean(self):
        if self.moves.count() > 4:  # Change the maximum number of relationships as needed
                raise ValidationError("A Pokemon can have at most 4 moves.")