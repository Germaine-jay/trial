alpha = ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV')
codes = ('!@#$%^&*()_+-?|\/}{][><_~=`1234567890')

alpha.split()
codes.split()

d = dict(zip(alpha,codes))


messages = input('enter message:')
def encoded(messages):
    code=''
    for i in range(len(messages)):
        if messages[i] in d.keys():
            code += d[messages[i]]
        else:
            code += messages[i]
    return code

def decoded(encry):
    code = ''
    for c in range(len(encry)):
        if encry[c] in d.values():
            keys = [i for i, r in d.items() if r==encry[c] ]
            code += ''.join(keys)
        else:
            code += encry[c]
    return code

encoded_message = encoded(messages)
print(encoded_message)
print(decoded(encoded_message))