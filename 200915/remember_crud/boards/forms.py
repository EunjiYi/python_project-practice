from django import forms
from .models import Board

# class BoardForm(forms.Form):
#     title = forms.CharField(max_length=50)
#     content = forms.CharField(widget=forms.Textar)

class BoardForm(forms.ModelForm):
    title = forms.CharField(
        label = '제목',
        widget=forms.TextInput(
            attrs={
                "placeholder":"제목을 입력하세요.", 
                "class": "my-class",
            }
        )
    )
    class Meta: #Mata 클래스의 상위 클래스의 정보를 입력하는 클래스이다. 
        model = Board
        #fields = ['title',] #특정 항목만 받고 싶을 때
        fields = '__all__' #다 받고 싶을 때



