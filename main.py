import sys
from reader import read
from queue import Queue
from generator import Generator
from timer import getTime

def launch():
    
    read_queues = read()
    
    # Variaveis importantes que podem ser alteradas
    actual_time = 2
    iterations = 1000
    
    # Variaveis importantes que nao devem ser alteradas
    generator = Generator()
    current_iteration = 0
    events = [ {'queue':'Q1','event':'ch','time':actual_time,'shuffle':0} ]
    all_queues = []
    
    # Agora, cria as filas
    for i in read_queues:
        newQ = Queue(i['id'].replace('\n',''),
                                i['next'],
                                i['same'],
                                i['out'],
                                i['server'],
                                i['capacity'],
                                i['arrival'],
                                i['exit'])
        all_queues.append(newQ)
    
    # Finalmente, da inicio a simulacao, contando as iteracoes
    while True:
        if current_iteration >= iterations: break
        current_iteration += 1
        print('\n')
        print('ESTAMOS NA ITERACAO ' + str(current_iteration))
        event = fetch_event(events) # cuida pra ver se events é realmente manipulada
        actual_time += event['shuffle']
        
        # Agora, com o evento, deve-se ver se ele e CH ou SA e contabilizar de acordo
        # Tem que tambem ver se ele e intermediario ou nao
        selectedQueue = '-1'
        for i in all_queues:
            if i.getId() == event['queue']: selectedQueue = i
        
        if event['event'] == 'ch': selectedQueue.cont_arrival(event,events,generator)
        elif event['event'] == 'sa': selectedQueue.cont_exit(event,events,generator)
    
    print('\n')
    print('RESULTADOS FINAIS:')
    print('==================')
    print('\n')
    print('TEMPOS DE EXECUCAO')
    print('------------------')
    print('LEGENDA: [(estado, tempo), (estado, tempo),...]')
    print('\n')
    printTime(all_queues)
    print('\n')
    print('DISTRIBUICAO E PERDAS')
    print('---------------------')
    printResults(all_queues)
    
def printResults(all_queues):
    for queue in all_queues:
        print('FILA ' + queue.getId() + ':')
        newQ = queue.getStates()
        totalSum = 0
        for i in range(len(newQ)):
            totalSum += newQ.get(i)
        # tenho minha soma
        for i in range(len(newQ)):
            percent = newQ.get(i)
            print('{0:.2f}%'.format(((percent/totalSum)*100)))
        print('NUMERO DE LOSSES DA FILA: ' + str(queue.getLoss()))
        print()
        
	
        
def printTime(all_queues):
    for queue in all_queues:
        print('Fila ' + queue.getId(), end=' ')
        newQ = queue.getStates()
        print(newQ.items())
        #print('LOSS DA FILA = ' + str(queue.getLoss()))
    print('TEMPO DA SIMULACAO = ' + str(getTime()) + ' segundos')
        
def fetch_event(events):
    candidate = 0
    time = sys.maxsize
    for event in events:
        if event['time'] < time: time = event['time']
    for event in events:
       if event['time'] == time:
           candidate = event
           events.remove(event)
    return candidate
            


if __name__ == "__main__":
    launch()
