def my_abs(x):
    if type(x) == int:
        print('정수형') 
    elif type(x) == float:
        print('실수형')
    elif type(x) == complex:
        print('복소수형')
    else:
        print('기타등등')