def find_vowels(string):
    res = {vow for vow in string if vow in "aeiouAEIOU"}
    print(f"unique vowels :{res}")
    
def main():
    string = "hello world"
    find_vowels(string)

if __name__ =="__main__":
    main()    