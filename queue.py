import random
from timer import setTime

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
        print(self.min_exit)
        print(self.states)

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
        
    def shuffle_arrival(self,generator):
        return (self.max_arrival - self.min_arrival) * generator.generate() + self.min_arrival
    
    def shuffle_exit(self,generator):
        return (self.max_exit - self.min_exit) * generator.generate() + self.min_exit
        
    def schedule_arrival(self,time,shuffle,events):
        if self.index == 'Q1':
            events.append({'queue':self.index,'event':'ch','time':time + shuffle,'shuffle':shuffle})
    
    def schedule_exit(self,time,shuffle,events):
        events.append({'queue':self.index,'event':'sa','time':time + shuffle,'shuffle':shuffle})
        print('SEI LA ' + str(time + shuffle))
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
            
    def cont_arrival(self,event,events,generator):
        print('ARRIVAL ENTERED')
        print('Fila ' + str(self.index) + ' esta de tamanho ' + str(self.currentState))
        print('Aplicando algoritmo...')
        if self.currentState < self.capacity:
            self.states[self.currentState] += (event['time'] - self.previousTime)
            setTime(event['time'] - self.previousTime)
            print('ENTRADA TEMPO ' + str(self.states[self.currentState]) + ' EM ' + self.index + ' ' + str(self.currentState))
            self.previousTime = event['time']
            self.currentState += 1
            print('Fila ' + str(self.index) + ' AGORA ATUALIZADA esta de tamanho ' + str(self.currentState))
            if self.currentState <= self.server:
                shuffle = self.shuffle_exit(generator)
                self.schedule_exit(event['time'],shuffle,events)
        else:
            self.loss += 1
            print('PERDEU PLAYBOY')
        shuffle = self.shuffle_arrival(generator)
        self.schedule_arrival(event['time'],shuffle,events)
            
    def cont_exit(self,event,events,generator):
        print('EXIT ENTERED')
        print('Fila ' + str(self.index) + ' esta de tamanho ' + str(self.currentState))
        print('Aplicando algoritmo...')
        self.states[self.currentState] += (event['time'] - self.previousTime)
        setTime(event['time'] - self.previousTime)
        print('ENTRADA TEMPO ' + str(self.states[self.currentState]) + ' EM ' + self.index + ' ' + str(self.currentState))
        self.previousTime = event['time']
        self.currentState -= 1
        print('Fila ' + str(self.index) + ' AGORA ATUALIZADA esta de tamanho ' + str(self.currentState))
        if self.currentState >= self.server:
            shuffle = self.shuffle_exit(generator)
            self.schedule_exit(event['time'],shuffle,events)
