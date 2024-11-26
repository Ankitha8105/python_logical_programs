def count_spaces(string):
    res= sum(1 for ch in string if ch == ' ')
    print(f"The Number of spaces in string is {res}")
    
def main():
    string = "Hello How r u and How was the day"
    count_spaces(string)
    
if __name__ == "__main__":
    main()