def solution(number):
    count=0
    total = 0
    while count < number:
        if (count % 3) == 0 and (count % 5) == 0:
            total += count
        elif (count % 3) == 0:
            total += count
        elif (count % 5) == 0:
            total += count
        count +=1
    print(total)
    return total

def main():
    solution(35559)
    solution(8643)
    solution(9001)
main()