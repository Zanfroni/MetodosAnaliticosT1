from reader import read
from queue import Queue

def launch():
    
    read_queues = read()
    print()
    print()
    print()
    print(read_queues)
    print()
    print(read_queues[1]['exit'][1])
    
    # Variaveis importantes que podem ser alteradas
    actual_time = 2
    iterations = 1000
    
    # Variaveis importantes que nao devem ser alteradas
    current_iteration = 0
    events = [ {'queue':'Q1','event':'ch','time':actual_time,'shuffle':actual_time} ]
    all_queues = []
    
    # Agora, cria as filas
    for i in read_queues:
        print('okay ' + i['capacity'])
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
        event = fetch_event(events) # cuida pra ver se events é realmente manipulada
        
        # Agora, com o evento, deve-se ver se ele e CH ou SA e contabilizar de acordo
        # Tem que tambem ver se ele e intermediario ou nao
        selectedQueue = '-1'
        for i in all_queues:
            print('oi ' + i.getId())
            print('tchu ' + event['queue'])
            if i.getId() == event['queue']: selectedQueue = i
                        
        print('got here ' + selectedQueue.getId())
        
        #BELEZA, FOI ESSA BOSTA!!
        
        if event['event'] == 'ch': print('CONTABILIZA')
        elif event['event'] == 'sa': print('CAGABILIZA')
        
        
        
def fetch_event(events):
    candidate = events.pop(0)
    for event in events:
        if event['time'] < candidate['time']:
            events.append(cadidate)
            candidate = event
            events.remove(event)
    return candidate
            


if __name__ == "__main__":
    launch()
