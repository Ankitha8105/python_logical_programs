import array
def bigger_ele(arr_ele):
    big = arr_ele[0]
    for item in arr_ele:
        if item >= big:
            big = item
    return big

def main():
    #arr_ele = array.array('i', [3,2,3])
    arr_ele = array.array('i', [2,2,1,1,1,2,2])
    biggest_ele =bigger_ele(arr_ele)
    print(f"The Biggest element in array is {biggest_ele}")
    
if __name__ == "__main__":
    main()