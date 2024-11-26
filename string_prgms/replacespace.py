def repace_spacewith_underscore(st):
    res = ''.join("_" if c==" " else c for c in st)
    print(res)
    
def main():
    string ="hello World"
    repace_spacewith_underscore(string)
    
if __name__ == "__main__":
    main()
    