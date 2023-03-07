from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Activity , Reply , Comment, Code , RechargeRequest, Profile, Post, LikePost, FollowersCount , Subject , GetPremium , News , Instructor , BuyLesson
from itertools import chain
import random


from django.shortcuts import get_object_or_404
# Create your views here.


def error_404(request , exception):
    return render(request , 'error-404.html' , status=404)


@login_required(login_url='signin')
def index(request):
    instructor = Instructor.objects.all()
    subject = Subject.objects.all()
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    return render(request, 'main/index.html', {'instructor':instructor    , 'user_profile': user_profile , 'subject':subject})

@login_required(login_url='signin')
def news(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    news = News.objects.all()
    context = {'news' : news , 'user_profile': user_profile }
    return render(request, 'main/news.html' , context)

@login_required(login_url='signin')
def news_detail(request , slug):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)

    news = get_object_or_404(News ,slug=slug )

    context = {'news' : news , 'user_profile': user_profile }
    return render(request , 'main/news-page.html' , context)

@login_required(login_url='signin')
def categorys(request):
    subject = Subject.objects.all()
    context = {'subject' : subject}
    return render(request , 'main/categorys.html' , context)


@login_required(login_url='signin')
def inbox(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)

    messages = Reply.objects.filter(replyed_to=request.user.username).values()

    return render(request, 'accounts/inbox.html' , {'messages' : messages , 'user_profile': user_profile })




@login_required(login_url='signin')
def account_activity(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)

    activities = Activity.objects.filter(username=request.user.username).values()

    return render(request, 'accounts/account-activity.html' , {'activities' : activities , 'user_profile': user_profile })


@login_required(login_url='signin')
def account_payment(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)

    payments = Activity.objects.filter(username=request.user.username).values()

    return render(request, 'accounts/account-payment.html' , {'activities' : payments , 'user_profile': user_profile })




@login_required(login_url='signin')
def lecture_detail(request , slug):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    user_following_list = []
    feed = []
    user_following = FollowersCount.objects.filter(follower=request.user.username)
    for users in user_following:
        user_following_list.append(users.user)
    for usernames in user_following_list:
        feed_lists = Post.objects.filter(user=usernames)
        feed.append(feed_lists)
    feed_list = list(chain(*feed))
    all_users = User.objects.all()
    user_following_all = []
    for user in user_following:
        user_list = User.objects.get(username=user.user)
        user_following_all.append(user_list)

    post = get_object_or_404(Post ,slug=slug)

    lessons_list = [1,]
    lessons_feed = []
    purchased_lessons = BuyLesson.objects.filter(username=request.user.username)
    for posts in purchased_lessons:
        lessons_list.append(posts.post_id)
    for posts in lessons_list:
        feed_lists = Post.objects.filter(id=posts)
        lessons_feed.append(feed_lists)
    purchased_lessons_list = list(chain(*lessons_feed))


    if BuyLesson.objects.filter(username=request.user.username, post_id=post.id).first():
        button_text = 'yes'
    else:
        button_text = 'no'
        
    return render(request, 'main/lesson-detail.html', {'post' : post , 'user_profile': user_profile, 'posts':feed_list , 'text' : button_text})


@login_required(login_url='signin')
def lecture_progress(request , slug):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    user_following_list = []
    feed = []
    user_following = FollowersCount.objects.filter(follower=request.user.username)
    for users in user_following:
        user_following_list.append(users.user)
    for usernames in user_following_list:
        feed_lists = Post.objects.filter(user=usernames)
        feed.append(feed_lists)
    feed_list = list(chain(*feed))
    all_users = User.objects.all()
    user_following_all = []
    for user in user_following:
        user_list = User.objects.get(username=user.user)
        user_following_all.append(user_list)

    post = get_object_or_404(Post ,slug=slug)

    lessons_list = [1,]
    lessons_feed = []
    purchased_lessons = BuyLesson.objects.filter(username=request.user.username)
    for posts in purchased_lessons:
        lessons_list.append(posts.post_id)
    for posts in lessons_list:
        feed_lists = Post.objects.filter(id=posts)
        lessons_feed.append(feed_lists)
    purchased_lessons_list = list(chain(*lessons_feed))

    if LikePost.objects.filter(username=request.user.username, post_id=post.id).first():
        like_filter = 'yes'
    else:
        like_filter = 'no'



    if BuyLesson.objects.filter(username=request.user.username, post_id=post.id).first():
        button_text = 'yes'
    else:
        button_text = 'no'

    comments = Comment.objects.filter(post_id=post.id).values()

    replys = Reply.objects.filter(username=request.user.username).values()


    
    
        
    return render(request, 'main/lecture.html', {'post' : post , 'user_profile': user_profile, 'posts':feed_list , 'text' : button_text , 'like':like_filter , 'comments':comments , 'replys':replys})








@login_required(login_url='signin')
def lesson_detail(request , slug):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    user_following_list = []
    feed = []
    user_following = FollowersCount.objects.filter(follower=request.user.username)
    for users in user_following:
        user_following_list.append(users.user)
    for usernames in user_following_list:
        feed_lists = Post.objects.filter(user=usernames)
        feed.append(feed_lists)
    feed_list = list(chain(*feed))
    all_users = User.objects.all()
    user_following_all = []
    for user in user_following:
        user_list = User.objects.get(username=user.user)
        user_following_all.append(user_list)

    post = get_object_or_404(Post ,slug=slug )

    lessons_list = [1,]
    lessons_feed = []
    purchased_lessons = BuyLesson.objects.filter(username=request.user.username)
    for posts in purchased_lessons:
        lessons_list.append(posts.post_id)
    for posts in lessons_list:
        feed_lists = Post.objects.filter(id=posts)
        lessons_feed.append(feed_lists)
    purchased_lessons_list = list(chain(*lessons_feed))

    if BuyLesson.objects.filter(username=request.user.username, post_id=posts).first():
        button_text = 'yes'
    else:
        button_text = 'no'
        
    return render(request, 'main/lesson-detail.html', {'post' : post , 'user_profile': user_profile, 'posts':feed_list, 'text' : button_text , 'other':purchased_lessons_list})



    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    user_following_list = []
    feed = []
    user_following = FollowersCount.objects.filter(follower=request.user.username)
    for users in user_following:
        user_following_list.append(users.user)
    for usernames in user_following_list:
        feed_lists = Post.objects.filter(user=usernames)
        feed.append(feed_lists)
    feed_list = list(chain(*feed))
    all_users = User.objects.all()
    user_following_all = []
    for user in user_following:
        user_list = User.objects.get(username=user.user)
        user_following_all.append(user_list)

    post = get_object_or_404(Post ,slug=slug )

    lessons_list = [1,]
    lessons_feed = []
    purchased_lessons = BuyLesson.objects.filter(username=request.user.username)
    for posts in purchased_lessons:
        lessons_list.append(posts.post_id)
    for posts in lessons_list:
        feed_lists = Post.objects.filter(id=posts)
        lessons_feed.append(feed_lists)
    purchased_lessons_list = list(chain(*lessons_feed))

    if BuyLesson.objects.filter(username=request.user.username, post_id=posts).first():
        button_text = 'yes'
    else:
        button_text = 'no'
        
    return render(request, 'main/lesson-page.html', {'post' : post , 'user_profile': user_profile, 'posts':feed_list, 'text' : button_text , 'other':purchased_lessons_list})




@login_required(login_url='signin')
def purchased_lessons(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)



    lessons_list = [1,]
    lessons_feed = []
    purchased_lessons = BuyLesson.objects.filter(username=request.user.username)
    for posts in purchased_lessons:
        lessons_list.append(posts.post_id)
    for posts in lessons_list:
        feed_lists = Post.objects.filter(id=posts)
        lessons_feed.append(feed_lists)
    purchased_lessons_list = list(chain(*lessons_feed))
    if BuyLesson.objects.filter(username=request.user.username, post_id=posts).first():
        button_text = 'yes'
    else:
        button_text = 'no'



    return render(request, 'main/purchased-lessons.html', {'user_profile': user_profile, 'post':purchased_lessons_list, 'text' : button_text,})




    

@login_required(login_url='signin')
def get_premium(request):

    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)

    if request.method == 'POST':
        users = request.user
        names = request.POST.get('name')
        emails = request.POST.get('email')
        years = request.POST.get('year')
        data = GetPremium(user=users , name=names ,  email=emails , year=years)
        data.save()
        # return redirect(reverse('main'))

    return render(request, 'main/premium.html' , {'user_profile': user_profile})


@login_required(login_url='signin')
def wallet_recharge(request):

    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)


    all_requests = RechargeRequest.objects.all()
    user_requests = all_requests.filter(username=request.user.username).values()




    if request.method == 'POST':
        usernames = request.user
        amounts = request.POST.get('amount')
        sender_numbers = request.POST.get('sender')
        wallet_numbers = request.POST.get('wallet')
        data = RechargeRequest(username=usernames , amount=amounts ,  sender_number=sender_numbers , wallet_number=wallet_numbers)
        data.save()
        return redirect('/wallet/requests')



    return render(request, 'money/wallet-recharge.html' , {'user_profile': user_profile , 'requests' : user_requests})




@login_required(login_url='signin')
def wallet_requests(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    all_requests = RechargeRequest.objects.all()
    user_requests = all_requests.filter(username=request.user.username).values()

    return render(request, 'money/wallet-requests.html' , {'user_profile': user_profile , 'requests':user_requests})


@login_required(login_url='signin')
def money_error(request):

    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)


    return render(request, 'money/money-error.html' , {'user_profile': user_profile})





@login_required(login_url='signin')
def dashboard(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    user_following_list = []
    feed = []
    user_following = FollowersCount.objects.filter(follower=request.user.username)

    for users in user_following:
        user_following_list.append(users.user)

    for usernames in user_following_list:
        feed_lists = Post.objects.filter(user=usernames)
        feed.append(feed_lists)

    feed_list = list(chain(*feed))




    all_profiles = Profile.objects.all()

    questions = Comment.objects.filter(commented_to=request.user.username).values()




    if request.method == 'POST':

        users = request.user
        titles = request.POST.get('title')
        captions = request.POST.get('caption')
        subjects = user_profile.subject
        years = request.POST.get('year')
        prices = request.POST.get('price')
        teacher_name = user_profile.name
        teacher_img = user_profile.image



        attach1_type = request.POST.get('attach1_type')
        attach1_link = request.POST.get('attach1_link')

        attach2_type = request.POST.get('attach2_type')
        attach2_link = request.POST.get('attach2_link')

        attach3_type = request.POST.get('attach3_type')
        attach3_link = request.POST.get('attach3_link')




        if len(request.FILES) != 0:
            clip = request.FILES['video']
            thumbnails = request.FILES['thumbnail']


        data = Post(user=users , title=titles ,  caption=captions , subject=subjects ,  year=years ,  video=clip , image=thumbnails , price=prices , teacher_name=teacher_name , teacher_img=teacher_img , attach1_type=attach1_type , attach1_link=attach1_link , attach2_type=attach2_type , attach2_link=attach2_link , attach3_type=attach3_type , attach3_link=attach3_link)

        data.save()
        return redirect("/dashboard#upload")


    return render(request, 'main/dashboard.html', {'user_profile': user_profile, 'posts':feed_list ,'profiles' :all_profiles , 'questions':questions})



@login_required(login_url='signin')
def delete_lesson(request):
    if request.method == 'POST':
        post_id = request.POST['post-id']


        delete_post = Post.objects.get(id=post_id)
        delete_post.delete()
        return redirect('/dashboard#videos')

    else:
        return redirect('/dashboard#videos')
    






@login_required(login_url='signin')
def dashboard_profiles(request):
    if request.method == 'POST':
        student = request.POST['student']
        money = request.POST['money']

        new_wallet = int(money)

        studentt = Profile.objects.get(id_user=student)
        studentt.money = new_wallet

        studentt.save()


        print("done")
        print(studentt.money)




        return redirect('/dashboard#students')

    else:
        return redirect('/dashboard#students')





@login_required(login_url='signin')
def dashboard_lesson(request , slug):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    user_following_list = []
    feed = []
    user_following = FollowersCount.objects.filter(follower=request.user.username)
    for users in user_following:
        user_following_list.append(users.user)
    for usernames in user_following_list:
        feed_lists = Post.objects.filter(user=usernames)
        feed.append(feed_lists)
    feed_list = list(chain(*feed))
    all_users = User.objects.all()
    user_following_all = []
    for user in user_following:
        user_list = User.objects.get(username=user.user)
        user_following_all.append(user_list)
    new_suggestions_list = [x for x in list(all_users) if (x not in list(user_following_all))]
    current_user = User.objects.filter(username=request.user.username)
    final_suggestions_list = [x for x in list(new_suggestions_list) if ( x not in list(current_user))]
    random.shuffle(final_suggestions_list)
    username_profile = []
    username_profile_list = []
    for users in final_suggestions_list:
        username_profile.append(users.id)
    for ids in username_profile:
        profile_lists = Profile.objects.filter(id_user=ids)
        username_profile_list.append(profile_lists)
    suggestions_username_profile_list = list(chain(*username_profile_list))
    post = get_object_or_404(Post ,slug=slug )
    return render(request, 'main/dashboard-lesson.html', {'post' : post , 'user_profile': user_profile, 'posts':feed_list, 'suggestions_username_profile_list': suggestions_username_profile_list[:4]})








@login_required(login_url='signin')
def activity(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)

    lessons_list = [1,]
    lessons_feed = []
    purchased_lessons = BuyLesson.objects.filter(username=request.user.username)
    for posts in purchased_lessons:
        lessons_list.append(posts.post_id)
    for posts in lessons_list:
        bought_lists = Post.objects.filter(id=posts)
        lessons_feed.append(bought_lists)
    purchased_lessons_list = list(chain(*lessons_feed))
    if BuyLesson.objects.filter(username=request.user.username, post_id=posts).first():
        button_text = 'yes'
    else:
        button_text = 'no'




    user_following_list = []
    feed = []

    user_following = FollowersCount.objects.filter(follower=request.user.username)

    for users in user_following:
        user_following_list.append(users.user)

    for usernames in user_following_list:
        feed_lists = Post.objects.filter(user=usernames)
        feed.append(feed_lists)

    feed_list = list(chain(*feed))


    





    all_posts= Post.objects.all()






    return render(request, 'main/lessons.html', {'user_profile': user_profile, 'posts':feed_list , 'all' :posts ,'bought':purchased_lessons_list, 'text' : button_text,  'all' : all_posts,})




@login_required(login_url='signin')
def upload(request):

    if request.method == 'POST':
        user = request.user.username
        image = request.FILES.get('image_upload')
        caption = request.POST['caption']
        if len(request.FILES) != 0:
            clip = request.FILES['clip']

        new_post = Post.objects.create(user=user, image=image, caption=caption , video=clip)
        new_post.save()

        return redirect('/dashboard#upload-video')
    else:
        return redirect('/dashboard#upload-video')

@login_required(login_url='signin')
def search(request):

    
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)

    user_following_list = []
    feed = []

    user_following = FollowersCount.objects.filter(follower=request.user.username)

    for users in user_following:
        user_following_list.append(users.user)

    for usernames in user_following_list:
        feed_lists = Post.objects.filter(user=usernames)
        feed.append(feed_lists)

    feed_list = list(chain(*feed))

    # user suggestion starts
    all_users = User.objects.all()
    user_following_all = []

    for user in user_following:
        user_list = User.objects.get(username=user.user)
        user_following_all.append(user_list)
    
    new_suggestions_list = [x for x in list(all_users) if (x not in list(user_following_all))]
    current_user = User.objects.filter(username=request.user.username)
    final_suggestions_list = [x for x in list(new_suggestions_list) if ( x not in list(current_user))]
    random.shuffle(final_suggestions_list)

    username_profile = []
    username_profile_list = []

    for users in final_suggestions_list:
        username_profile.append(users.id)

    for ids in username_profile:
        profile_lists = Profile.objects.filter(id_user=ids)
        username_profile_list.append(profile_lists)

    suggestions_username_profile_list = list(chain(*username_profile_list))

    if request.method == 'POST':
        username = request.POST['username']
        username_object = User.objects.filter(username__icontains=username)

        username_profile = []
        username_profile_list = []

        for users in username_object:
            username_profile.append(users.id)

        for ids in username_profile:
            profile_lists = Profile.objects.filter(id_user=ids)
            username_profile_list.append(profile_lists)
        
        username_profile_list = list(chain(*username_profile_list))
    return render(request, 'search.html', {'user_profile': user_profile, 'username_profile_list': username_profile_list,  'posts':feed_list, 'suggestions_username_profile_list': suggestions_username_profile_list[:4]})



@login_required(login_url='signin')
def search_page(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)

    user_following_list = []
    feed = []

    user_following = FollowersCount.objects.filter(follower=request.user.username)

    for users in user_following:
        user_following_list.append(users.user)

    for usernames in user_following_list:
        feed_lists = Post.objects.filter(user=usernames)
        feed.append(feed_lists)

    feed_list = list(chain(*feed))

    # user suggestion starts
    all_users = User.objects.all()
    user_following_all = []

    for user in user_following:
        user_list = User.objects.get(username=user.user)
        user_following_all.append(user_list)
    
    new_suggestions_list = [x for x in list(all_users) if (x not in list(user_following_all))]
    current_user = User.objects.filter(username=request.user.username)
    final_suggestions_list = [x for x in list(new_suggestions_list) if ( x not in list(current_user))]
    random.shuffle(final_suggestions_list)

    username_profile = []
    username_profile_list = []

    for users in final_suggestions_list:
        username_profile.append(users.id)

    for ids in username_profile:
        profile_lists = Profile.objects.filter(id_user=ids)
        username_profile_list.append(profile_lists)

    suggestions_username_profile_list = list(chain(*username_profile_list))


    return render(request, 'main/search-page.html', {'user_profile': user_profile, 'posts':feed_list, 'suggestions_username_profile_list': suggestions_username_profile_list[:4]})



@login_required(login_url='signin')
def charge_wallet_code(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)

    return render(request, 'money/code-charge.html', {'user_profile': user_profile})




@login_required(login_url='signin')
def code_charge(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)


    if request.method == 'POST':
        code = request.POST['code']

        if Code.objects.filter(code_id=code).first():
            valid_code = Code.objects.get(code_id=code)
            valid_code_money = valid_code.money
            user_profile.money = user_profile.money + valid_code_money



            user_profile.save()
            user_object.save()
            text = 'yes'
            new_activity = Activity.objects.create(username=request.user.username , activity_type='charge' ,purchase_type='code' , wallet=user_profile.money , money=valid_code_money)
            valid_code.delete()
            print(user_profile.money)
        else:
            text = 'no'

    return render(request, 'money/code-charge-request.html', {'user_profile': user_profile, 'text' : text,})


@login_required(login_url='signin')
def lesson_code_charge(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)


    if request.method == 'POST':
        code = request.POST['code']
        post_id = request.POST['post-id']
        post_price = request.POST['price']
        post = Post.objects.get(id=post_id)

        if Code.objects.filter(code_id=code).first():
            valid_code = Code.objects.get(code_id=code)
            valid_code_money = valid_code.money
            user_profile.money = user_profile.money + valid_code_money



            user_profile.save()
            user_object.save()
            new_activity = Activity.objects.create(username=request.user.username , activity_type='charge' ,purchase_type='code' , wallet=user_profile.money , money=valid_code_money)
            valid_code.delete()

            lesson_price = post_price
            
            if user_profile.money < post.price:
                return redirect('/purchase-error')
            else:
                new_buy = BuyLesson.objects.create(post_id=post_id, username=request.user.username)
                new_buy.save()
                lesson_price = post.price
                user_profile.money = user_profile.money-lesson_price
                user_profile.no_of_buys = user_profile.no_of_buys+1

                post.no_of_buys = post.no_of_buys+1
                post.save()
                user_profile.save()
                new_activity = Activity.objects.create(username=request.user.username , activity_type='purchase' ,purchase_type='code' , wallet=user_profile.money , lesson_name=post.title , money=lesson_price)
                
                return redirect('/lessons/progress/'+post_id)
        else:
            text = 'no'
            return render(request, 'money/code-charge-request.html', {'user_profile': user_profile, 'text' : text,})
    else:
        return redirect('/lessons')



@login_required(login_url='signin')
def purchase_lesson(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)

    if request.method == 'POST':
        username = request.POST['buyer']
        post_id = request.POST['post']


        post = Post.objects.get(id=post_id)
        buy_filter = BuyLesson.objects.filter(post_id=post_id, username=username).first()
        text = 'buy'

        if buy_filter == None:

            lesson_price =post.price
            if user_profile.money < post.price:
               return redirect('/purchase-error')
            else:
               new_buy = BuyLesson.objects.create(post_id=post_id, username=username)
               new_buy.save()
               lesson_price = post.price
               user_profile.money = user_profile.money-lesson_price
               user_profile.no_of_buys = user_profile.no_of_buys+1
               post.no_of_buys = post.no_of_buys+1
               post.save()

               user_profile.save()
               new_activity = Activity.objects.create(username=request.user.username , activity_type='purchase' ,purchase_type='wallet' , wallet=user_profile.money , lesson_name=post.title , money=lesson_price)
        return redirect('/lessons/progress/'+post_id)
    else:
        return redirect('/lessons/'+ post_id)






@login_required(login_url='signin')
def purchased_lessons(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)



    lessons_list = [1,]
    lessons_feed = []
    purchased_lessons = BuyLesson.objects.filter(username=request.user.username)
    for posts in purchased_lessons:
        lessons_list.append(posts.post_id)
    for posts in lessons_list:
        feed_lists = Post.objects.filter(id=posts)
        lessons_feed.append(feed_lists)
    purchased_lessons_list = list(chain(*lessons_feed))
    if BuyLesson.objects.filter(username=request.user.username, post_id=posts).first():
        button_text = 'yes'
    else:
        button_text = 'no'



    return render(request, 'main/purchased-lessons.html', {'user_profile': user_profile, 'post':purchased_lessons_list, 'text' : button_text,})







@login_required(login_url='signin')
def like_post(request):
    username = request.user.username
    post_id = request.GET.get('post_id')

    post = Post.objects.get(id=post_id)

    like_filter = LikePost.objects.filter(post_id=post_id, username=username).first()

    if like_filter == None:
        new_like = LikePost.objects.create(post_id=post_id, username=username)
        new_like.save()
        post.no_of_likes = post.no_of_likes+1
        post.save()
        return redirect('/lessons#lessons')
    else:
        like_filter.delete()
        post.no_of_likes = post.no_of_likes-1
        post.save()
        return redirect('/lessons#lessons')


@login_required(login_url='signin')
def like_lesson(request):
    username = request.user.username
    post_id = request.GET.get('post_id')

    post = Post.objects.get(id=post_id)

    like_filter = LikePost.objects.filter(post_id=post_id, username=username).first()

    if like_filter == None:
        new_like = LikePost.objects.create(post_id=post_id, username=username)
        new_like.save()
        post.no_of_likes = post.no_of_likes+1
        post.save()
        return redirect('/lessons/progress/'+post_id)
    else:
        like_filter.delete()
        post.no_of_likes = post.no_of_likes-1
        post.save()
        return redirect('/lessons/progress/'+post_id)


@login_required(login_url='signin')
def comment(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    user_image = user_profile.image

    if request.method == 'POST':
        username = request.POST['user']
        post_id = request.POST['post']
        comment =request.POST['comment']
        commented_to =request.POST['commented-to']
        username_name = user_profile.name
        
        post = Post.objects.get(id=post_id)

        new_comment = Comment.objects.create(post_id=post_id, username=username , comment=comment, commented_to=commented_to , username_image=user_image , username_name=username_name)
        new_comment.save()
        post.no_of_comments = post.no_of_comments+1
        post.save()

        return redirect('/lessons/progress/'+post_id +'#comments')
    else:
        return redirect('/lessons/progress/'+ post_id+'#comments')
    




@login_required(login_url='signin')
def reply(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    user_image = user_profile.image

    if request.method == 'POST':
        username = request.POST['user']
        comment_id = request.POST['comment']
        reply = request.POST['reply']
        comment_text = request.POST['text']

        replayed = request.POST['replayed-to']
        username_name = user_profile.name
        
        comment = Comment.objects.get(comment_id=comment_id)


        new_reply = Reply.objects.create(comment_id=comment_id,  username=username , reply=reply, replyed_to=replayed , comment_text=comment_text , username_image=user_image , username_name=username_name)
        new_reply.save()
        comment.no_of_replys = comment.no_of_replys+1
        comment.save()

        return redirect('/dashboard#questions')
    else:
        return redirect('/dashboard#questions')




@login_required(login_url='signin')
def profile(request, pk):

    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)


    profile_object = User.objects.get(username=pk)
    profile = Profile.objects.get(user=profile_object)
    user_posts = Post.objects.filter(user=pk)
    user_post_length = len(user_posts)

    follower = request.user.username
    user = pk

    if FollowersCount.objects.filter(follower=follower, user=user).first():
        button_text = 'Unfollow'
    else:
        button_text = 'Follow'

    user_followers = len(FollowersCount.objects.filter(user=pk))
    user_following = FollowersCount.objects.filter(follower=pk).first()

    context = {
        'user_object': user_object,
        'user_profile': user_profile,
        'profile': profile,
        'profile_object': profile_object,
        'user_posts': user_posts,
        'user_post_length': user_post_length,
        'button_text': button_text,
        'user_followers': user_followers,
        'user_following': user_following,
    }
    return render(request, 'main/my-profile.html', context)

@login_required(login_url='signin')
def follow(request):
    if request.method == 'POST':
        follower = request.POST['follower']
        user = request.POST['user']

        if FollowersCount.objects.filter(follower=follower, user=user).first():
            delete_follower = FollowersCount.objects.get(follower=follower, user=user)
            delete_follower.delete()
            return redirect('/profile/'+user)
        else:
            new_follower = FollowersCount.objects.create(follower=follower, user=user)
            new_follower.save()
            return redirect('/profile/'+user)
    else:
        return redirect('/')




@login_required(login_url='signin')
def settings(request):
    user_profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        
        if request.FILES.get('image') == None:
            image = user_profile.image
            school = request.POST['school']
            phone = request.POST['phone']
            year = request.POST['year']
            name = request.POST['name']
            public = request.POST['public']
            location = request.POST['location']

            user_profile.image = image
            user_profile.school = school
            user_profile.phone = phone
            user_profile.year = year
            user_profile.name = name
            user_profile.public = public
            user_profile.location = location
            user_profile.save()
            return redirect('/settings')
        if request.FILES.get('image') != None:
            image = request.FILES.get('image')
            school = request.POST['school']
            phone = request.POST['phone']
            year = request.POST['year']
            name = request.POST['name']
            public = request.POST['public']
            location = request.POST['location']

            user_profile.image = image
            user_profile.school = school
            user_profile.phone = phone
            user_profile.year = year
            user_profile.name = name
            user_profile.public = public
            user_profile.location = location
            user_profile.save()
        
        return redirect('/settings')
    return render(request, 'accounts/edit-profile.html', {'user_profile': user_profile})


@login_required(login_url='signin')
def settings_teacher(request):
    user_profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        
        if request.FILES.get('image') == None:
            image = user_profile.image
            school = request.POST['school']
            phone = request.POST['phone']
            name = request.POST['name']
            location = request.POST['location']

            user_profile.image = image
            user_profile.school = school
            user_profile.phone = phone
            user_profile.name = name
            user_profile.location = location
            user_profile.save()
        if request.FILES.get('image') != None:
            image = request.FILES.get('image')
            school = request.POST['school']
            phone = request.POST['phone']
            name = request.POST['name']
            location = request.POST['location']

            user_profile.image = image
            user_profile.school = school
            user_profile.phone = phone
            user_profile.name = name
            user_profile.location = location
            user_profile.save()
        
        return redirect('/settings-teacher')
    return render(request, 'accounts/edit-profile-teacher.html', {'user_profile': user_profile})



@login_required(login_url='signin')
def setup_acount(request):
    user_profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        
        if request.FILES.get('image') == None:
            image = user_profile.image
            school = request.POST['school']
            phone = request.POST['phone']
            year = request.POST['year']
            name = request.POST['name']
            public = request.POST['public']
            location = request.POST['location']

            user_profile.image = image
            user_profile.school = school
            user_profile.phone = phone
            user_profile.year = year
            user_profile.name = name
            user_profile.public = public
            user_profile.location = location
            user_profile.save()
        if request.FILES.get('image') != None:
            image = request.FILES.get('image')
            school = request.POST['school']
            phone = request.POST['phone']
            year = request.POST['year']
            name = request.POST['name']
            public = request.POST['public']
            location = request.POST['location']

            user_profile.image = image
            user_profile.school = school
            user_profile.phone = phone
            user_profile.year = year
            user_profile.name = name
            user_profile.public = public
            user_profile.location = location
            user_profile.save()
        
        return redirect('/')
    return render(request, 'accounts/setup-account.html', {'user_profile': user_profile})



@login_required(login_url='signin')
def setup_acount_teacher(request):
    user_profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        
        if request.FILES.get('image') == None:
            image = user_profile.image
            school = request.POST['school']
            phone = request.POST['phone']
            subject = request.POST['subject']
            name = request.POST['name']
            # public = request.POST['public']
            location = request.POST['location']

            user_profile.image = image
            user_profile.school = school
            user_profile.phone = phone
            user_profile.subject = subject
            user_profile.name = name
            user_profile.location = location

            user_profile.public = 'True'
            user_profile.year == 'none'
            user_profile.save()
        if request.FILES.get('image') != None:
            image = request.FILES.get('image')
            school = request.POST['school']
            phone = request.POST['phone']
            subject = request.POST['subject']
            name = request.POST['name']
            # public = request.POST['public']
            location = request.POST['location']

            user_profile.image = image
            user_profile.school = school
            user_profile.phone = phone
            user_profile.subject = subject
            user_profile.name = name
            user_profile.location = location

            user_profile.public = 'True'
            user_profile.year == 'none'
            user_profile.save()
        
        return redirect('/')
    return render(request, 'accounts/setup-account-teacher.html', {'user_profile': user_profile})





def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        teacher = request.POST['teacher']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                #log user in and redirect to settings page
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)

                #create a Profile object for the new user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                if teacher == 'True':
                    return redirect('setup-account-teacher')
                else: 
                    return redirect('setup-account')
        else:
            messages.info(request, 'Password Not Matching')
            return redirect('signup')
        
    else:
        return render(request, 'accounts/signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)



        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('signin')

    else:
        return render(request, 'accounts/login.html')
    

@login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    return redirect('signin')