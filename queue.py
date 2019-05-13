import random

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
        for i in range(self.capacity+1):
            self.states[i] = 0
        self.min_arrival = int(arrival[0])
        self.max_arrival = int(arrival[1])
        self.min_exit = int(exitTime[0])
        self.max_exit = int(exitTime[1])
        print(self.min_exit)
        print(self.states)

    def getId(self):
        return self.index
        
    # OBSERVACAO: Este aleatorio nao envolve nem entrada nem saida.
    # COMO O PROPRIO MATERIAL DE AULA MOSTRA, e um aleatorio qualquer
    # para decidir em qual rotacao a fila segue depois de simular um
    # passo, logo teve-se que se usar um random qualquer.
    def shuffle_probability(self):
        return random.uniform(0,1)
        
    def shuffle_arrival(self,generator):
        return (self.max_arrival - self.min_arrival) * generator.generate() + self.arrival
    
    def shuffle_exit(self,generator):
        return (self.max_exit - self.min_exit) * generator.generate() + self.min_exit

    ''' RETHINK HOW I'M GONNA SHARE THE WORK '''
    def cont_arrival(self,event,events,generator):
        print('Fila ' + self.index + ' esta de tamanho ' + self.currentState)
        print('Aplicando algoritmo...')
        if self.currentState < self.capacity:
            self.states[self.capacity] += event['time'] - previousTime
            self.previousTime = event['time']
            self.currentState += 1
            if self.currentState <= self.server:
                if(shuffle_probability() < self.nextQueue):
                    # AQUI ELE AGENDA A ENTRADA PARA O PROXIMO
                    shuffle = shuffle_exit(generator)
                elif self.sameRotation == 0:
                    # AGENDA PARA ELE MESMO
                    shuffle = shuffle
        return
        
    def cont_exit(self,event,events,generator):
        return
