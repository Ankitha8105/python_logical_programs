def find_nonrepeating_ch(string):
    res = " ".join(ch for ch in string if string.count(ch) == 1)
    print(f"The non -repeated character is {res}")
    
def main():
    string = "sswiiggyy"
    find_nonrepeating_ch(string)
    
if __name__ == "__main__":
    main()