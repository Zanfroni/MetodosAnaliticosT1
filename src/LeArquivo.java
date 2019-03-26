import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;


public class LeArquivo {
	
	public LeArquivo() {
	}
		
	public ArrayList<String> getData(FileReader fr){
		BufferedReader br = null;
		ArrayList<String> data = new ArrayList<>();
		
		try {
			
			br = new BufferedReader(fr);
			
			String sCurrentLine;
			
			while ((sCurrentLine = br.readLine()) != null) {
				data.add(sCurrentLine);
				System.out.println(sCurrentLine); //DEBUG SHIT
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
			
			System.out.println("Oi gatinha!!"); //DEBUG SHIT
			
		}
		return data;
		
	}
}
