from itertools import zip_longest


def compareVersion( version1: str, version2: str) -> int:
    print(zip_longest(version1.split('.'), version2.split('.'), fillvalue=0))

    for v1, v2 in zip_longest(version1.split('.'), version2.split('.'), fillvalue=0):
            x, y = int(v1), int(v2)
            if x != y:
                return 1 if x > y else -1
    return 0

A="1.01"
B="1.001"
C=compareVersion(A,B)
print(C)