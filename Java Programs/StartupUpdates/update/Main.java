package update;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.net.URL;
import java.util.Scanner;

import javax.swing.JFrame;

import org.apache.commons.io.*;

public class Main {
	
	public static File ufile;
	public static File vfile;

	public static boolean checkForUpdates() throws FileNotFoundException{
		Scanner uscan = new Scanner(ufile);
		Scanner vscan = new Scanner(vfile);
		String u = "";
		while (uscan.hasNextLine()){
			u += uscan.nextLine();
		}
		String v = "";
		while (vscan.hasNextLine()){
			v += vscan.nextLine();
		}
		if(u.equals(v)){
			uscan.close();
			vscan.close();
			return false;
		}
		else{
			uscan.close();
			vscan.close();
			return true;
		}
	}
	public static void main(String[] args) throws IOException {
		if(new File("C:\\Program Files (x86)").isDirectory()){
			ufile = new File("C:\\Program Files (x86)\\Chalkboard\\update.txt");
			vfile = new File("C:\\Program Files (x86)\\Chalkboard\\version.txt");
		}
		else{
			ufile = new File("C:\\Program Files\\Chalkboard\\update.txt");
			vfile = new File("C:\\Program Files\\Chalkboard\\version.txt");
		}
		FileUtils.copyURLToFile(new URL("http://www.kamakwazee.net/Chalkboard/version.txt"), ufile);
		if(checkForUpdates()){
			new Update();
		}
	}

}
