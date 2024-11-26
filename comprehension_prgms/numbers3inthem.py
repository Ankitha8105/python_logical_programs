def find_3contaning_num(num):
    res = [i for i in range(0,num) if '3' in str(i)]
    print(res)
    
def main():
    num = 50
    find_3contaning_num(num)
    
if __name__ == "__main__":
    main()