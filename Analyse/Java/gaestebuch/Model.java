

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;

public class Model {
	String gaestebuchDatei = "gaestebuch.txt";

	InputStream in;
	OutputStream out;

	public int speichern(String text) {
		StringBuffer inhalt = new StringBuffer();
		int zeichen = 0;
		try {
			in = new FileInputStream(gaestebuchDatei);

			while (zeichen != -1) {
				zeichen = in.read();

				inhalt.append((char) zeichen);

			}
			in.close();
		} catch (FileNotFoundException e) {
			// Falls Gästebuchdatei noch nicht vorhanden, erstelle diese
			try {
				System.out.println("Gästebuch noch nicht vorhanden. Wird erstellt.");
				out = new FileOutputStream(gaestebuchDatei);

				out.close();
			} catch (IOException e1) {

				e1.printStackTrace();
			}

		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		inhalt.append(text);
		inhalt.append("\r\n*******\r\n");
		try {
			out = new FileOutputStream(gaestebuchDatei);
			for (int i = 0; i < inhalt.length(); i++) {
				zeichen = (int) inhalt.charAt(i);
				if (zeichen < 65535)
					out.write(zeichen);
			}
			inhalt.delete(0, inhalt.length());
			out.close();
		} catch (IOException e1) {

			e1.printStackTrace();
		}

		return 0;
	}

	public String lesen() {
		StringBuffer inhalt = new StringBuffer();
		int zeichen = 0;
		try {
			in = new FileInputStream(gaestebuchDatei);

			while (zeichen != -1) {
				zeichen = in.read();

				inhalt.append((char) zeichen);

			}
			in.close();
		} catch (FileNotFoundException e) {
			System.out.println("Gästebuch noch nicht vorhanden.");
		} catch (IOException e) {

		}

		return inhalt.toString();
	}
}
