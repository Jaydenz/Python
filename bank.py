
# def counter(basemoney, lilv, i=1):
#     totalmoney = basemoney + basemoney * lilv
#     print(totalmoney)
#     a = totalmoney // 500
#     if a == 2:
#         return i
#     else:

#         return counter(totalmoney, lilv, i=i+1)
    

# b =counter(500, 0.1)
# print(b)

items = [1, 10, 7, 4, 5, 9]
def sum(items):
    head, *tail = items
    print(*tail)
    print(head)
    return head + sum(tail) if tail else head
print(sum(items))
