package launch;

import java.io.File;
import java.io.IOException;
import java.net.MalformedURLException;
import java.util.Formatter;
import java.util.Scanner;

import javax.swing.JOptionPane;

public class Update {
	public void runUpdate() throws IOException{
		if(new File("updater.exe").exists()){
			Runtime.getRuntime().exec("updater.exe");
			Scanner scan = new Scanner(new File("update.txt"));
			Formatter format = new Formatter(new File("version.txt"));
			format.format(scan.nextLine());
			format.close();
			scan.close();
		}
		else{
			System.out.println("Update Failed");
			new Update();
		}
		new File("update.txt").deleteOnExit();
		new File("updater.exe").deleteOnExit();
	}
	public Update() throws MalformedURLException, IOException{
		program program = new program();
		int update = JOptionPane.showConfirmDialog(null, "Update Available. Would you like to update?", "Update", JOptionPane.YES_NO_OPTION);
		if(update == JOptionPane.YES_OPTION){
			new Downloader();
			runUpdate();
			program.start();
		}
		else{
			Formatter f = new Formatter(new File("updated.txt"));
			f.format("false");
			f.close();
			program.start();
		}
	}
}
