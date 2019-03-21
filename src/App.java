import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

/**
 * 
 * @author Annderson Packeiser
 * @author Gabriel Franzoni
 *
 */

public class App {
	
	private static final String FILENAME = "chanin.txt";
	
	public static void main(String[] args) {
		
		FileReader fr = null;
		BufferedReader br = null;
		
		try {
			
			fr = new FileReader(FILENAME);
			br = new BufferedReader(fr);
			
			String sCurrentLine;
			
			while ((sCurrentLine = br.readLine()) != null) {
				System.out.println(sCurrentLine);
			}
			
		} catch (IOException e) {
			
			e.printStackTrace();
			
		} finally {
			
			try {
				
				if (br != null) br.close();
				if (fr != null) fr.close();
				
			} catch (IOException ex) {
				
				ex.printStackTrace();
				
			}
			
			System.out.println("Oi gatinha!!");
			
		}
		
	}
	
}
