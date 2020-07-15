import hashlib
import itertools

GESTURE_SALT = "28DF17A9B837BAFD951724E325F6F86B5B6E477D"  # constant
target = "hash"
uin = "QQ"


def encodeGesture(gesture, uid):
    i = len(uid)
    length = len(GESTURE_SALT)
    md5 = hashlib.new('md5', gesture.encode()).hexdigest()
    tmp = md5[:6] + GESTURE_SALT[:int(length / 2)] + md5[6:]
    tmp2 = tmp[:len(tmp) - 9] + GESTURE_SALT[int(length / 2):] + tmp[len(tmp) - 9:]
    tmp = tmp2[:2] + uid[:int(i / 2)] + tmp2[2:]
    tmp2 = tmp[:len(tmp) - 5] + uid[int(i / 2):] + tmp[len(tmp) - 5:]
    md5 = hashlib.new('md5', tmp2.upper().encode("utf-8")).hexdigest()
    return md5.upper()


for i in range(3, 10):
    for j in itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8], i):
        key = str(j).replace('(', '[').replace(')', ']')
        if encodeGesture(key, uin) == target:
            print(j)
            exit(0)
print("no gesture found")
