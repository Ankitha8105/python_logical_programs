def frozenset_operations(set_ele):
    frozen_set = frozenset(set_ele)
    max_ele,min_ele = max(frozen_set),min(frozen_set)
    length = len(frozen_set)
    sort_set = sorted(frozen_set)
    return frozen_set,max_ele,min_ele,length,sort_set

def main():
    s = {1,2,3,4,5,6,7,2,1}
    res_set,max_ele,min_ele,length,sorted_set = frozenset_operations(s)
    print(f"The frozenset is {res_set}")
    print(f"The maxmimum element in the set is {max_ele}")
    print(f"The minimum element in the set  is {min_ele}")
    print(f"The length of frozenset is {length}")
    print(f"The sorted frozenset is {sorted_set}")
    
if __name__ == "__main__":
    main()