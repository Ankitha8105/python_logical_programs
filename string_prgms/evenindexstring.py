def create_evenindex_st(st):
    res = ' '.join(st[i] for i in range(0,len(st)) if i%2 == 0)
    print(f"The even index string is :{res}")
    
def main():
    st = "abcdef"
    create_evenindex_st(st)
    
if __name__== "__main__":
    main()