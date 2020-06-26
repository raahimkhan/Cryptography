# for md5

md5_hash_before = "47a6a15acfe53e127d4d3ab814ab3fc0"
md5_hash_after = "911f3a59ffdd252b78eb44e1a602a5f6"

# for sha256

sha256_hash_before = "9280e316d31a0b46137856e5b6dc76fc0053d7e5f8c50cc31b18543b285c23ce"
sha256_hash_after = "bf9b7535a5eaad09f4118c7b278f458f6469d2f2411ac0602c12da12b74d2879"

# number of bits that are same

same_md5 = 0
same_sha256 = 0

def compare(H1, H2):
    count = 0
    for i, j in zip(H1, H2):
        if i == j:
            count = count + 1
            
    return count

def main():
    print("For md5")
    print("H1 : 47a6a15acfe53e127d4d3ab814ab3fc0")
    print("H2 : 911f3a59ffdd252b78eb44e1a602a5f6")
    same_md5 = compare(md5_hash_before, md5_hash_after)
    print(str(same_md5) + " bits are same between H1 and H2 if md5 hash is used")
    print('')
    print('')
    print("For sha256")
    print("H1 : 9280e316d31a0b46137856e5b6dc76fc0053d7e5f8c50cc31b18543b285c23ce")
    print("H2 : bf9b7535a5eaad09f4118c7b278f458f6469d2f2411ac0602c12da12b74d2879")
    same_md5 = compare(sha256_hash_before, sha256_hash_after)
    print(str(same_sha256) + " bits are same between H1 and H2 if sha256 hash is used")
    
main()
    