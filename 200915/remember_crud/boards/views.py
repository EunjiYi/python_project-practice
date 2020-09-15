from django.shortcuts import render, redirect

from .models import Board
from .forms import BoardForm

def index(request):
    # DB 에서 데이터를 파이썬으로 들고옴.
    datas = Board.objects.all()

    context = {
        'datas': datas
    }
    return render(request, 'boards/index.html', context)


def variable(request, name):
    context = {
        'vari_name': name
    }
    return render(request, 'boards/vari.html', context)


def detail(request, pk):
    # 어떤 데이터를 넘겨줘야 하지????? 누가 눌렸는데???
    # 정보가 필요해!!!!!!!!
    # pk 가 있으면 해당 Pk 로 데이터를 찾을 수 있다!!!!
    data = Board.objects.get(pk=pk)
    print(data) # 하나의 object 만 반환.
    context = {
        'data': data,
    }
    return render(request, 'boards/detail.html', context)


def create(request):
    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save()
            return redirect('boards:detail', board.pk)

        # forms.Form을 상속받아서 사용하는 경우
        # if form.is_valid():
        #     data = form.cleaned_data
        #     board = Board()
        #     board.title = data.get('title')
        #     board.content = data.get('content')
        #     board.save()
        #     return redirect('boards:detail', board.pk)
    else:
        form = BoardForm()
    context = {
        'form': form,
    }
    return render(request, 'boards/form.html', context)


def update(request, id):
    board = Board.objects.get(pk=id)

    if request.method == "POST":
        form = BoardForm(request.POST, instance=board) # 수정되는 값을 꼭 instance에 넣어줘야한다. 안그러면 수정을 해도 새로운 게시글로 생긴다.
        if form.is_valid():
            data = form.save()
            return redirect('boards:detail', data.pk)
    else:
        form = BoardForm(instance=board)
    context = {
        'form': form,
    }
    return render(request, 'boards/form.html', context)


def delete(request, id):
    board = Board.objects.get(id=id)
    if request.method == "POST":
        board.delete()
        return redirect('boards:index')
    # 입력받은 id도 board.pk 와 같기 때문에 어떤 값을 넣어도 된다.
    return redirect('boards:detail', id)
