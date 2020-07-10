lookup_table = {}

def exps(x, y, z):
    if x <= 0: 
        return y + z

    #else
    return exps(x-1,y+1,z) + exps(x-2,y+2,z*2) + exps(x-3,y+3,z*3)



def expensive_seq(x, y, z):
    global lookup_table
   # see if we have computed an answer for the triple before
    my_triple = (x, y, z)
    
    if my_triple in lookup_table:
        return lookup_table[my_triple]
        
    answer_for_this_triple = exps(x, y, z)

    # store the answer
    lookup_table[my_triple] = answer_for_this_triple

    return answer_for_this_triple

if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))

print('done')