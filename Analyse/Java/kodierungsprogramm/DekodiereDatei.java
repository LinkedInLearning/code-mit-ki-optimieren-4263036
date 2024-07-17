
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;

public class DekodiereDatei {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		// TODO Auto-generated method stub
		int zeichen=0;
		try {
			InputStream in = new FileInputStream(args[0]);
			OutputStream out = new FileOutputStream(args[1]);
			while(zeichen!=-1) {
			  zeichen = in.read();
			  //System.out.print((char)zeichen);
			  out.write((zeichen-3)%256);
			}
			in.close();
			out.close();
		}
		catch (ArrayIndexOutOfBoundsException e) {
			System.out.println("Das Programm verlangt zwei Parameter (Quell- und Zieldatei).");
		}
		catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		System.out.println("Dekodierung beendet");
	}

}
