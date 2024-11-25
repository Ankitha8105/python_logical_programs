def find_happy_num(num):
    seen_numbers = set() 
    
    while num != 1 and num not in seen_numbers:
        seen_numbers.add(num)  
        sum = 0  
        
        while num != 0:
            d = num % 10
            sum += d * d
            num = num // 10
        
        num = sum  
    
    return num == 1  

def main():
    #num = 19
    num = 2
    res = find_happy_num(num)
    if res:
        print(f"The number {num} is a Happy Number")
    else:
        print(f"The number {num} is not a Happy Number")

if __name__ == "__main__":
    main()

