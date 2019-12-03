from hashlib import sha256

#Convert a plain text to a SHA256 Hash
def convert_sha256(plain):
    m = sha256()
    plain_byte = bytearray(str(plain), 'utf-8')
    m.update(plain_byte)
    return m.hexdigest()