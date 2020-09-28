import hashlib
x='bikash'
out=hashlib.sha256(x.encode()).hexdigest()
print(out)