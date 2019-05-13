import sys

'''
Funcao que realiza a leitura do arquivo de entrada que vai definir as filas.
O objetivo e criar uma matriz que ira conter as informacoes de cada fila para que
entao sejam construidas. As tabelas de eventos para que seja realizada a simulacao.

O read() e bastante simples. Ele cria uma matriz (seria uma lista de listas no Python)
que em cada linha representa uma fila, onde as colunas contem os dados
No laco, cada parte le uma informacao e guarda em uma coluna/lista diferente para
que depois seja facil de acessar.

Por exemplo, se eu quiser acessar fila 4, parte server, so digitar queues[3]['server']
que ele imediatamente retorna o valor guardado
'''
def read():
    try:
        with open('chanin.txt', 'r') as f:
            # Tamanho da fila
            queueSize = int(f.readline().strip().replace('Size ',''))
            
            # Matriz final
            all_queues = []
            
            # A quantidade de iteracoes e representada pela quantidade lida, logo deve estar de acordo
            for i in range(1, queueSize + 1):
                
                # Le cada linha e vai guardando em posicoes diferentes
                f.readline()
                new_queue = {}
                
                newline = f.readline().strip()
                new_queue['id'] = newline
                
                newline = f.readline().strip().replace('Next ','')
                new_queue['next'] = newline
                
                newline = f.readline().strip().replace('Same ','')
                new_queue['same'] = newline
                
                newline = f.readline().strip().replace('Out ','')
                new_queue['out'] = newline
                
                newline = f.readline().strip().replace('C ','')
                new_queue['server'] = newline
                
                newline = f.readline().strip().replace('K ','')
                new_queue['capacity'] = newline
                
                newline = f.readline().strip().replace('CH ','')
                new_queue['arrival'] = newline.split('..')
                
                newline = f.readline().strip().replace('SA ','')
                new_queue['exit'] = newline.split('..')
                
                all_queues.append(new_queue)
        
        return all_queues
        
    except:
        print('Ocorreu um erro na leitura do arquivo')
        sys.exit()
