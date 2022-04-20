def printbyte(a):
    print(bin(a))

if __name__ == '__main__':
    # printbyte(1)
    # printbyte(2)
    # printbyte(3)
    # printbyte(4)
    printbyte(5)
    # printbyte(6)
    # printbyte(7)

    printbyte(5 << 2)
    print(int(bin(5 << 2), 2))
    printbyte(5 >> 2)
    print(int(bin(5 >> 2), 2))

    # << 按位左移，左移n位相当于乘以2的n次方
    # >> 按位右移 ，左移n位相当于除以2的n次方
    # &  按位与，二进制位数同且为1结果位为1
    # l  按位或 ，二进制位数或有1结果位为1
    # ^  按位异或 ，二进制位数不同结果位为1
    # ~  按位取反，二进制位0和1结果位互换
