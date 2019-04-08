
public class FilaSimples {

	private int server, cap, inA, inB, outA, outB;
	private double time;
	private int fila = 0;
	private Generator g = new Generator();
	private int j = 0;

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
	
	public void startSimulation(){
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
	
}
