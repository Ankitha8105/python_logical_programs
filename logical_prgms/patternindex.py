import re
def find_index_pattern(text,pattern):
    pat = re.compile(pattern)
    res = pat.search(text)
    if res:
        print(res.start())
    else:
        print("Pattern match not found")
    
def main():
    
    text = 'ABCABAABCABAC'
    pattern = 'CAB'
    
    find_index_pattern(text,pattern)
    
if __name__ == "__main__":
    main()
