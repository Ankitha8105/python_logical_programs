def reverse_vowels(string):
    vowels = 'aeiouAEIOU'
    str_list = list(string)
    i,j=0,len(str_list)-1
    
    while i<j:
        if str_list[i] not in vowels:
            i += 1
        elif str_list[j] not in vowels:
            j -= 1
            
        else:
            str_list[i],str_list[j] = str_list[j],str_list[i]
            i += 1
            j -= 1
        
    res_str = ''.join(str_list)
    print(f"The reversed string is {res_str}")
           
def main():
    #string = "hello"
    string = "leetcode"
    reverse_vowels(string)

if __name__ == "__main__":
    main()
