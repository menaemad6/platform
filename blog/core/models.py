from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime






from django.utils.text import slugify

from django.db.models.signals import post_save

User = get_user_model()


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)

    video = models.FileField(upload_to='lessons' , blank=True)


    image = models.ImageField(upload_to='post_images')
    title = models.CharField(blank=True , max_length=100)
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)
    no_of_buys = models.IntegerField(default=0)
    no_of_comments = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    teacher_name = models.CharField(max_length=100 ,blank=True , null=True)
    teacher_img = models.ImageField(upload_to='teacher_images' , blank=True , null=True)


    class subjects(models.TextChoices):
        arabic = 'arabic',
        english = 'english',
        math = 'math',
        physics = 'physics',
        chemistry = 'chemistry',
        biology = 'biology',
        french = 'french',
        german = 'german'
    subject = models.CharField(max_length=25, choices=subjects.choices, default=subjects.arabic,  blank=True)
    class years(models.TextChoices):
        first = 'first',
        second = 'second',
        third = 'third',
    year = models.CharField(max_length=25, choices=years.choices, default=years.first,  blank=True)


    class attachment_type(models.TextChoices):
        homework = 'homework',
        test = 'test',
        link = 'link'
    attach1_type = models.CharField(max_length=25, choices=attachment_type.choices, default=attachment_type.homework,  blank=True)
    attach1_link = models.CharField(blank=True , max_length=300)

    attach2_type = models.CharField(max_length=25, choices=attachment_type.choices, default=attachment_type.homework,  blank=True)
    attach2_link = models.CharField(blank=True , max_length=300)

    attach3_type = models.CharField(max_length=25, choices=attachment_type.choices, default=attachment_type.homework,  blank=True)
    attach3_link = models.CharField(blank=True , max_length=300)

    slug = models.SlugField(blank=True, null=True)

    class Meta:
        verbose_name = ("Lesson")
        verbose_name_plural = ("Lessons")
    
    
    def save(self , *args , **kwargs):
        if not self.slug :
            self.slug = slugify(self.id)
        super(Post , self).save( *args , **kwargs)

    def __str__(self):
        return self.title + ' ( ' + self.user + ' ) ' +  '- ' + self.year + ' Year ' 



# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    name = models.CharField(max_length=100, blank=True , null=True)
    school = models.TextField(blank=True)
    image = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    location = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=100, blank=True , null=True)
    class years(models.TextChoices):
        first = 'first',
        second = 'second',
        third = 'third',
        none = 'none',
    year = models.CharField(max_length=25, choices=years.choices, default=years.none,  blank=True , null=True)

    money = models.IntegerField(editable=True , default='0')
    no_of_buys = models.IntegerField(default=0)

    public = models.BooleanField(default=True)
    join_date = models.DateTimeField(default=datetime.now)
    premium = models.BooleanField(default=True)
    instructor = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)






    class subjects(models.TextChoices):
        arabic = 'arabic',
        english = 'english',
        math = 'math',
        physics = 'physics',
        chemistry = 'chemistry',
        biology = 'biology',
        french = 'french',
        german = 'german',
        student = 'student'
    subject = models.CharField(max_length=25, choices=subjects.choices, default=subjects.student, null=True,  blank=True)

    def __str__(self):
        return self.user.username



class BuyLesson(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username + ' Buyed ' + self.post_id

    class Meta:
        verbose_name = ("Buy")
        verbose_name_plural = ("Buys")



class RechargeRequest(models.Model):
    username = models.CharField(max_length=100)
    amount = models.CharField(max_length=500)
    sender_number = models.CharField(max_length=100 , blank=True)
    wallet_number = models.CharField(max_length=100 , blank=True)
    created_at = models.DateTimeField(default=datetime.now)


    def __str__(self):
        return self.username + ' Requested ' + self.amount

    class Meta:
        verbose_name = ("Recharge")
        verbose_name_plural = ("Recharges")





class Code(models.Model):
    code_id = models.CharField(max_length=5 , blank=True , null=True)
    money = models.IntegerField()

    slug = models.SlugField(blank=True , null=True , allow_unicode=True , unique=True)
    def save(self , *args , **kwargs):
        if not self.slug :
            self.slug = slugify(self.code_id)
            super(Code , self).save(*args , **kwargs)

    def __str__(self):
        return self.code_id 

    class Meta:
        verbose_name = ("Code")
        verbose_name_plural = ("Codes")







class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)


    def __str__(self):
        return self.username + ' Liked ' + self.post_id

    class Meta:
        verbose_name = ("Like")
        verbose_name_plural = ("Likes")




class FollowersCount(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    follow_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.user


    class Meta:
        verbose_name = ("Follow")
        verbose_name_plural = ("Follows")




class Comment(models.Model):
    comment_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    post_id = models.CharField(max_length=500)

    commented_to = models.CharField(max_length=500 , blank=True)

    comment = models.CharField(max_length=500)
    created_at = models.DateTimeField(default=datetime.now)
    username = models.CharField(max_length=100)
    username_image = models.ImageField(upload_to='comment_images' , blank=True , null=True)
    username_name = models.CharField(max_length=100 ,blank=True)

    no_of_likes = models.IntegerField(default=0)  
    no_of_replys = models.IntegerField(default=0)  

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = ("Comment")
        verbose_name_plural = ("Comments")




class Reply(models.Model):
    reply_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    comment_id = models.CharField(max_length=500)

    replyed_to = models.CharField(max_length=500 , blank=True)
    comment_text = models.CharField(max_length=500 , blank=True)

    reply = models.CharField(max_length=500)
    created_at = models.DateTimeField(default=datetime.now)
    username = models.CharField(max_length=100)
    username_image = models.ImageField(upload_to='comment_images' , blank=True , null=True)
    username_name = models.CharField(max_length=100 ,blank=True)

    no_of_likes = models.IntegerField(default=0)  

    def __str__(self):
        return self.username + ' Replyed On ' + self.comment_id

    class Meta:
        verbose_name = ("Reply")
        verbose_name_plural = ("Replys")





class Activity(models.Model):
    activity_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    username = models.CharField(max_length=100)

    lesson_name = models.CharField(max_length=100 , blank=True)
    money = models.IntegerField(editable=True , default='0' , blank=True)
    wallet = models.IntegerField(editable=True , default='0' , blank=True)

    class activity_types(models.TextChoices):
        charge = 'charge',
        purchase = 'purchase'
    activity_type = models.CharField(max_length=25, choices=activity_types.choices,  blank=True)

    class purchase_types(models.TextChoices):
        code = 'code',
        wallet = 'wallet'
    purchase_type = models.CharField(max_length=25, choices=purchase_types.choices,  blank=True)

    created_at = models.DateTimeField(default=datetime.now)



    def __str__(self):
        return self.username

    class Meta:
        verbose_name = ("Activity")
        verbose_name_plural = ("Activities")







class Subject(models.Model):
    subject = models.CharField(max_length=100, blank=True , null=True)
    image = models.ImageField( upload_to='categorys_img/' , verbose_name=("image") , blank=True ,  null=True)
    def __str__(self):
        return  '%s' %(self.subject)


    slug = models.SlugField(blank=True, null=True)
    
    
    def save(self , *args , **kwargs):
        if not self.slug :
            self.slug = slugify(self.subject)
        super(Subject , self).save( *args , **kwargs)




class GetPremium(models.Model):
    user = models.OneToOneField(User, verbose_name=("user"), on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True , null=True)
    email = models.CharField(max_length=200, blank=True , null=True)

    class years(models.TextChoices):
        first = 'first',
        second = 'second',
        third = 'third',

    year = models.CharField(max_length=25, choices=years.choices, default=years.first,  blank=True)

    class Meta:
        verbose_name = ("Registration")
        verbose_name_plural = ("Premium Registrations")

    def __str__(self):
        return  '%s' %(self.name)




class Instructor(models.Model):
    name = models.CharField(max_length=100, blank=True , null=True)
    bio = models.CharField(max_length=100, blank=True , null=True)
    facebook = models.CharField(max_length=100, blank=True , null=True)
    image = models.ImageField( upload_to='profile_img/' , verbose_name=("image") , blank=True ,  null=True)
    class subjects(models.TextChoices):
        arabic = 'arabic',
        english = 'english',
        math = 'math',
        physics = 'physics',
        chemistry = 'chemistry',
        biology = 'biology',
        french = 'french',
        german = 'german'
    subject = models.CharField(max_length=25, choices=subjects.choices, default=subjects.arabic,  blank=True)


    def __str__(self):
        return  '%s' %(self.name)



class News(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE ,default='1', blank=True)
    title = models.CharField(max_length=40 , blank=True)
    caption = models.TextField(max_length=1000 , blank=True)
    image = models.ImageField( upload_to='news/' , verbose_name=("News Image") , blank=True ,  null=True)
    date = models.DateTimeField(("join date"),default=datetime.now)
    slug = models.SlugField(blank=True , null=True , verbose_name=("Video Slug (URL)") , allow_unicode=True , unique=True)
    def save(self , *args , **kwargs):
        if not self.slug :
            self.slug = slugify(self.title)
            super(News , self).save(*args , **kwargs)


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = ("New")
        verbose_name_plural = ("News")