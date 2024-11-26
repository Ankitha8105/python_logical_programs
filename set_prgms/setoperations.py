def operations_on_set(set1,set2):
    union_set = set1.union(set2)
    set_diff = set1.difference(set2)
    set_intersection = set1.intersection(set2)
    set_symmetric = set1.symmetric_difference(set2)
    set1.difference_update(set2)
    
    return union_set,set_diff,set_intersection,set_symmetric,
    
def main():
    set1 = {1,2,3,4}
    set2 ={3,4,5,6}
    union_set,diff_set,intersection_set,symmetric= operations_on_set(set1,set2)
    print(f"The union of two sets is {union_set}")
    print(f"The intersection of two sets is {intersection_set}")
    print(f"The difference of two sets is {diff_set}")
    print(f"The symmetric between two sets is {symmetric}")
    print(f"The update of two sets is {set1}")
    
if __name__=="__main__":
    main()