def reverse_integer(num):
    
    if num < 0:
        temp = num * -1
        rev = cal_rev(temp)
        print(f"The reverse of {num} is {rev*-1}")
    else:
        rev =cal_rev(num)
        print(f"The reverse of {num} is {rev}")
        
def cal_rev(num):
    rev = 0
    while(num != 0):
        d = num%10
        rev = rev*10 + d
        num = num//10
    return rev
           
def main():
    #num = 123
    num = -4576
    reverse_integer(num)
    
if __name__ =="__main__":
    main()