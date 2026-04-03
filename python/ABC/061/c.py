s = input()
n = len(s)

def self(i,w):
    if(i == n-1):
        return sum(list(map(int, w.split("+"))))
    return self(i+1,w+s[i+1]) + self(i+1,w+"+"+s[i+1])

print(self(0,s[0]))
