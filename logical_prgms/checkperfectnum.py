import math
def Perfect_num(num):
    
    if math.isqrt(num) ** 2 == num:
        return "Perfect"
    else:
        return "Not Perfect"
        
def main():
    num = 25
    res = Perfect_num(num)
    print(f"The Number is {res} Number")
    
if __name__ == "__main__":
    main()