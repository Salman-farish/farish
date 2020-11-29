lis=[[2,'john',4200],[1,"barath",3400],[3,"heela",3300]]

def sort_foo(x):
    return x[0]
print(sorted(lis,key=sort_foo))