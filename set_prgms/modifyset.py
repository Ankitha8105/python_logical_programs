def modify_set(set_ele):
    after_adding = set_ele.add(5)
    after_removing = set_ele.remove(2)
    after_discard = set_ele.discard(5)
    set1 = {6,9}
    updating = set_ele.update(set1)
    pop_op = set_ele.pop()
    print(f"After adding 5: {after_adding}")
    print(f"After removing 2: {after_removing}")
    print(f"After discarding 5: {after_discard}")
    print(f"After updating {set1}: {updating}")
    print(f"After poping : {pop_op}")
    
def main():
    set_ele = {1,2,3}
    modify_set(set_ele)
    
if __name__ == "__main__":
    main()