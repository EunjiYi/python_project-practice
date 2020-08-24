a = "test"
is_break = False
for i in range(len(a)):
    if a[i] == 'k':
        print("break 걸림")
        is_break = True
        break
# else:
#     print("break 안걸림")
if not is_break:
    print("break 안걸림")

