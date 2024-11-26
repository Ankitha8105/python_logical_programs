def print_evenodd(num):
    res =["even" if i%2 == 0 else "odd" for i in range(0,num) ]
    print(res)
    
def main():
    num = 10
    print_evenodd(num)
    
if __name__ == "__main__":
    main()
    