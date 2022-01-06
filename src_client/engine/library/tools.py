def add_tuples(*args):
    check_length = len(args[0])
    for current_tuple in args:
        if(check_length == len(current_tuple)):
            check_length = len(current_tuple)
        else:
            raise Exception('Tuples are not all the same size')

    list_tuple = zeros(check_length)
    for current_tuple in args:
        for index in range (len(current_tuple)):
            list_tuple[index] += current_tuple[index]
    return tuple(list_tuple)


def zeros(length: int) -> list:
    list_zeros = []
    for i in range(length):
        list_zeros.append(0)
    return list_zeros

if __name__ == "__main__":
    print(add_tuples((1,2,3), (2,3,4), (3,4,5)))