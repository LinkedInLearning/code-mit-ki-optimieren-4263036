

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class View extends JFrame{
	JTextArea ta = new JTextArea();
	JTextArea eintraege = new JTextArea();
	
	JButton btn = new JButton("Eintrag hinzufügen");
	JScrollPane scroll = new JScrollPane (ta);
	JScrollPane scroll2 = new JScrollPane (eintraege);
	View(){
		this.setSize(600, 500);
		this.setDefaultCloseOperation(EXIT_ON_CLOSE);
		this.setTitle("Gästebuch");
		this.eintraege.setEditable(false);
		
		this.add(scroll);
		this.add(btn,BorderLayout.NORTH);
		this.add(scroll2,BorderLayout.EAST);
	}


}
