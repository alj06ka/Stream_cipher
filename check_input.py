import re


def is_key_valid(key):
    """
    :param key: input binary key
    :return: True if key is binary (has only '0' and '1' values
    """
    if len(re.findall('([0-1]*)', key)[0]) == len(key):
        return True
    else:
        return False


if __name__ == '__main__':
    print(is_key_valid('010101010101dgf010100'))

