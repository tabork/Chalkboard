package launch;

import java.io.File;
import java.io.IOException;
import java.net.MalformedURLException;
import java.util.Formatter;
import java.util.Scanner;

import javax.swing.JFrame;
import javax.swing.JOptionPane;

public class Update {
	
	private Downloader d;
	
	public void runUpdate() throws IOException{
		if(new File("update.exe").exists()){
			Runtime.getRuntime().exec("update.exe");
		}
		else{
			System.out.println("Update Failed");
			new Update();
		}
	}
	public void setup() throws MalformedURLException, IOException{
		d = new Downloader();
		d.setSize(620,300);
		d.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		d.setVisible(true);
	}
}
