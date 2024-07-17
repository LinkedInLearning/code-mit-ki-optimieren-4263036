import java.io.*;

public class KodiereDatei {
    public static void main(String[] args) {
        encodeFile(args);
    }
    
    private static void encodeFile(String[] args) {
        if (args.length < 2) {
            System.out.println("Das Programm verlangt zwei Parameter (Quell- und Zieldatei).");
            return;
        }

        try (InputStream in = new FileInputStream(args[0]);
             OutputStream out = new FileOutputStream(args[1])) {
            
            int currentByte;
            while ((currentByte = in.read()) != -1) {
                int encodedByte = (3 + currentByte) % 256;
                out.write(encodedByte);
            }
            
            System.out.println("Kodierung beendet");
            
        } catch (FileNotFoundException e) {
            System.out.println("Datei nicht gefunden: " + e.getMessage());
        } catch (IOException e) {
            System.out.println("Ein Fehler ist beim Lesen oder Schreiben aufgetreten: " + e.getMessage());
        }
    }
}
