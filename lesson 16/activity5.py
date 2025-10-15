def find_first_set_bit(n):
    if n == 0:
        return -1  #no set bits in 0
    position = 0
    while (n & 1) == 0:
       n>>= 1
       position += 1
       return position
    

    # example usage: 
    number = 8 #Binary: 10010
    find_first_set_bit_position = find_first_set_bit(number)
    print(f"First set bit position: {find_first_set_bit}")