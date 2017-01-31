# You are given a string "abc" which is encoded like "123" where alphabets are mapped like a => 1 to z => 26. Now find out how many string can be formed by reverse engineering encode string "123". 

# For ex. given string "123" we can form 3 string "abc"(1,2,3), "lc" (i.e 12,3), "aw"(1,23). 

# for string "1234" we have following possible combinations, I might be missing some of them but you get the idea 

# {12, 3, 4} 
# {1, 23, 4} 
# {1, 2, 3, 4}


string = '1234'

def decode(string):
    def compute(index, sub, combinations):
        if sub:
            if int(sub) <= 26: combinations.append(sub)
            else: compute(index, string[index], combinations)
        for i in range(index+1, len(string)):
            compute(i, string[index], combinations)