package move;

import java.io.File;

public class Main {
	
	public static File f, m;
	public static File xp = new File("C:\\Documents and Settings\\All Users\\Start Menu\\Programs\\Startup");
	public static File v7 = new File("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Startup");

	public static void main(String[] args) {
		if(xp.isDirectory()){
			f = new File(xp.toString() + "\\ChalkboardUpdates.exe");
		}
		else if(v7.isDirectory()){
			f = new File(v7.toString() + "\\ChalkboardUpdates.exe");
		}
		m = new File("ChalkboardUpdates.exe");
		move(m,f);
	}

	public static void move(File m2, File f2) {
		boolean moved = m.renameTo(f);
		if(moved){
			System.out.println("Successful Install");
		}
		else{
			System.out.println("Failed Install");
		}
	}

}
