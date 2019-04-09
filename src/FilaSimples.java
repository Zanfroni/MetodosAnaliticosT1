import java.util.LinkedList;

public class FilaSimples {

	private int server, cap, inA, inB, outA, outB;
	private double time, prevTime = 0;
	private int fila = 0;
	private Generator g = new Generator();

	// iteradores
	private int it = 0;
	private int itEvent = 0;

	private double actualEvent = -1;
	private double auxIndex;

	// IMPORTANT STUFF
	private double table[][];
	private double eventTable[][];
	private double actualTime;
	
	//USELESS??
	private int auxit;

	public FilaSimples(int inA, int inB, int outA, int outB, int server, int cap, double time){
		this.inA = inA;
		this.inB = inB;
		this.outA = outA;
		this.outB = outB;
		this.server = server;
		this.cap = cap;
		this.time = time;
		table = new double[cap+3][25];
		eventTable = new double[3][100];
		actualTime = time;
	}

	public void startSimulation(){
		
		// Preenche TABLE com zeros
		table[0][0] = fila;
		table[0][1] = 0;
		for(int i = 0; i <= cap; i++){
			table[0][i+2] = 0;
		}

		// Preenche EVENT TABLE com o inicial     ----> 0 = Chegada e 1 = Saida
		eventTable[0][0] = 0;
		eventTable[0][1] = actualTime;


		// PRECISAR VER O EVENTO DA EVENT TABLE E REMOVER DELA. SE FOR -1 É QUE JA FOI REMOVIDO
		// ESTA PRIMEIRA PARTE ANTES DA ITERAÇÃO, ELE SEMPRE PEGA O PRIMEIRO
		actualEvent = eventTable[0][0];
		eventTable[0][0] = -1;
		eventTable[1][0] = 99999;
		eventTable[2][0] = 0;
		

		if(actualEvent == 0) chegada();
		else saida();

		int chosen = -2;
		while(it < 20){
			double lessTime = 9999;
			// procura o proximo evento
			for(int i =0;i <= itEvent; i++){
				if(eventTable[0][i] != -1.0){
					if(eventTable[1][i] < lessTime){
						lessTime = eventTable[1][i];
						chosen = i;
					}
				}
			}
			// terei um escolhido. preciso agr ver se e entrada ou saido (e botar -1) e iniciar a chegada/saida
			// tambem preciso atualizar o actualTime com o tempo sorteado dele
			if(eventTable[0][chosen] == 0){
				double notin = prevTime;
				double aux = actualTime;
				actualTime += eventTable[2][chosen];
				prevTime = aux;
				chegada();
				// aqui ele faz um especial caso fila esteja já cheia.
				if(auxit == it){
					actualTime = prevTime;
					prevTime = notin;
					table[fila+2][auxit] += (actualTime - prevTime);
					notin = prevTime;
					aux = actualTime;
					actualTime += eventTable[2][chosen];
					prevTime = aux;
				}
				eventTable[0][chosen] = -1;
				eventTable[1][chosen] = 99999;
			}
			else if(eventTable[0][chosen] == 1){
				double aux = actualTime;
				actualTime += eventTable[2][chosen];
				prevTime = aux;
				saida();
				eventTable[0][chosen] = -1;
				eventTable[1][chosen] = 99999;
			}
			else{
				break;
			}
		}
		System.out.println("\n\n\n\n\n\n\n\n\n");
		System.out.println("RESULTADOS FINAIS");
		System.out.print(table[0][it] + " ");
		System.out.printf("%.3f  ", table[1][it]);
		for(int i = 0; i <= cap; i++){
			System.out.printf("%.3f  ", table[i+2][it]);
		}
		System.out.println("\n\n");

		System.out.println("\n\n\n\n\n\n\n\n\n");
		System.out.println("TABELA (FILA, TEMPO, 0, 1, 2, 3...N)");
		for(int j = 0; j  <= cap+2; j++){
			for(int i = 0; i <= it; i++){
				System.out.printf("%.2f | ", table[j][i]);
			}
			System.out.println();
		}
		// DEBUGGAR, caso queira ver a tabela dos eventos
		/*System.out.println("\n\n\n\n\n\n\n\n\n");
		for(int j = 0; j  <= 2; j++){
			for(int i = 0; i < itEvent; i++){
				System.out.printf("%.2f | ", eventTable[j][i]);
			}
			System.out.println("\n\n\n\nCHECKPOINT\n\n\n\n\n");
		}
		System.out.println("\n\n\n\n\n\n\n\n\n");*/

		// CALCULO DE PROPORCAO

		double calculo;
		for(int i = 0; i <= cap; i++){
			calculo = table[2+i][it]/actualTime;
			System.out.printf("%.2f porcento",calculo*100);
			System.out.println();
		}
		System.out.print("TOTAL 100 porcento");
		System.out.println();
		
	}

	public void chegada(){
		auxit = it;
		if (fila < cap){
			it++;
			// PREENCHE A TABLE COM TODOS OS VALORES ANTERIORES
			for(int i = 0; i <= cap+2; i++){
				table[i][it] = table[i][it-1];
			}

			// AGORA ALTERAMOS, PREENCHENDO APENAS O TEMPO NOVO
			table[fila+2][it] = table[fila+2][it-1] + (actualTime - prevTime);
			//BOTA O TEMPO
			table[1][it] = actualTime;
			//Agora bota o tamanho da fila atual (ALGORITMO)
			fila++;
			table[0][it] = fila;
			if(fila <= server) {
				agendaSaida();
			}
		}
		agendaEntrada();
	}

	public void saida(){
		it++;
		// PREENCHE A TABLE COM TODOS OS VALORES ANTERIORES
		for(int i = 0; i <= cap+2; i++){
			table[i][it] = table[i][it-1];
		}
		// AGORA ALTERAMOS, PREENCHENDO APENAS O TEMPO NOVO
		table[fila+2][it] = table[fila+2][it-1] + (actualTime - prevTime);
		//BOTA O TEMPO
		table[1][it] = actualTime;
		//Agora bota o tamanho da fila atual (ALGORITMO)
		fila--;
		table[0][it] = fila;
		if(fila >= server) {
			agendaSaida();
		}
	}
	
	public void agendaEntrada(){
		itEvent++;
		double sorteio = (inB-inA) * g.nextRandom() + inA;
		eventTable[2][itEvent] = sorteio;
		eventTable[1][itEvent] = sorteio+actualTime;
		eventTable[0][itEvent] = 0;
	}

	public void agendaSaida(){
		itEvent++;
		double sorteio = (outB-outA) * g.nextRandom() + outA;
		eventTable[2][itEvent] = sorteio;
		eventTable[1][itEvent] = sorteio+actualTime;
		eventTable[0][itEvent] = 1;
	}

}
