import array
def reverse_array(arr_ele):
    n = len(arr_ele)
    for i in range(0,n // 2):
        temp = arr_ele[i]
        arr_ele[i] = arr_ele[n - 1 - i]
        arr_ele[n - 1 - i] = temp
    return arr_ele


def main():
    list_arr = []
    arr_ele = array.array('i',[1, 2, 3, 4, 5])
    res_arr = reverse_array(arr_ele)
    for items in res_arr:
        list_arr.append(items)
    print(f"The Array elements is {list_arr}")
    
if __name__ == "__main__":
    main()    