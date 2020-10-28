도대체 언제까지 set과 tuple과 dictionary를 헷갈릴 것인가.

--------------



### set()

`x = set()`

> 순서 없음. 중복 없음(중복된 값 제거할 때 사용한다.). mutable(가변)

* 중괄호 사용
* 선언시에는 딕셔너리랑 구분하려고 `x = set()`으로 선언한다. `괄호만 쓰지 않고 set 생성자를 쓴다.`
* 안에 값이 있다면 그냥 바로 `x = {1, 2, 3}` 이렇게 선언해도 된다.



#### set 원소 추가

#### add

> `x.add(5)`

#### update

> dictionary의 update는 여러 값을 수정 또는 추가할 때 사용했지만, set은 중복이 자동으로 제거되기 때문에 수정이라는 느낌보다는 여러 데이터를 한 번에 추가하는 개념으로 사용한다.

> `x  = {1,2,3}`
>
> `x.update([3, 4, 5])`
>
> `print(x)` #{1, 2, 3, 4, 5}



#### set 원소 제거

#### remove

> `x.remove(3)`
>
> 만약 없으면 keyError발생

#### discard

> `x.discard(3)`
>
> 제거할 원소가 없어도 에러 발생하지 않음.





---------------



### tuple - 리스트와 유사하지만 값을 바꿀 수 없다. 

> 순서 있다. immutable(불변). iterable(순회가능), 중복허용

- tuple(튜플)변환 - `tuple(iterable한객체)`로 tuple(튜플)로 변형할 수 있다.

```python
>>> tuple([1, 7, 5, 3, 9])
(1, 7, 5, 3, 9)

>>> tuple("abcde")
('a', 'b', 'c', 'd', 'e')
```



- list형과 비슷하지만 한 번 생성되면 값을 변경할 수 없다. **immutable(불변)**

  ```python
  my_list[0] = "Hello"  # various_list = ["Hello", 2, 3, 4, 5, 6, 7, 8, 9, 10]
  my_tuple[0] = "Hello"  # TypeError: 'tuple' object does not support item assignment
  ```

  

- #### 따라서, list는 딕셔너리의 key값으로 쓸 수 없지만, tuple은 가능하다.

  ```python
  my_dict = {my_list: "My List!"}  # TypeError: unhashable type: 'list'
  my_dict = {my_tuple: "My tuple!"}  # 정상 작동
  ```

  

#### tuple 선언

`x = ()`

하나의 원소만 있으면 튜플로 선언되지 않는다.

그래서 한 개의 원소만 있다면, 뒤에 콤마를 찍어서 tuple로 만든다.

```python
>>> h = (350)
>>> type(h)
<class 'int'>
>>> h = (350,)
>>> type(h)
<class 'tuple'>
>>> len(h)
1
```

 

---------



### dictionary

> 순서없음, 값은 중복될 수 있지만 키가 중복되면 마지막 값으로 덮어씌워짐, mutable(가변)



 immutable한 키(key)와 mutable한 값(value)으로 맵핑되어 있는 순서가 없는 집합

> 키로 사용가능: `immutable`한 것들 number, tuple
>
> 키로 사용 불가능: `mutable`한 것들 list, set, dict



#### 선언

`x = {}`

`x = dict()`



* 순서가 없어서 인덱스로 접근 불가능. 키로 접근 가능
* mutable해서 키로 접근해서 값 변경 가능.



- 여러값 수정은 update 메소드를 사용한다. 키가 없는 값이면 추가된다.

```python
>>> a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
>>> a.update({'bob':99, 'tony':99, 'kim': 30})
>>> a
{'alice': [1, 2, 3], 'bob': 99, 'tony': 99, 'suzy': 30, 'kim': 30}
```



## dictionary(딕셔너리) 변환

- 리스트 속에 리스트나 튜플, 튜플속에 리스트나 튜플의 값을 키와 value를 나란히 입력하면, 아래와 같이 dict로 변형할 수 있습니다.

```python
>>> name_and_ages = [['alice', 5], ['Bob', 13]]
>>> dict(name_and_ages)
{'alice': 5, 'Bob': 13}
>>> name_and_ages = [('alice', 5), ('Bob', 13)]
>>> dict(name_and_ages)
{'alice': 5, 'Bob': 13}
>>> name_and_ages = (('alice', 5), ('Bob', 13))
>>> dict(name_and_ages)
{'alice': 5, 'Bob': 13}
>>> name_and_ages = (['alice', 5], ['Bob', 13])
>>> dict(name_and_ages)
{'alice': 5, 'Bob': 13}
```





## dictionary(딕셔너리)의 요소 삭제

- list와 마찬가지로 del키워드를 사용한다.

```python
>>> a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
>>> del a['alice']
>>> a
{'bob': 20, 'tony': 15, 'suzy': 30}
```





##  dictionary(딕셔너리) 의 in

- dictionary의 in은 키에 한해서 동작한다.

```python
>>> 'alice' in a
True
>>> 'teacher' in a
False
>>> 'teacher' not in a
True
```



## dictionary(딕셔너리)를 읽기 쉽게 표현해주는 pprint

- pprint모듈로 dictionary를 찍어보자

```python
>>> from pprint import pprint as pp
>>> a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30,"dodo": [1,3,5,7], "mario": "pitch"}
>>> print(a)
{'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30, 'dodo': [1, 3, 5, 7], 'mario': 'pitch'}
>>> pp(a)
{'alice': [1, 2, 3],
 'bob': 20,
 'dodo': [1, 3, 5, 7],
 'mario': 'pitch',
 'suzy': 30,
 'tony': 15}
```



----------------------

--------------



## set 기타 메소드

## 8. set(집합) 연산 - 연산자

- `^` : 대칭차집합 연산자(합집합 - 교집합)

```
>>> a = {1, 2, 3, 4, 5}
>>> b = {3, 4, 5, 6, 7}
>>> c = a ^ b
>>> a
{1, 2, 3, 4, 5}
>>> b
{3, 4, 5, 6, 7}
>>> c
{1, 2, 6, 7}
```

- `|=, &=, -=, ^=` : `=` 과 조합함으로써 연산과 동시에 할당합니다.
- id 또한 변경되지 않습니다.

```
>>> a = {1, 2, 3, 4, 5}
>>> b = {3, 4, 5, 6, 7}
>>> a |= b
>>> a
{1, 2, 3, 4, 5, 6, 7}
>>> b
{3, 4, 5, 6, 7}
>>> a = {1, 2, 3, 4, 5}
>>> b = {3, 4, 5, 6, 7}
>>> id(a)
4334668040
>>> a &= b
>>> a
{3, 4, 5}
>>> id(a)
4334668040
>>> 
```

## 9. set(집합) - 연산메소드

- union - 합집합

```python
>>> a = {1, 2, 3, 4, 5}
>>> b = {3, 4, 5, 6, 7}
>>> c = a.union(b)
>>> a
{1, 2, 3, 4, 5}
>>> b
{3, 4, 5, 6, 7}
>>> c
{1, 2, 3, 4, 5, 6, 7}
```

- intersection - 교집합

```python
>>> a = {1, 2, 3, 4, 5}
>>> b = {3, 4, 5, 6, 7}
>>> c = a.intersection(b)
>>> a
{1, 2, 3, 4, 5}
>>> b
{3, 4, 5, 6, 7}
>>> c
{3, 4, 5}
```

- difference - 차집합

```python
>>> a = {1, 2, 3, 4, 5}
>>> b = {3, 4, 5, 6, 7}
>>> c = a.difference(b)
>>> a
{1, 2, 3, 4, 5}
>>> b
{3, 4, 5, 6, 7}
>>> c
{1, 2}
```

- symmetric_difference : 대칭차집합 연산자(합집합 - 교집합)

```python
>>> a = {1, 2, 3, 4, 5}
>>> b = {3, 4, 5, 6, 7}
>>> c = a.symmetric_difference(b)
>>> a
{1, 2, 3, 4, 5}
>>> b
{3, 4, 5, 6, 7}
>>> c
{1, 2, 6, 7}
```

## 10. set(집합) - 기타 메소드

- issubset : 부분집합 여부 확인

```python
>>> a = {1, 2, 3, 4, 5}
>>> b = {1, 2, 3}
>>> a.issubset(b)
False
>>> b.issubset(a)
True
```

- issuperset : issubset과 반대 superset인지 확인

```python
>>> a = {1, 2, 3, 4, 5}
>>> b = {1, 2, 3}
>>> a.issuperset(b)
True
>>> b.issuperset(a)
False
```

- isdisjoint : 교집합이 없으면 True, 있으면 False

```python
>>> a = {1, 2, 3}
>>> b = {4, 5, 6}
>>> a.isdisjoint(b)
True
>>> c = {1, 2, 3}
>>> d = {3, 4, 5}
>>> c.isdisjoint(d)
False
```