#바이너리 트리를 배열로 표현하기
class BinaryTree:
    def __init__(self,H):   #H : 트리의 높이
        self.tree = [-1] * (pow(2,H+1))

    #부모 노드, 자식노드 정보를 가지고 insert
    def insert(self,parent,child):
        #tree안에 부모가 없으면, 루트
        if parent not in self.tree:
            self.tree[1] = parent
            self.tree[2] = child
        else: # 부모가 이미 트리 안에 있음
            #자식은 어디다? 부모노드의 인덱스 * 2 또는 *2 +1
            p_idx = self.tree.index(parent)
            if self.tree[p_idx * 2] == -1:
                self.tree[p_idx * 2] = child
            else:
                self.tree[p_idx * 2 + 1] = child

    def print_tree(self):
        print(self.tree)

    def pre_order(self,idx):
        if idx>=len(self.tree):
            return
        # 전위순회 부모노드를 자식노드보다 먼저 방문해야 한다.
        if self.tree[idx] != -1:
            print(self.tree[idx],end=" ")
            self.pre_order(idx*2)
            self.pre_order(idx * 2 + 1)

    def in_order(self,idx):
        if idx >= len(self.tree):
            return
        if self.tree[idx] != -1:
            #왼쪽
            self.in_order(idx * 2)
            #부모
            print(self.tree[idx],end=" ")
            #오른쪽
            self.in_order(idx * 2 + 1)

    def post_order(self,idx):
        if idx >= len(self.tree):
            return
        if self.tree[idx] != -1:
            self.post_order(idx*2)
            self.post_order(idx * 2 +1)
            print(self.tree[idx], end=" ")


H = 4 # 트리의 높이를 모르면 ㅠㅠ 인접리스트쓰자 걍. 효율성도 인접행렬보다 인접리스트임.
my_tree = BinaryTree(H)
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
edges = list(map(int,input().split()))
for i in range(0,len(edges),2):
    my_tree.insert(edges[i],edges[i+1])

my_tree.print_tree()
my_tree.pre_order(1)
print()
my_tree.in_order(1)
print()
my_tree.post_order(1)

'''
[-1, 1, 2, 3, 4, -1, 5, 6, 7, -1, -1, -1, 8, 9, 10, 11, 12, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 13, -1]
1 2 4 7 12 3 5 8 9 6 10 11 13 
12 7 4 2 1 8 5 9 3 10 6 13 11 
12 7 4 2 8 9 5 10 13 11 6 3 1 
'''