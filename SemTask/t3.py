values = [0, 2, 10, 6]

def same_by(f,o):
    return all(not f(i) for i in o)

if same_by(lambda x:x%2,values):
    print('1')
else:
    print('0')