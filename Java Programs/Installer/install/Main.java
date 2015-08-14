package install;
import java.io.IOException;
import java.util.Calendar;
import java.util.TimeZone;

import javax.swing.JFrame;

public class Main {
	
	public static void main(String[] args) 
	{
		
		Calendar calendar = Calendar.getInstance();
		TimeZone timeZone = calendar.getTimeZone();
		System.out.println(timeZone.getDisplayName());
		TimeZone pacific = TimeZone.getTimeZone("PST");
		System.out.println(pacific.getDisplayName());
		int difference = timeZone.getRawOffset() - pacific.getRawOffset();
		int hours = difference / 3600000;
		System.out.println(Integer.toString(hours));
		
		try {
			Downloader downloader = new Downloader("Downloading");
			downloader.setSize(640,320);
			downloader.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
			downloader.setVisible(true);
			downloader.Download(hours);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}

}
