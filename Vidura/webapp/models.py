from django.db import models


class DietaryPreference(models.TextChoices):
    NONE = 'NONE'
    VEGETARIAN = 'VE'
    VEGAN = 'VG'


class SimulatedConversation(models.Model):
    """
    Stores the result of simulated conversations
    where ChatGPT answers its top 3 favorite foods.
    """
    dietary_preference = models.CharField(
        max_length=20,
        choices=DietaryPreference.choices,
        default=DietaryPreference.NONE
    )
    favorite_foods = models.JSONField(default=list)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Conversation [{self.timestamp}] ({self.dietary_preference})"
