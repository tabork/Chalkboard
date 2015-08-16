package install;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.URL;
import java.util.ArrayList;

import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JProgressBar;

import org.apache.commons.io.IOUtils;
import org.apache.commons.net.ftp.FTPClient;
import org.apache.commons.net.ftp.FTPFile;

public class Downloader extends JFrame{

	/**
	 *
	 */
	private static String GUID = "454f42d9-6f6e-48be-804d-e275fb4a97ed";
	private static final long serialVersionUID = 4237530638084074684L;
	public static JProgressBar currentBar, totalBar;
	public static JLabel fileLabel;
	public static double totalSize;
	public static long current, currentPrev;
	public static int percentage, pd;
	public static int loop = 0;
	public static double totalFileSizes;
	public static double currentFileSizes;
	public static String[] paths;
	public static FTPClient client;
	public static ArrayList<String> pathList;
	public static int amtDownloaded, amtTotal;
	public static boolean x86;
	
	private static class ProgressListener implements ActionListener{
		
		public void actionPerformed(ActionEvent e){
			
			currentPrev = current;
			current = ((DownloadCountingOutputStream) e.getSource()).getByteCount();
            percentage = (int) Math.round((current/totalSize)*100);
			changeBar(currentBar, percentage);
			
		}
		
	}

	public Downloader(String dn) throws IOException{
		super (dn);
		setLayout(null);
		fileLabel = new JLabel("");
		fileLabel.setBounds(25, 30, 575, 20);
		add(fileLabel);
		currentBar = new JProgressBar();
		currentBar.setBounds(25, 50, 575, 50);
		add(currentBar);
		totalBar = new JProgressBar();
		totalBar.setBounds(25, 150, 575, 50);
		add(totalBar);
	}
	
	private double getTotalFileSizes(FTPFile[] files)
	{
		
		double totalSizes = 0;
		
		for(FTPFile file : files)
		{
			
			if(!file.isDirectory() && !file.getName().equals(".") && !file.getName().equals("..") && !file.getName().equals(".htaccess"))
				totalSizes += (double) file.getSize();
			
		}
		
		return totalSizes;
		
	}
	
	private void getPaths(String path) throws IOException
	{
		
		FTPFile[] files = client.listFiles(path);
		for(FTPFile file : files)
		{
			
			if(!file.getName().equals(".") && !file.getName().equals("..") && !file.getName().equals(".htaccess"))
			{
				
				if(file.isDirectory())
				{
					
					getPaths(path + file.getName() + "/");
					if(x86)
						new File("C:\\Program Files\\Chalkboard\\" + path + file.getName() + "\\").mkdirs();
					else
						new File("C:\\Program Files (x86)\\Chalkboard\\" + path + file.getName() + "\\").mkdirs();
					
				}
				else
				{
					
					pathList.add(path + file.getName());
					
				}
				
			}
			
		}
		
	}
	
	public void Download(int hours) throws IOException{
		current = 0;
		client = new FTPClient();
		try {
			client.connect("kamakwazee.net");
			System.out.println("connected");
			client.login("chalkboardinst", "Chalkb0ard!nst");
			client.enterLocalPassiveMode();
			System.out.println("Logged in");
			FTPFile[] files = client.listFiles("/Chalkboard");
			totalFileSizes = getTotalFileSizes(files);
			pathList = new ArrayList<String>();
			getPaths("/");
			paths = pathList.toArray(new String[pathList.size()]);
			amtTotal = paths.length;
			System.out.println(Integer.toString(amtTotal));
			System.out.println("Made connections");
			String arch = System.getProperty("os.arch");
			x86 = (arch.contains("64")) ? false : true;
			if(x86)
				new File("C:\\Program Files\\Chalkboard\\").mkdirs();
			else
				new File("C:\\Program Files (x86)\\Chalkboard\\").mkdirs();
			for(String path : paths)
			{
				
				String p = path;
				fileLabel.setText(path);
				if(x86)
					path = "C:\\Program Files\\Chalkboard\\" + path;
				else
					path = "C:\\Program Files (x86)\\Chalkboard\\" + path;
				
				URL dl = new URL("http://kamakwazee.net/Chalkboard/" + p);
				OutputStream os = new FileOutputStream(new File(path));
				InputStream is = dl.openStream();
				DownloadCountingOutputStream countStream = new DownloadCountingOutputStream(os);
				countStream.setListener(new ProgressListener());
				totalSize = Double.parseDouble(dl.openConnection().getHeaderField("Content-Length"));
				IOUtils.copy(is, countStream);
				amtDownloaded++;
				int pd = (int) Math.round((((double) amtDownloaded)/((double) amtTotal))*100);
				changeBar(totalBar, pd);
				
			}
			client.disconnect();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		finally
		{
			
			finish("Downloading");
			
		}
	}
	
	public static void changeBar(JProgressBar bar, int p){
		bar.setValue(p);
		bar.setStringPainted(true);
		bar.update(bar.getGraphics());
	}
	
	public void finish(String dn){
		System.out.println("Finished " + dn);
		setVisible(false);
		dispose();
	}
	
}
