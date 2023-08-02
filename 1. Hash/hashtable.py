def checkPrime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def getPrime(n):
    if n % 2 == 0:
        n = n + 1
    while not checkPrime(n):
        n += 2
    return n

def hashFunction(key):
    capacity = getPrime(10)
    return key % capacity

def insertData(key, data):
    index = hashFunction(key)
    # Handling collisions using chaining
    if hashTable[index] == []:
        hashTable[index] = [[key, data]]
    else:
        hashTable[index].append([key, data])

def removeData(key):
    index = hashFunction(key)
    if hashTable[index] != []:
        for i, kv in enumerate(hashTable[index]):
            if kv[0] == key:
                del hashTable[index][i]
                return
    print("Key not found")

hashTable = [[] for _ in range(10)] # Corrected initialization

insertData(123, "apple")
insertData(432, "mango")
insertData(213, "banana")
insertData(654, "guava")

print(hashTable)

removeData(123)

print(hashTable)
