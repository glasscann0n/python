def main():
    number= 8181181
    total = ""
    for i in str(number):
        i=int(i)
        temp = i*i
        temp= str(temp)
        total = total + temp
    total = int(total)
    print(total)
main()