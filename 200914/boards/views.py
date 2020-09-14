from django.shortcuts import render, redirect

from .models import Board

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
    print(request.POST)
    if request.method == "POST":
        print('DB에 저장 플리즈...')
        # 1 번째 방법
        board = Board()
        board.title = request.POST.get('title')
        board.content = request.POST.get('content')
        board.save()

        # 2 번째 방법
        # board = Board(title=request.POST.get('title'), content=request.POST.get('content'))
        # board.save()

        # 3 번째 방법
        # Board.objects.create(title=request.POST.get('title'), content=request.POST.get('content'))
        
        return redirect('boards:detail', board.pk)
    else: 
        print('입력창을 보여주세요.. ')

    return render(request, 'boards/new.html')


def update(request, id):
    # DB 에서 값을 가지고 와야 하는데...
    # 글 하나를 가져와야 하는데... 뭘 가져오면 되지???
    board = Board.objects.get(pk=id)
    if request.method == "POST":
        board.title = request.POST.get('title')
        board.content = request.POST.get('content')
        board.save()
        return redirect('boards:detail', board.pk)
    else: 
        context = {
            'board': board,
        }
    return render(request, 'boards/edit.html', context)


def delete(request, id):
    board = Board.objects.get(id=id)
    if request.method == "POST":
        board.delete()
        return redirect('boards:index')
    # 입력받은 id도 board.pk 와 같기 때문에 어떤 값을 넣어도 된다.
    return redirect('boards:detail', id)
