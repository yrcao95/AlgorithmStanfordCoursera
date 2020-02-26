def multi(num1,num2):
    length_num1, length_num2=len(str(num1)),len(str(num2))
    num1_one=(str(num1)[:length_num1//2])
    if num1_one=="":
        num1_one_int=0
    else:
        num1_one_int=int(num1_one)
    num1_zero=(str(num1)[length_num1//2:])
    if num1_zero=="":
        num1_zero_int=0
    else:
        num1_zero_int=int(num1_zero)
    num2_one=(str(num2)[:length_num2//2])
    if num2_one=="":
        num2_one_int=0
    else:
        num2_one_int=int(num2_one)
    num2_zero=(str(num2)[length_num2//2:])
    if num2_zero=="":
        num2_zero_int=0
    else:
        num2_zero_int=int(num2_zero)
    base_one=len(str(num1_zero))
    base_two=len(str(num2_zero))
    if len(str(num1))==1 and len(str(num2))==1:
        return num1*num2
    return num1_one_int*num2_one_int*10**(base_one+base_two)+num1_one_int*num2_zero_int*10**base_one+num1_zero_int*num2_one_int*10**base_two+num1_zero_int*num2_zero_int


print(multi(
3141592653589793238462643383279502884197169399375105820974944592,2718281828459045235360287471352662497757247093699959574966967627))