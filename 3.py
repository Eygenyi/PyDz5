l=str(input())
def pol(l):
    if len(l)<1:
        print('True')
    elif l[0]==l[-1]:
            pol(l[1:-1])
    else:
        print('false')
pol(l)