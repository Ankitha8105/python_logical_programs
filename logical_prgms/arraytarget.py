import array

def find_target(arr_ele, target):
    for i in range(0, len(arr_ele)):
        for j in range(i + 1, len(arr_ele)):
            if arr_ele[i] + arr_ele[j] == target:
                return i, j
    return None  

def main():
    arr_ele = array.array('i', [3, 2, 4])
    target = 6  
    
    result = find_target(arr_ele, target)
    if result:
        res1, res2 = result
        print(f"Indices of elements that add up to {target}: {res1}, {res2}")
    else:
        print(f"No two elements found that add up to {target}")

if __name__ == "__main__":
    main()
