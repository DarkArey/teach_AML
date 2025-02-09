# The function of converting the signed x from decimal to binary representation
# The bin_dig indicates the number of binary digits of the x
# If the bin_dig is less than the required number to represent the x, the ValueError is raised
def dec2bin(x, bin_dig):
    sign = x < 0
    x = abs(x)

    if x == 0:
        bin_x = '0'
        sign = 0
    else:
        bin_x = ""

        while x > 0:
            bin_x = str(x % 2) + bin_x
            x //= 2

    if (len(bin_x) + 1) > bin_dig:
        raise ValueError('The specified bin_dig is less than the required number to represent the x')

    if sign:
        new_bin_x = ''
        f = False
        for dig in range(len(bin_x) - 1, -1, -1):
            if f:
                if bin_x[dig] == '1':
                    new_bin_x = '0' + new_bin_x
                else:
                    new_bin_x = '1' + new_bin_x
            else:
                new_bin_x = bin_x[dig] + new_bin_x
                if bin_x[dig] == '1':
                    f = True
        bin_x = new_bin_x

    for exDig in range(bin_dig - len(bin_x)):
        bin_x = str(int(sign)) + bin_x

    return bin_x


if __name__ == '__main__':
    print(dec2bin(-10, 5))
