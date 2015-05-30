import hashes

chainhook_names = set()
chainhooks = {}

def chainhook(func):
    n = func.func_name
    if not n in chainhook_names:
        chainhook_names.add(n)
    return func

class CryptoCur(object):

    p2pkh_version = 0
    p2sh_version = 0
    genesis_hash = 0

    coin_name = 'CryptoCur'
    code = 'COIN'

    def __init__(self):
        global chainhook_names, chainhooks
        for k in dir(self):
            if k in chainhook_names:
                coins = chainhooks.get(k, [])
                if not self in coins:
                    coins.append(self)
                chainhooks[k] = coins

    def header_hash(self, x):
        return hashes.sha256(x)

    def tx_hash(self, x):
        return hashes.sha256(x)

    def base58_hash(self, x):
        return hashes.sha256(x)