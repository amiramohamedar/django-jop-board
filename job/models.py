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

# الداله دى هتتولى مهمه رفع الصورة 
def image_upload (instance , filename):
    imagename , extension = filename.split(".") # السطر دا خاص ب الextintion الخاص بالصورة    
    return "jobs/%s.%s"%(instance.id, extension)  # عاوز تحط ايه هنا 


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
    image = models.ImageField(upload_to=image_upload)
    slug = models.SlugField(blank=True , null=True)
    def save (self,*args , **kwargs):
        self.slug = lugify(self.title)
        super(Job,self).save(*args, **kwargs)



#عشان اظهر ال عنوان الوظيفه اللى هيا jop object اللى رجعلتى لما عملت save لل الوظيفه 
    def __str__ (self):
        return self.title

class Category (models.Model):
    name = models.CharField(max_length=25)

    def __str__ (self):
        return self.name

