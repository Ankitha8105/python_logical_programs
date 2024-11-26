def divisible_by7(num):
    
    res =[i for i in range(0,num) if i%7 == 0]
    print(f"The result string is {res}")
    
def main():
    num =1000
    divisible_by7(num)
    
if __name__ == "__main__":
    main()