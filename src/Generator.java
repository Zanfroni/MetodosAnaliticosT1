import java.util.*;
import java.io.*;
import java.text.DecimalFormat;

// Integrantes: Annderson Packeiser Oreto e Gabriel Franzoni

// Este e o gerador criado a partir da fórmula do Congruente Linear, implementado na linguagem Java

public class Generator {
		private  double[] v2 = new double[1000];
		public static int i = 0;

	// A classe principal verifica se teve 4 inputs de argumentos
	// Os argumentos devem ser respectivamente: a, c, X0 e M
	// Para que seja gerado números entre 0 a 1, algumas condicoes precisam ser atingidas:
	// --> a > 1, c < 1, X0 < 1 e M = 1. Deixamos para o usuario entrar qualquer numero como argumento para flexibilidade
	// O arquivo .txt anexado usa a = 3, c = 0.431, X0 = 0.56 e M = 1
	// OBS: Caso este codigo seja aproveitado em trabalhos futuros da disciplina, o mesmo sera adequadamente melhorado
	public Generator(){
		generate();
	}

	public double nextRandom() {
		return v2[i++];
	}

	// O metodo cria um PrintWriter para criar um .txt e escrever nele
	public void generate() {
		double a = 3;
		double c = 0.431;
		double x = 0.56;
		double m = 1;

		// Os valores que sao gerados pela formula abaixo sao guardados num
		// vetor de 1000 posicoes, ja que a intencao e gerar 1000 numeros por enquanto

		v2[0] = x;

		// Formula do Congruente Linear sendo aplicada
		for(int i = 1; i < v2.length; i++){
			v2[i] = ((a * v2[i-1]) + c) % m;
		}

		// Fecha o arquivo e termina a geração
	}

}
