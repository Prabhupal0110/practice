a=1
b=1
print(a-b)
print(a+b)
print(a*b)

def calc(c,d,operation):
    if operation=='+':
        return (c+d);
    elif operation=='-':
        return (c-d);
    elif operation == '*':
        return (c*d);
    else:
        return (c/d);
