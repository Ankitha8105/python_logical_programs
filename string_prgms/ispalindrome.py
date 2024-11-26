def check_palindrome(st):
    cleaned = "".join(c.lower() for c in st if c.isalnum())
    return cleaned == cleaned[::-1]
           
def main():
    print(check_palindrome("A man a plan a canal Panama"))
    
if __name__== "__main__":
    main()   