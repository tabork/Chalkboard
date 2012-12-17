package launch;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.net.ConnectException;
import java.net.URL;
import java.net.UnknownHostException;
import java.util.Scanner;

import javax.swing.JFrame;

import org.apache.commons.io.*;

public class Main {

	public static boolean checkForUpdates() throws FileNotFoundException{
		Scanner uscan = new Scanner(new File("update.txt"));
		Scanner vscan = new Scanner(new File("version.txt"));
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
		program program = new program();
		try{
			FileUtils.copyURLToFile(new URL("http://www.kamakwazee.net/Chalkboard/version.txt"), new File("update.txt"));
			if(checkForUpdates()){
				new Update().setup();
			}
			else{
				program.start();
			}
		}
		catch(UnknownHostException uhe){
			program.start();
		}
		catch(ConnectException ce){
			program.start();
		}
	}

}
