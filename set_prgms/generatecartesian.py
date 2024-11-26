def generate_cartesian_prd(set1,set2):
    res_set = {(x,y) for x in set1 for y in set2}
    print(f"The cartesian product is {res_set}")
    
def main():
    set1 = {1,2}
    set2 = {3,4}
    generate_cartesian_prd(set1,set2)
    
if __name__ == "__main__":
    main()