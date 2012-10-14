package update;

import java.io.File;
import java.io.IOException;
import java.net.MalformedURLException;
import java.util.Formatter;
import java.util.Scanner;

import javax.swing.JOptionPane;

public class Update {
	public void runUpdate() throws IOException{
		File updater;
		if(new File("C:\\Program Files (x86)").isDirectory()){
			updater = new File("C:\\Program Files (x86)\\Chalkboard\\updater.exe");
		}
		else{
			updater = new File("C:\\Program Files\\Chalkboard\\updater.exe");
		}
		if(updater.exists()){
			Runtime.getRuntime().exec(updater.toString());
		}
		else{
			System.out.println("Update Failed");
			new Update();
		}
	}
	public Update() throws MalformedURLException, IOException{
		int update = JOptionPane.showConfirmDialog(null, "Update Available. Would you like to update?", "Update", JOptionPane.YES_NO_OPTION);
		if(update == JOptionPane.YES_OPTION){
			new Downloader();
			runUpdate();
		}
		else{
			File updated;
			if(new File("C:\\Program Files (x86)").isDirectory()){
				updated = new File("C:\\Program Files (x86)\\Chalkboard\\updated.txt");
			}
			else{
				updated = new File("C:\\Program Files\\Chalkboard\\updated.txt");
			}
			Formatter f = new Formatter(updated);
			f.format("false");
			f.close();
		}
	}
}
