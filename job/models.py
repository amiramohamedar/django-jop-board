from django.db import models



'''
djang model field : # title
-html widget # charfield input
-valadtion  # email password or any input requierinput
db size     #max_length=100
'''
JOB_TYPE= (
    ('Full Time', 'Full Time'),
    ('Part Time','Part Time'),
)

# Create your models here.
class Job(models.Model): #تكافئ table
    title = models.CharField(max_length=100 ) # coulmn يكافئ 
    #location 
    jop_type= models.CharField(max_length=15, choices=JOB_TYPE )
    description = models.TextField (max_length=2000 ) 
    published_at = models.DateTimeField(auto_now=True)
    Vacancy = models.IntegerField(default=1)
    salary=models .IntegerField(default=0)
    experience = models.IntegerField (default=1)
    Category = models.ForeignKey('Category',on_delete=models.CASCADE )
#عشان اظهر ال عنوان الوظيفه اللى هيا jop object اللى رجعلتى لما عملت save لل الوظيفه 
    def __str__ (self):
        return self.title

class Category (models.Model):
    name = models.CharField(max_length=25)

    def __str__ (self):
        return self.name

