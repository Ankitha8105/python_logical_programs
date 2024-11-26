def find_ele_divby_digit(num):
    res = [i for i in range(0,num) if True in [True for x in range(2,9) if num%x == 0]]
    print(res)
    
def main():
    num = 50
    find_ele_divby_digit(num)
    
if __name__ == "__main__":
    main()
    
    