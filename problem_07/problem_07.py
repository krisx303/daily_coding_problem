
s = '132212'
# '132212' -> '13221' + b || '1322' + l
# '13221' -> '1322' + a || '132' + u
# '1322' -> '132' + b || '13' + v
# '132' -> '13' + b || ('1' + 0) = false
# '13' -> '1' + c || '' + m
# '1' -> '' + a
# '' -> 1

# '1' -> 'a'
# '13' -> 'ac' + 'm'
# '132' -> 'acb' + 'mb'
# '1322' -> 'acbb' + 'mbb' + 'acv' + 'mv'
# '13221' -> 'acbba' + 'mbba' + 'acva' + 'mva' + 'acbu' + 'mbu'
# '132212' -> 'acbbab' + 'mbbab' + 'acvab' + 'mvab' + 'acbub' + 'mbub' + 'acbbl' + 'mbbl' + 'acvl' + 'mvl'
n = len(s)
D = [0] * (n+1)
D[0] = 1
if n > 0:
    D[1] = 1
for i in range(1, n):
    n2 = int(s[(i-1):(i+1)])
    D[i+1] += D[i]
    if n2 < 27:
        D[i+1] += D[i-1]
print(D)
print(D[-1])