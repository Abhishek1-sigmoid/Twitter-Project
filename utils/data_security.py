import hashlib

def md5_hashing(s):
    if type(s) == int:
        s = str(s)
    result = hashlib.md5(s.encode()).hexdigest()
    return result
