'''
Funcao do Congruente Linear que gera os numeros pseudo-aleatorios
Foi necessario criar uma classe pois iremos declarar ele, para entao
chama-lo varias vezes (como um iterator). Por esta razao, ele deve
ser declarado APENAS uma vez para que matenha a consistencia na geracao
de numeros pseudo aleatorios, por isso ele e chamada no main e passado
para as filas, ao inves de ser chamado nas filas, pois senao iriamos
declarar diversos, gerando em grande parte o mesmo numero aleatorio.
'''
class Generator:
    
    # Estes sao os valores de entrada inicial quando o Gerador e chamado pela primeira vez.
    # Perceba que o X vai mudar constantemente, enquanto os outros tres valores
    # permanecerao constantes.
    x_seed = 19
    M = 4493
    a = 500
    c = 4

    # Chama-se esta funcao para realizar a conta e gerar um numero. O seed sera atualizado.
    def generate(self):
        
        self.x_current = ((self.a * self.x_seed) + self.c) % self.M
        self.x_seed = self.x_current

        return (self.x_current / self.M)
