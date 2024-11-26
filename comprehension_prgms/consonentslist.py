def consonents_list(string):
    vowels = "aeiouAEIOU"
    res = [ch for ch in string if ch.isalpha() if ch not in vowels]
    print(res)
    
def main():
    string = "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"
    consonents_list(string)

if __name__ == "__main__":
    main()