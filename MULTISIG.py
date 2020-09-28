from bitcoin import *
pub1=privtopub(random_key())
pub2=privtopub(random_key())
pub3=privtopub(random_key())
multi=mk_multisig_script(pub1,pub2,pub3,2,3) # 2 sign out of 3
maddr=scriptaddr(multi)
print(maddr)
