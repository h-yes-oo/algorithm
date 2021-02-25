def pre(v):
    if v>7:
        return
    else:
        print(v, end=' ')
        pre(v*2) #왼쪽 자식
        pre(v*2+1) #오른쪽 자식
def mid(v):
    if v>7:
        return
    else:
        mid(v*2) #왼쪽 자식
        print(v, end=' ')
        mid(v*2+1) #오른쪽 자식
def post(v):
    if v>7:
        return
    else:
        post(v*2) #왼쪽 자식
        post(v*2+1) #오른쪽 자식
        print(v, end=' ')

pre(1)
print()
mid(1)
print()
post(1)