import random
from timer import setTime

'''
Esta classe representa CADA fila da simulacao. Ela ira conter todos os
dados necessarios, como capacidade, servidores, tempos de entrada e saida
para numero pseudo-aleatorio...

Ela ira conter em formato de hashes, todos os seus estados (por exemplo:
com capacidade 4, ela tera estados 0...5).
'''

class Queue:
    index = None
    nextQueue = None
    sameRotation = None
    outQueue = None
    server = None
    capacity = None
    states = {}
    min_arrival = None
    max_arrival = None
    min_exit = None
    max_exit = None
    
    # Variaveis de controle
    currentState = 0
    loss = 0
    previousTime = 0
    
    def __init__(self,index,nextQueue,sameRotation,outQueue,server,capacity,arrival,exitTime):
        self.index = index
        self.nextQueue = float(nextQueue)
        self.sameRotation = float(sameRotation)
        self.outQueue = float(outQueue)
        self.server = int(server)
        self.capacity = int(capacity)
        self.states = {}
        for i in range(self.capacity+1):
            self.states[i] = 0
        self.min_arrival = int(arrival[0])
        self.max_arrival = int(arrival[1])
        self.min_exit = int(exitTime[0])
        self.max_exit = int(exitTime[1])
        self.loss = 0
        self.currentState = 0

    def getId(self):
        return self.index
       
    def getStates(self):
        return self.states
    
    def getLoss(self):
        return self.loss
        
    # OBSERVACAO: Este aleatorio nao envolve nem entrada nem saida.
    # COMO O PROPRIO MATERIAL DE AULA MOSTRA, e um aleatorio qualquer
    # para decidir em qual rotacao a fila segue depois de simular um
    # passo, logo teve-se que se usar um random qualquer.
    def shuffle_probability(self):
        return random.uniform(0,1)
    
    # Geradores de numeros pseudo-aleatorios. Chamam o generator para
    # retornar o valor    
    def shuffle_arrival(self,generator):
        return (self.max_arrival - self.min_arrival) * generator.generate() + self.min_arrival
    
    def shuffle_exit(self,generator):
        return (self.max_exit - self.min_exit) * generator.generate() + self.min_exit
    
    
    # Estas duas funcoes a seguir simplesmente agendam uma chegada ou
    # saida, de acordo com o tempo e sorteio providos.    
    def schedule_arrival(self,time,shuffle,events):
        if self.index == 'Q1':
            events.append({'queue':self.index,'event':'ch','time':time + shuffle,'shuffle':shuffle})
    
    def schedule_exit(self,time,shuffle,events):
        events.append({'queue':self.index,'event':'sa','time':time + shuffle,'shuffle':shuffle})
        if(self.shuffle_probability() < self.nextQueue):
            # Se cair aqui, ele vai agendar chegada para a proxima fila
            string = self.index
            new = int(string.replace('Q',''))
            new += 1
            new = 'Q'+str(new)
            events.append({'queue':new,'event':'ch','time':time + shuffle,'shuffle':shuffle})
        elif(self.sameRotation > 0):
            # Se ter rotacao para ele mesmo, agenda chegada para ele mesmo
            # Se ele cair fora do sistema, nao faz nada, pois a saida ja fara o trabalho
            events.append({'queue':self.index,'event':'ch','time':time + shuffle,'shuffle':shuffle})
     
     
    # As duas funcoes a seguir servem como os algoritmos de contabilizacao
    # Eles foram adaptados para funcionar com todos os tipos de rotacoes,
    # seja de uma fila para outra, como de uma fila para ela mesma.
    # Como o algoritmo de rotacao e bastante parecido, no cont_exit(),
    # foi agendado uma saida e uma entrada com o mesmo tempo, pois o
    # algoritmo resumidamente e baseado neste conceito.
    
    def cont_arrival(self,event,events,generator):
        print('CONTABILIZANDO CHEGADA...')
        print('Fila ' + str(self.index) + ' entrou de tamanho ' + str(self.currentState))
        if self.currentState < self.capacity:
            self.states[self.currentState] += (event['time'] - self.previousTime)
            setTime(event['time'] - self.previousTime)
            self.previousTime = event['time']
            self.currentState += 1
            print('Fila ' + str(self.index) + ' saiu de tamanho ' + str(self.currentState))
            if self.currentState <= self.server:
                shuffle = self.shuffle_exit(generator)
                self.schedule_exit(event['time'],shuffle,events)
        else:
            self.loss += 1
            print('LOSS!!!')
        shuffle = self.shuffle_arrival(generator)
        self.schedule_arrival(event['time'],shuffle,events)
            
    def cont_exit(self,event,events,generator):
        print('CONTABILIZANDO SAIDA...')
        print('Fila ' + str(self.index) + ' entrou de tamanho ' + str(self.currentState))
        self.states[self.currentState] += (event['time'] - self.previousTime)
        setTime(event['time'] - self.previousTime)
        self.previousTime = event['time']
        self.currentState -= 1
        print('Fila ' + str(self.index) + ' saiu de tamanho ' + str(self.currentState))
        if self.currentState >= self.server:
            shuffle = self.shuffle_exit(generator)
            self.schedule_exit(event['time'],shuffle,events)
