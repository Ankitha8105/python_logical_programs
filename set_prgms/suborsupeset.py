def check_set(set1,set2):
    res1 = set1.issubset(set2)
    res2 = set1.issuperset(set2)
    if res1:
        print(f"The set1 is a subset of set2")
    else:
        print(F"The set1 is not a subset of set2")
     
    if res2:
          print(f"The set1 is a superset of set2")
    else:
        print(F"The set1 is not a superset of set2") 
    
def main():
    set1 = {1,2,3}
    set2 = {1,2,3,4,5}  
    check_set(set1,set2)
    
if __name__=="__main__":
    main()