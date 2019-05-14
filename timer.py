'''
Esta pequena classe simplesmente contabiliza o tempo final total de toda
a simulacao. Resolveu-se modularizar para tornar mais facil de chamar
e mais coerente. Possui apenas o seu getter e setter
'''

timer = 0

def setTime(time):
    global timer
    timer += time
	
def getTime():
    global timer
    return timer
