# for i1 in range(1,4):
#     for i2 in range(1,4):
#         for i3 in range(1,4):
#             print(i1, i2. i3) #중복순열 = 중복을 허용한 순열


#
# for i1 in range(1,4):
#     for i2 in range(1,4):
#         if i1 != i2:
#             for i3 in range(1,4):
#                 if i3 != i1 and i3 != i2:
#                     print(i1, i2, i3) #그냥 순열

data = [1,2,3]
for i1 in range(len(data)):
     for i2 in range(len(data)):
         if i1 != i2:
             for i3 in range(len(data)):
                 if i3 != i1 and i3 != i2:
                     print(data[i1], data[i2], data[i3])