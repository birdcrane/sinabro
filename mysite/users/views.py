from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.db import IntegrityError
# Create your views here.
# 회원가입
def signup(request):
    if request.method == 'POST':
        try:
            if request.POST['password1'] == request.POST['password2']:
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1'],
                    email=request.POST['email'],
                )
                auth.login(request, user)
                return redirect('/users/login')
            else:
                return render(request, 'users/signup.html', {'error': '비밀번호가 일치하지 않습니다.'})
        except ValueError:
            # 필드가 비어있는 경우 처리
            return render(request, 'users/signup.html', {'error': '모든 필드를 채워주세요.'})
        except IntegrityError:
            # 이미 등록된 사용자 이름인 경우 처리
            return render(request, 'users/signup.html', {'error': '이미 사용 중인 사용자 이름입니다.'})
    else:
        form = UserCreationForm
        return render(request, 'users/signup.html', {'form' :form})
