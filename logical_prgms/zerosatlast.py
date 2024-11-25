import array
def last_zeros(array_ele):
    arr1 = array.array('i')
    arr2 = array.array('i')
    for item in array_ele:
        if(item == 0):
            arr1.append(item)
            
        else:
            arr2.append(item)
    arr2.extend(arr1)
    print(f"the resukt array is {arr2}")
        
def main():
    #arr_ele =array.array('i',[1,0,5,4,0])
    #arr_ele =  array.array('i', [0,1,0,3,12])
    #arr_ele = array.array('i',[1,7,0,0,8,0,10,12,0,4])
    arr_ele =  array.array('i',  [1,7,0,0,8,0,10,12,0,4])
    last_zeros(arr_ele)
    
if __name__ == "__main__":
    main()