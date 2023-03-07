from django.contrib import admin
from .models import Profile, Post, LikePost, FollowersCount , Instructor , News , GetPremium , Subject , BuyLesson
from .models import RechargeRequest , Code , Comment , Reply , Activity
# Register your models here.



class MainAdmin(admin.ModelAdmin):
    list_display =  ['user' ,'phone' , 'year' , 'premium' , 'instructor' , 'admin' , 'public', 'money' , 'no_of_buys']
    list_editable = ['year' , 'premium' , 'instructor' , 'admin' ,'public', 'money' , 'no_of_buys']



admin.site.register(Profile , MainAdmin)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(RechargeRequest)
admin.site.register(Code)
admin.site.register(BuyLesson)
admin.site.register(Activity)
admin.site.register(GetPremium)
admin.site.register(Subject)
admin.site.register(News)
admin.site.register(Instructor)
admin.site.register(LikePost)
admin.site.register(FollowersCount)