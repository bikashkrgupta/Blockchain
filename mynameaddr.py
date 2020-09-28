from bitcoin import *
priv=sha256('bikash')
pub=privtopub(priv)
addr=pubtoaddr(pub)
print(addr)