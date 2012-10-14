import java.io.File;
import java.io.FileNotFoundException;
import java.util.Formatter;


public class Main {
	public static void main(String args[]) throws FileNotFoundException{
		Formatter f = new Formatter(new File("updated.txt"));
		f.format("true");
		f.close();
	}
}
