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
	private double table[][] = new double[cap+3][25];
	private double eventTable[][] = new double[3][100];
	private double actualTime = time;

	public FilaSimples(int inA, int inB, int outA, int outB, int server, int cap, double time){
		this.inA = inA;
		this.inB = inB;
		this.outA = outA;
		this.outB = outB;
		this.server = server;
		this.cap = cap;
		this.time = time;
		System.out.println("DEBUGGING SHIT OKAYYY");
		System.out.println(inA);               // DEBUGGGGGGING SAHIT
		System.out.println(inB);
		System.out.println(outA);
		System.out.println(outB);
		System.out.println(server);
		System.out.println(cap);
		System.out.println(time);
	}
	
	// SIMULACAO AQUI DEVE SAIR OS RESULTADOS
	// DEADLINE PARA TERMINAR ISTO SERIA AMANHA
	// USAR AULA DE HOJE PARA TIRAR UMAS DUVIDAS SOBRE
	// CODIGO (ESTRUTURA, CONSISTENCIA E OTIMIZACAO)
	// OUTPUTS (DEVO ESCREVER?? IMPRIMIR... COMO CARALHOS GERAR GRAFICO)
	// DEIXEI PARA AMANHA PRA PROGRAMAR POIS DEPENDE DESSAS DUVIDAS
	
	/**public void startSimulation(){
		double table[][] = new double[cap+3][20];
		String eventTable[][] = new String[3][20];
		double actualTime = time;
		table[0][0] = fila;
		table[0][1] = 0.0;
		for (int i = 2; i < cap+3; i++) table[0][i] = 0.0;
		for (int i = 1; i < 20; i++) {
			chegada(i);
		}
	}

	public void chegada(int i) {
		if (fila < cap) {
			String aux[] = eventTable[j];
			eventTable[j][2] = null;
			for (int i = 0; i < eventTable.length; i++) {
				
			}
			= actualTime - table[i-1][1];
			fila++;
			table[i][0] = fila;
			if (fila <= server) {
				agendaSaida(table[i][1] + ((outB - outA) * g.nextRandom() + outA);
			}
		}
		agendaChegada(table[i][1] + ((inB - inA) * g.nextRandom() + inA);
	}

	public void saida(double rand) {
		fila--;
		if (fila >= 1) {
			agendaSaida(table[i][1] + ((outB - outA) * g.nextRandom() + outA);
		}
	}

	public void agendaSaida(double rand) {
		eventTable[j][0] = "s" + j;
		eventTable[j][1] = "" + (table[1][i] + rand);
		eventTable[j][2] = "" + rand;
		ordena();
	}

	public void agendaChegada(double rand) {
		eventTable[j][0] = "c" + j;
		eventTable[j][1] = "" + (table[1][i] + rand);
		eventTable[j][2] = "" + rand;
		ordena();
	}

	public void ordena() {
		for (int k = 0; k < eventTable.length-1; i++) {
		for (int i = 0; i < eventTable.length-1; i++) {
			if (eventTable[j+1][2] != null && eventTable[j][2] != null) {
			if (Double.parseDouble(eventTable[i][2]) > Double.parseDouble(eventTable[i][2])) {
				double aux = Double.parseDouble(eventTable[i][2]);
				eventTable[i][2] = eventTable[i+1][2];
				eventTable[i+1][2] = aux + "";
			}
			} else {
				break;
			}
		}
		}
	}
	**/


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

		if(actualEvent == 0) chegada();
		else saida();

		int chosen = -1;
		while(it < 20){
			double lessTime = 9999;
			// procura o proximo evento
			for(int i =0;i < itEvent; i++){
				if(eventTable[0][i] != -1){
					if(eventTable[1][i] < lessTime){
						lessTime = eventTable[1][i];
						chosen = i;
					}
				}
			}
			// terei um escolhido. preciso agr ver se e entrada ou saido (e botar 2) e iniciar a chegada/saida
			// tambem preciso atualizar o actualTime com o tempo sorteado dele
			double aux = actualTime;
			actualTime += eventTable[2][chosen];
			prevTime = aux;
			if(eventTable[0][chosen] == 0){
				chegada();
				eventTable[0][chosen] = -1;
			}
			else if(eventTable[0][chosen] == 1){
				saida();
				eventTable[0][chosen] = -1;
			}
			else return;
		}
	}

	public void chegada(){
		if (fila < cap){
			it++;
			// PREENCHE A TABLE COM TODOS OS VALORES ANTERIORES
			for(int i = 0; i <= cap+2; i++){
				table[i][it] = table[i][it-1];
			}

			// AGORA ALTERAMOS, PREENCHENDO APENAS O TEMPO NOVO
			table[fila+2][it] = actualTime - prevTime;
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
		table[fila+2][it] = actualTime - prevTime;
		//BOTA O TEMPO
		table[1][it] = actualTime;
		//Agora bota o tamanho da fila atual (ALGORITMO)
		fila--;
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
