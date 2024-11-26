def reverse_ch_word(string):
    res = " ".join(words[::-1] for words in string.split())
    print(res)
    
def main():
    string  = "hello world"
    reverse_ch_word(string)
    
if __name__ == "__main__":
    main()