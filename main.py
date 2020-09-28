from bitcoin import *
priv = random_key()
#print(priv) # print private key 
pub=privtopub(priv)
 #print public key

addr=pubtoaddr(pub)
print(addr)  #print addr from public key

