def sum_common(lst1, lst2, lst3):
    sum = 0
    for item in lst1:
        if item in lst2 and item in lst3:
            sum += item
    return sum
def main():
    print(sum_common([1, 2, 3], [5, 3, 2], [7, 3, 2])) 
    print(sum_common([1, 2, 2, 3], [5, 3, 2, 2], [7, 3, 2, 2]))  
    print(sum_common([1], [1], [2]))  
    
if __name__ == "__main__":
    main()
