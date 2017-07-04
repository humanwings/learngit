# sha256(文字列) => SHA256-16進数文字列、Bitcoin秘密鍵相当、64文字
# hash160(16進数文字列) => RIPEMD160-16進数文字列、40文字
# privtopub(秘密鍵16進数文字列) => 公開鍵16進数文字列
# pubtoaddr(公開鍵16進数文字列) => アドレス文字列(base58checkエンコード)
# random_key() => 16進数64文字秘密鍵相当
# encode_pubkey(公開鍵16進数文字列, 'bin') => バイナリ形式公開鍵
# encode_privkey(priv, formt, vbyte=0) => formt:decimal,bin,bin_compressed,hex,hex_compressed,wif,wif_compressed
# decode_privkey => function of convert hex to decimal
# bin_to_b58check(bin_hash160(pubbin1), 0) => アドレス文字列

import bitcoin

# Generate a random private key
valid_private_key = False 

while not valid_private_key:
    private_key = bitcoin.random_key()
    # private_key = 1E99423A4ED27608A15A2616A2B0E9E52CED330AC530EDCC32C8FFC6A526AEDD
    decoded_private_key = bitcoin.decode_privkey(private_key, 'hex')
    valid_private_key =  0 < decoded_private_key < bitcoin.N

print("Private Key (hex) is: ", private_key)
print("Private Key (decimal) is: ", decoded_private_key)

# Convert private key to WIF format
wif_encoded_private_key = bitcoin.encode_privkey(decoded_private_key, 'wif')

print("Private Key (WIF) is: ", wif_encoded_private_key)

# Add suffix "01" to indicate a compressed private key
compressed_private_key = private_key + '01'

print("Private Key Compressed (hex) is: ", compressed_private_key)

# Generate a WIF format from the compressed private key (WIF-compressed)
wif_compressed_private_key = bitcoin.encode_privkey(
    bitcoin.decode_privkey(compressed_private_key, 'hex'), 'wif')
wif_compressed_private_key2 = bitcoin.encode_privkey(
    compressed_private_key, 'wif_compressed')
print("Private Key (WIF-Compressed) is: ", wif_compressed_private_key)
print("Private Key (WIF-Compressed) is: ", wif_compressed_private_key2)

# Multiply the EC generator point G with the private key to get a public key point
print("bitcoin.G is:", bitcoin.G)
public_key = bitcoin.fast_multiply(bitcoin.G, decoded_private_key) 
print("Public Key (x,y) coordinates is:", public_key)

# Encode as hex, prefix 04
hex_encoded_public_key = bitcoin.encode_pubkey(public_key,'hex') 
print("Public Key (hex) is:", hex_encoded_public_key)

# Compress public key, adjust prefix depending on whether y is even or odd
(public_key_x, public_key_y) = public_key 
if (public_key_y % 2) == 0:
    compressed_prefix = '02' 
else:
    compressed_prefix = '03'
hex_compressed_public_key = compressed_prefix + bitcoin.encode(public_key_x, 16) 
print("Compressed Public Key (hex) is:", hex_compressed_public_key)

# Generate bitcoin address from public key
print("Bitcoin Address (b58check) is:", bitcoin.pubkey_to_address(public_key))


# Generate compressed bitcoin address from compressed public key
print("Compressed Bitcoin Address (b58check) is:", bitcoin.pubkey_to_address(hex_compressed_public_key))