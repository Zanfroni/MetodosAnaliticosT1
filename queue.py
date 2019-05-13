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
            
    def cont_arrival(self,event,events,generator):
        print('Fila ' + str(self.index) + ' esta de tamanho ' + str(self.currentState))
        print('Aplicando algoritmo...')
        if self.currentState < self.capacity:
            self.states[self.capacity] += event['time'] - self.previousTime
            self.previousTime = event['time']
            self.currentState += 1
            if self.currentState <= self.server:
                shuffle = self.shuffle_exit(generator)
                schedule_exit(event['time'],shuffle,events)
        else: loss += 1
        shuffle = self.shuffle_arrival(generator)
        schedule_arrival(event['time'],shuffle,events)
            
    def cont_exit(self,event,events,generator):
        print('Fila ' + str(self.index) + ' esta de tamanho ' + str(self.currentState))
        print('Aplicando algoritmo...')
        self.states[self.capacity] += event['time'] - self.previousTime
        self.previousTime = event['time']
        self.currentState -= 1
        if self.currentState >= self.server:
            shuffle = self.shuffle_exit(generator)
            schedule_exit(event['time'],shuffle,events)


    # ABANDONADO. ENCONTROU-SE UMA SOLUCAO MUITO MAIS SIMPLES!!!
    
    '''
    RETHINK HOW I'M GONNA SHARE THE WORK
    def cont_arrival(self,event,events,generator):
        print('Fila ' + str(self.index) + ' esta de tamanho ' + str(self.currentState))
        print('Aplicando algoritmo...')
        if self.currentState < self.capacity:
            self.states[self.capacity] += event['time'] - self.previousTime
            self.previousTime = event['time']
            self.currentState += 1
            if self.currentState <= self.server:
                if(self.shuffle_probability() < self.nextQueue):
                    # AQUI ELE AGENDA A ENTRADA PARA O PROXIMO (SAIDA DESTE)
                    shuffle = self.shuffle_exit(generator)
                    mark_tandem(event['time'],shuffle,events)
                elif self.sameRotation == 0:
                    # AGENDA PARA ELE MESMO
                    shuffle = self.shuffle_exit(generator)
                    mark_exit(event['time'],shuffle,events)
                else:
                    shuffle = self.shuffle_exit(generator)
                    mark_rotation(event['time'],shuffle,events)
        else: self.loss += 1
        shuffle = self.shuffle_arrival(generator)
        mark_arrival(event['time'],shuffle,events)
        
    def cont_exit(self,event,events,generator):
        print('Fila ' + str(self.index) + ' esta de tamanho ' + str(self.currentState))
        print('Aplicando algoritmo...')
        self.currentState -= 1
        if self.currentState >= server:
            if(self.shuffle_probability() < self.nextQueue):
                shuffle = self.shuffle_exit(generator)
                mark_tandem(event['time'],shuffle,events)
            else:
                shuffle = self.shuffle_exit(generator)
                mark_exit(event['time'],shuffle,events)
        
    def cont_final(self,event,events,generator):
        print('Fila ' + str(self.index) + ' esta de tamanho ' + str(self.currentState))
        print('Aplicando algoritmo...')
        self.currentState -= 1
        if self.currentState >= server:
            shuffle = self.shuffle_exit(generator)
            mark_final(event['time'],shuffle,events)
        
    def mark_arrival(self,time,shuffle,events):
        events.append({'queue':self.index,'event':'ch','time':time + shuffle,'shuffle':shuffle})
        
    def mark_rotation(self,time,shuffle,events):
        events.append({'queue':self.index,'event':'rot','time':time + shuffle,'shuffle':shuffle})
        
    def mark_tandem(self,time,shuffle,events):
        events.append({'queue':self.index,'event':'pt','time':time + shuffle,'shuffle':shuffle})
    
    def mark_exit(self,time,shuffle,events):
        events.append({'queue':self.index,'event':'sa','time':time + shuffle,'shuffle':shuffle})
        
    def mark_final(self,time,shuffle,events):
        events.append({'queue':self.index,'event':'final','time':time + shuffle,'shuffle':shuffle})
    '''
