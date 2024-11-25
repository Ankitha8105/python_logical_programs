def find_idx_target(arr_ele,target):
    for idx in range(0,len(arr_ele)):
        if(arr_ele[idx] == target):
            print(idx)
            break

def main():
    '''arr_ele = [2, 3, 5, 7, 9]
    target = 7    '''
    arr_ele = [1, 2, 3, 4, 4, 5, 6, 7]
    target = 4
    find_idx_target(arr_ele,target)
    
if __name__ == "__main__":
    main()