# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

def closepath(num: int) -> int:
    closedPa = 0
    oneValues = '0469'
    numStr = str(num)
    
    for i in numStr:
        if i in oneValues:
            closedPa += 1
        if i == '8':
            closedPa += 2
            
    return closedPa

def vowelConsonants(word: str) -> str:
    vow, cons, = "", ""
    vowel = 'AIEOUaieou'
    
    for i in word:
        if i in vowel:
            vow += i
        else:
            cons += i
    
    return vow, cons


vowel, cons = vowelConsonants("onomatopoeia ")
print(vowel +"\n" + cons)

x = closepath(1234567890)
print("\n", x)

