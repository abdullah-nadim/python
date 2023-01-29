def def_to_bin(num):
    bits = []

    print(binery)
    while num>0 :
        bits.append(num%2)
        num= num//2
    bits.reverse()

    binary = ''
    for bit in bits:
        binary += str(bit)
    return binary



decimal = int(input("enter decimal"))
binery =def_to_bin(decimal)
