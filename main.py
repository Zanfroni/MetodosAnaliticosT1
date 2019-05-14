import sys
from reader import read
from queue import Queue
from generator import Generator
from timer import getTime

'''
Funcao que serve como principal para execucao da simulacao.
launch() serve como o hub principal para a simulacao, onde
o arquivo de entrada sera lido e a informacoes executadas na
simulacao
'''

def launch():
    
    # Le o arquivo de entrada
    read_queues = read()
    
    # OBS: Variaveis importantes que podem ser alteradas
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
        try:
            if current_iteration >= iterations: break
            current_iteration += 1
            print('\n')
            print('ESTAMOS NA ITERACAO ' + str(current_iteration))
            event = fetch_event(events)
            actual_time += event['shuffle']
			
            # Agora, com o evento, deve-se ver se ele e CH ou SA e contabilizar de acordo
            selectedQueue = '-1'
            for i in all_queues:
                if i.getId() == event['queue']: selectedQueue = i
			
            if event['event'] == 'ch': selectedQueue.cont_arrival(event,events,generator)
            elif event['event'] == 'sa': selectedQueue.cont_exit(event,events,generator)
        except:
            print('Ocorreu um erro durante a simulacao')
            sys.exit()
    
    # Nesta secao, serao impressos todos os resultados da simulacao
    # das N filas.
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
    print('TEMPO DA SIMULACAO = ' + str(getTime()) + ' segundos')
        

# Esta pequena funcao sera nossa fila de prioridade.
# Ela ira percorrer toda a lista de eventos procurando pelo
# menor tempo. Quando encontrar o menor tempo, ele remove da
# lista o evento com menor tempo e o retorna para ser executado        
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
            

'''
Inicia o algoritmo
'''
if __name__ == "__main__":
    launch()
