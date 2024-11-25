def find_kth_element(arr_ele, k):
    arr_ele.sort()
    
    if k > 0 and k <= len(arr_ele):
        print(f"The {k}-th smallest element is {arr_ele[k-1]}")
    else:
        print("Invalid value for k")

def main():
    arr_ele = [7, 4, 6, 3, 9, 1]
    k = 3
    find_kth_element(arr_ele, k)
    
if __name__ == "__main__":
    main()
