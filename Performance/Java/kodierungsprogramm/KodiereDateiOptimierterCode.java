import java.io.*;

public class KodiereDateiOptimierterCode {
    public static void main(String[] args) {
        if (args.length < 2) {
            System.out.println("Das Programm verlangt zwei Parameter (Quell- und Zieldatei).");
            return;
        }

        try (InputStream in = new BufferedInputStream(new FileInputStream(args[0]));
             OutputStream out = new BufferedOutputStream(new FileOutputStream(args[1]))) {

            int zeichen;
            while ((zeichen = in.read()) != -1) {
                out.write((3 + zeichen) % 256);
            }

        } catch (FileNotFoundException e) {
            System.out.println("Datei nicht gefunden: " + e.getMessage());
        } catch (IOException e) {
            e.printStackTrace();
        }

        System.out.println("Kodierung beendet");
    }
}
