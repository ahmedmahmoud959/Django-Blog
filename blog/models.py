
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
# Create your models here.



class Categories(models.Model):
    '''
    '''
    
    cat_name = models.CharField( max_length=30 , verbose_name='اسم القسم')
    description = models.TextField(max_length=200 , verbose_name='وصف القسم')
    cat_color = models.CharField(max_length=15 , verbose_name='لون القسم')
    
    def __str__(self):
        return self.cat_name
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'القسم'
        verbose_name_plural = 'الاقسام'
       
class Author(models.Model):
    '''
    '''
    name = models.CharField(max_length=35,primary_key=True)
    info = models.TextField()
    
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'المؤلف'
        verbose_name_plural = 'المؤلفين'



class Post(models.Model):
    '''
   
    '''
   
    title = models.CharField(max_length=70 , verbose_name='عنوان المقال')
    description = models.TextField(max_length=200 , verbose_name='وصف المقال')
    image_main = models.ImageField(upload_to ='main-post/%y/%m/%d' ,default='default.png',blank=True , verbose_name='صورة المقال')
    image_url = models.URLField(blank=True, verbose_name='رابط صورة المقال')
    content = RichTextField(verbose_name='محتوى المقال')
    active = models.BooleanField(default=True , verbose_name='نشط')
    show_in_home_first = models.BooleanField(default=False,verbose_name='طهور في أول مقدة الرئيسية')
    show_in_home = models.BooleanField(default=False,verbose_name='طهور في مقدة الرئيسية')
    post_date  = models.DateTimeField(default=timezone.now , null=True , verbose_name='تاريخ الانشاء')
    post_update = models.DateTimeField(auto_now=True,null=True)
    views = models.IntegerField(default=0 ,null=True)
    category = models.ForeignKey(Categories ,on_delete=models.CASCADE, verbose_name='القسم')
    author = models.ForeignKey(Author ,on_delete=models.CASCADE, verbose_name='المؤلف' ,null=True)
    ads_num = models.IntegerField(default=1)
    def __str__(self):
        return self.title
  
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'مقال'
        verbose_name_plural = 'مقالات'
        ordering = ('-post_date',)

        
        

# class Ads(models.Model):
#     '''
#     '''
#     page_choices = (
#         ('home','الرئيسية') ,
#         ('post','المقال') , 
#         ('cat','القسم') ,
#         ('author','المؤلف')
#         )
#     posision_choices = (
#         ('V','عمودي'),
#         ('H','افقي')
#         )
#     ad_serv= models.CharField(max_length=10)
#     code = models.TextField()
#     page = models.CharField(max_length=35,choices=page_choices)
#     posision = models.CharField(max_length=20,choices=posision_choices)
    
    
    
    # def __str__(self):
    #     return self.ad_serv
    
    # class Meta:
    #     db_table = ''
    #     managed = True
    #     verbose_name = 'إعلان'
    #     verbose_name_plural = 'إعلانات'