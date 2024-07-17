
import java.io.*;

public class KodiereDatei {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int zeichen=0;
		try {
			InputStream in = new FileInputStream(args[0]);
			OutputStream out = new FileOutputStream(args[1]);
			while (zeichen != -1) {
				zeichen = in.read();
				// System.out.print((char)zeichen);
				out.write((3 + zeichen) % 256);
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
		System.out.println("Kodierung beendet");

	}
}
