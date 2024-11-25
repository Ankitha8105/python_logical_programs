def print_single_count(string):
    
    count = 1
    result = ""
    
   
    for i in range(1, len(string)):
        if string[i] == string[i - 1]:  
            count += 1
        else: 
            result += f"{count}{string[i - 1]}"
            count = 1  
    
    
    result += f"{count}{string[-1]}"
    print(result)
            
            
def main():
    string = 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'
    print_single_count(string)
    
if __name__ == '__main__':
    main()