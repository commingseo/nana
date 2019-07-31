#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import auth
from random import *
#from . import menu_img

# Create your views here.
def addPath(x):
    return "http://halftone-project-nwsqa.run.goorm.io/static/img/" + x

def home(request):
    return render(request, 'index.html')

#회원가입 메소드
def join(request):
        if request.method == 'POST':
            if request.POST['password1'] == request.POST['password2']:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('home')
        return render(request, 'join.html')
    
#로그인 메소드
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'UserName or Password is incorrect.'})
    else:
        return render(request, 'login.html')
    
#로그아웃 메소드
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'join.html')

def breakfast(request): 
    menu_img = list(map(addPath,[
             '1/Serial.jpg',
             '1/benddo.png',
             '1/toast.jpg',
             '1/egg.jpg',
             '1/salad.jpg',
             '1/searice.jpg',
             '1/riceberger.jpg',
             '1/water.jpg',
             '1/soup.jpg', 
             '1/homerice.jpg',
             '1/3m.jpg'
            ]))

    breakfast = {
            0 : '시리얼', 
            1 : '도시락', 
            2 : '토스트', 
            3 : '계란후라이', 
            4 : '샐러드', 
            5 : '김밥',
            6 : '밥버거',
            7 : '물',
            8 : '스프',
            9 : '가정식', 
            10 : '3분요리',
            }
    rand = randrange(len(menu_img))
    
    url = menu_img[rand]
    
    print(url)
    return render(request, 'breakfast.html', {'breakfast' : breakfast[rand], 'url' : url})


def lunch(request):
    menu_img = list(map(addPath,[
            '2/Britto.jpg',
            '2/Bulgogi.jpg',
            '2/Champon.jpg',
            '2/Kimchistew.jpg',
            '2/Tteokbokki.jpg',
            '2/bibimcoldnoodle.jpg',
            '2/blacknoodle.jpg',
            '2/bread.jpg',
            '2/friedice.jpg', 
            '2/hamberger.png',
            '2/hotnoodle.jpg',
            '2/icenoodle.jpg',
            '2/jjageuli.jpg',
            '2/misostew.jpg',
            '2/pasta.jpg',
            '2/pizza.jpg',
            '2/porkden.jpg',
            '2/ramen.jpg',
            '2/ricesoup.jpg',
            '2/searice.jpg',
            '2/spicypork.jpg',
            '2/sushi.jpg'
            ]))

    lunch = {0 : '브리또', 
            1 : '불고기', 
            2 : '짬뽕', 
            3 : '김치찌개', 
            4 : '떡볶이', 
            5 : '비빔냉면',
            6 : '짜장면',
            7 :'빵',
            8 : '볶음밥',
            9 : '햄버거', 
            10 : '우동',
            11 : '냉면',
            12 : '짜글이',
            13 : '된장찌개',
            14 : '파스타',
            15 : '피자',
            16 : '돈까스',
            17 : '라면',
            18 : '국밥',
            19 : '김밥',
            20 : '제육볶음',
            21 : '초밥'
            }
    rand = randrange(len(menu_img))
    
    url = menu_img[rand]
    
    print(url)
    return render(request, 'lunch.html', {'lunch' : lunch[rand], 'url' : url})

def dinner(request):
    menu_img = list(map(addPath,[
        '3/Champon.jpg',
        '3/Chicken.png',
        '3/ChickenRibs.jpg',
        '3/Giblet.png',
        '3/Kimchistew.gif',
        '3/Ricebowls.jpg',
        '3/SoybeanPaste Stew.jpg',
        '3/Tteokbokki.jpg',
        '3/benddo.png',
        '3/blacknoodle.jpg',
        '3/gut.jpg',
        '3/hamberger.png',
        '3/homerice.jpg',
        '3/jjageuli.jpg',
        '3/pasta.jpg',
        '3/pizza.jpg',
        '3/porkbelly.jpg',
        '3/porkden.jpg',
        '3/ramen.jpg',
        '3/steak.jpg',
        '3/sushi.jpg'
        ]))
        
    dinner = {0 : '짬뽕',
              1 : '치킨',
              2 : '닭갈비',
              3 : '곱창',
              4 : '김치찌개',
              5 : '덮밥',
              6 : '된장찌개',
              7 : '떡볶이',
              8 : '도시락',
              9 : '짜장면',
              10 : '막창',
              11 : '햄버거',
              12 : '집밥',
              13 : '짜그리',
              14 : '파스타',
              15 : '피자',
              16 : '삼겹살',
              17 : '돈까스',
              18 : '라면',
              19 : '스테이크',
              20 : '초밥'
             }
    
    rand = randrange(len(menu_img))
    url = menu_img[rand]
    
    print(url)
    return render(request, 'dinner.html', {'dinner' : dinner[rand], 'url' : url})


def midnightsnack(request):
    menu_img = list(map(addPath,['4/pizza.jpg',
                '4/Chicken.jpg',
                '4/gut.jpg'
               ]))
                
    midnightsnack = {
        0 : '피자',
        1 : '치킨',
        2 : '곱창'
    }
    rand = randrange(len(menu_img))
    
    url = menu_img[rand]
    
    print(url)
    return render(request, 'midnightsnack.html', {'midnightsnack' : midnightsnack[rand], 'url' : url})

def ladder(request):
    return render(request,'ladder.html')

def roulette(request):
    return render(request,'roulette.html')
