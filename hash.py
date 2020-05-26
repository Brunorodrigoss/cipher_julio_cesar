def apply_sha1(text):
    import hashlib
    result = hashlib.sha1(text.encode())
    return result.hexdigest()
