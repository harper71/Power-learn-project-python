def large_power(base, exponent):
    if base**exponent > 5000:
        return True
    return False


def divisible_by_10(nums):
    if nums % 10 == 0:
        return True
    return False

if __name__ == '__main__':
    print(large_power(5, 100))
    print(divisible_by_10(100))
    