# Your code here

hash_table = {}

def expensive_seq(x, y, z):
    # Your code here
    if x <= 0:
        hash_table += y+z
    elif x > 0:
        hash_table += exp(x-1,y+1,z) + exp(x-2,y+2,z*2) + exp(x-3,y+3,z*3)
    return hash_table



if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
