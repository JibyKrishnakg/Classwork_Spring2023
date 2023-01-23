def incr_by_5(x):
    ans=x+5
    if ans==15:
        print("Not a good number")
        return ans, False
    return ans, True
k=input("Enter the number:")
k=int(k)
y=incr_by_5(k)
print("The answer is {}".format(y))
print(y[0])
print(y[1])
