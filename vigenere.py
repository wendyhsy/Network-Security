import sys
from collections import Counter
engFreq = {
  "a":0.08167, "b":0.01492,
  "c":0.02782, "d":0.04253,
  "e":0.12702, "f":0.02228,
  "g":0.02015, "h":0.06094,
  "i":0.06996, "j":0.00153,
  "k":0.00772, "l":0.04025,
  "m":0.02406, "n":0.06749,
  "o":0.07507, "p":0.01929,
  "q":0.00095, "r":0.05987,
  "s":0.06327, "t":0.09056,
  "u":0.02758, "v":0.00978,
  "w":0.02360, "x":0.00150,
  "y":0.01974, "z":0.00074
}
engDict = {
  0: "a",1: "b",
  2: "c",3: "d",
  4: "e",5: "f",
  6: "g",7: "h",
  8: "i",9: "j",
  10: "k",11: "l",
  12: "m",13: "n",
  14: "o",15: "p",
  16: "q",17: "r",
  18: "s",19: "t",
  20: "u",21: "v",
  22: "w",23: "x",
  24: "y",25: "z",
}

def dictReverse(letter):
    for num, character in engDict.items():  
        if character == letter:
            return num

def decrypt(key, ciphertext):
    decrypt=""
    len_text=0
    for keyword in ciphertext:
        if (keyword in engFreq): 
            len_text=len_text+1
    keyText1=key*int(len_text/len(key))
    remains=len_text-int(len_text/len(key))*len(key)
    if remains>0:
        keyText1=keyText1+key[:remains]

    for i in range(len_text):
        if (keyword in engFreq):  
            mapped = engDict[(dictReverse(ciphertext[i])-dictReverse(keyText1[i])) % 26]
            decrypt+=mapped
    return decrypt  

def main():
    with open(sys.argv[1], 'r') as my_file:
        ciphertext=my_file.read()
        if ciphertext != None:
            # print("hacking ...")
            text=''.join(filter(str.isalpha, ciphertext)).lower()
            examine(text)
        else:
            print("Nothing to hack...")

def examine(text):
    potentialKenys=findFreqWords(text)
    factors={}
    for i in potentialKenys:
        factors[i]=[]
        for j in potentialKenys[i]:
            factors[i].extend(findFactors(j))
    commonFactors=findCommonGCD(factors)
    topKeys=[]
    for i in commonFactors:
        topKeys.append(i[0])
    # for k in topKeys:
    #     if k>2:
    split(text, max(topKeys))
    # print("topKeys",topKeys)
    return topKeys

def findFreqWords(text):
    dictKey={}
    for keyLen in range(2,7):
        for k in range(len(text)-keyLen):
            keyword = text[k:k+keyLen]
            for j in range(k+keyLen, len(text)-keyLen):
                if text[j:j+keyLen]==keyword:
                    if (keyword not in dictKey):
                        dictKey[keyword] = []
                        keyword = ""
                    else:
                        if(j-k)>1:
                            dictKey[keyword].append(j-k)
                        keyword = ""
   
    cleanDictKey = dict((k,v) for k,v in dictKey.items() if len(v)>1)
    return cleanDictKey


def findFactors(x):
    factors=[]
    for i in range(2, 20):
        if x%i==0:
            factors.append(i)
    if 1 in factors:
        factors.remove(1)
    return factors

def findCommonGCD(factors):
    counts={}
    for i in factors:
        for j in factors[i]:
            if j not in counts:
                counts[j]=1
            else:
                counts[j]+=1
    topCounts = Counter(counts).most_common(3)
    # print("topcount", topCounts)
    return topCounts

def split(text, length):
    strings=[]
    for i in range(0,len(text)-1,length):
        k=text[i:i+length]
        strings.append(k)
    buckets={}
    mostFrequent={}
    leastFrequent={}
    solution=""
    for b in range(len(strings[0])):
        buckets[b]={"a":0, "b":0,"c":0,"d":0,
                    "e":0, "f":0,"g":0,"h":0,
                    "i":0, "j":0,"k":0,"l":0,
                    "m":0, "n":0,"o":0,"p":0,
                    "q":0, "r":0,"s":0,"t":0,
                    "u":0, "v":0,"w":0,"x":0,
                    "y":0, "z":0}
        mostFrequent[b]={}
        leastFrequent[b]={}
    for i in strings:
        for j in range(len(i)):
            if i[j] in buckets[j]:
                buckets[j][i[j]]+=1
            # else:
            #     buckets[j][i[j]]=1
    # print("buckets",buckets)
    for b in range(len(strings[0])):
        mostFrequent[b] = Counter(buckets[b]).most_common(3)
        leastFrequent[b] = Counter(buckets[b]).most_common()[:-3-1:-1]
        # print("mostfrequent b", mostFrequent[b])
        # print("leastFrequent b", leastFrequent[b])  
        most=[]
        least=[]      
        for keyM in mostFrequent[b]:
            most.append(keyM[0])
        for keyL in leastFrequent[b]:
            least.append(keyL[0])
        for key in mostFrequent[b]:
            for i in most:
                # find location of the most key
                mostNum=dictReverse(key[0])
                # find letter "a"'s location
                k=(mostNum-4)%26
                # find what letter is shifted to from a
                
                # print("a:", a, "K:",k)
                # print("z:", engDict[(k+25)%26])
                if engDict[(k+25)%26] in least:
                    a=engDict[k]
                    solution=solution+a
                    break    
            
            
    print(solution)
    print(decrypt(solution, text))

    return strings

if __name__ == '__main__':
    main()