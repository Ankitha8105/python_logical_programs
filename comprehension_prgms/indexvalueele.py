def find_indexvalue(list_ele):
    res = [(index,value) for index,value in enumerate(list_ele) ]
    print(res)
    
def main():
    list_ele = ['hii',4,8.9,'Apple']
    find_indexvalue(list_ele)

if __name__ == "__main__":
    main()