package gaestebuch;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Controler {
/**
 * Startmethode
 * @param args
 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		View v = new View();
		Model m = new Model();
		v.setVisible(true);
		v.eintraege.setText(m.lesen());
		v.btn.addActionListener(new ActionListener() {

			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				if(!v.ta.getText().equals("")) {
					m.speichern(v.ta.getText());
					v.eintraege.setText(m.lesen());	
					v.ta.setText(null);
					
				}
			}
			
		});
		
	}

}
