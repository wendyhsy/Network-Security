thisdict = {
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
odd = [1,3,5,7,9,11,15,17,19,21,23,25]
for i in range(25):
    for j in odd:
        a = thisdict[(j*(23-i)) % 26]
        b = thisdict[(j*(9-i)) % 26]
        c = thisdict[(j*(4-i)) % 26]
        d = thisdict[(j*(5-i)) % 26]
        e = thisdict[(j*(16-i)) % 26]
        f = thisdict[(j*(20-i)) % 26]
        g = thisdict[(j*(21-i)) % 26]
        h = thisdict[(j*(5-i)) % 26]
        x = thisdict[(j*(18-i)) % 26]
        y = thisdict[(j*(25-i)) % 26]
        k = thisdict[(j*(15-i)) % 26]
        l = thisdict[(j*(21-i)) % 26]
        m = thisdict[(j*(8-i)) % 26]
        n = thisdict[(j*(11-i)) % 26]
        o = thisdict[(j*(25-i)) % 26]
  
        print(a+b+c+d+" "+e+f+g+" "+h+x+y+k+l+m+" "+n+o+". i and j are %d, %d",i,j)



