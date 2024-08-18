from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

#الوجبة
class Meal(models.Model): 
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=360)

    def number_of_rating(self):
        try:
            rating=Rating.objects.filter(meal=self)
            return len(rating)
        except:
            return 0
        
        
    def avg_rating(self):
        sum=0
        try:
            rating=Rating.objects.filter(meal=self)
            
            for i in rating:
                sum = sum + i.stars
                
            if len(rating)>0:
                avg = sum / len(rating)
                return avg
            
            else:
                return 0
                
        except:
            return 0
    
    def __str__(self):
        return self.title

#التقييم بين الوحبة وال مستخدم
class Rating(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])#التقييم عدد صحيح من 1 لل 5

    # def __str__(self):
    #     return self.meal


    class Meta:
        unique_together = (('user', 'meal'),)
        # index_together=(('user', 'meal'),)#للاصدارات القديمة
        
        indexes=[
            models.Index(fields=['user','meal']),
                 ]
        # indexes=