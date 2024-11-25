import array
def find_nonrepeated(arr_ele):
    dict_ele = { }
    
    for i in arr_ele:
        if i in dict_ele:
            dict_ele[i] += 1
        else:
            dict_ele[i] = 1
    
    for items in dict_ele:
        if (dict_ele[items] == 1):
            print(f"The Element is not repeated in array is {items}")
            break
    
def main():
    arr_ele = array.array('i',[6,6,2,3,7,3,7])
    find_nonrepeated(arr_ele)
    
if __name__=="__main__":
    main()