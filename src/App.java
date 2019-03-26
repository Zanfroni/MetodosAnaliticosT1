import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.Scanner;

/**
 * 
 * @author Annderson Packeiser
 * @author Gabriel Franzoni
 *
 */

// Nota-se que esta e uma versao prototipo simulando sucessivamente uma fila simples
// Documentacao apropriada, codigo consistente e otimizacoes estarao presentes na versao final
// Repositorio: https://github.com/Zanfroni/MetodosAnaliticosT1

public class App {
	
	public static void main(String[] args) throws FileNotFoundException {
		
		Scanner in = new Scanner(System.in);
		System.out.println("Digite o arquivo de entrada (com a extensão)");
		String inputFile = in.nextLine();
		
		try {
			
			FileReader file = new FileReader(inputFile);
			ArrayList<String> data = new ArrayList<>();
			LeArquivo read = new LeArquivo();
			data = read.getData(file);
			
			FilaSimples queue = new FilaSimples(getValues(data,0),
												getValues(data,1),
												getValues(data,2),
												getValues(data,3),
												getValues(data,4),
												getValues(data,5));
			//queue.
			
			for(String e : data){
				System.out.println(e); // DEBUG SHIT
			}
			
		} catch(FileNotFoundException e) {
			System.out.println("Arquivo não encontrado. Tente novamente...");
			System.exit(1);
		}
		
	}
	
	private static int getValues(ArrayList<String> list, int index){
		
		return Integer.parseInt(list.get(index));
		
	}
	
}
