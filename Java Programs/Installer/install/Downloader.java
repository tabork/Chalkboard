package install;

import org.apache.commons.io.IOUtils;
import org.apache.commons.net.ftp.FTPClient;
import org.apache.commons.net.ftp.FTPFile;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;

import javax.swing.*;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.*;
import java.net.URL;
import java.util.ArrayList;

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
	public static String installPath;
	private String server, un, pw;
	
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

			if(!file.getName().equals(".") && !file.getName().equals("..") && !file.getName().equals(".htaccess") && !file.getName().equals(".ftpquota"))
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

	private void readXML()
	{

		try
		{

			File fXmlFile = new File("ftpinfo.xml");
			DocumentBuilderFactory dbFactory = DocumentBuilderFactory.newInstance();
			DocumentBuilder dBuilder = dbFactory.newDocumentBuilder();
			Document doc = dBuilder.parse(fXmlFile);

			doc.getDocumentElement().normalize();

			NodeList nList = doc.getElementsByTagName("ftp");

			Node nNode = nList.item(0);

			System.out.println("\nCurrent Element :" + nNode.getNodeName());

			if(nNode.getNodeType() == Node.ELEMENT_NODE)
			{

				Element eElement = (Element) nNode;
				server = eElement.getElementsByTagName("server").item(0).getTextContent();
				un = eElement.getElementsByTagName("un").item(0).getTextContent();
				pw = eElement.getElementsByTagName("pw").item(0).getTextContent();

			}

		} catch(Exception e)
		{
			e.printStackTrace();
		}

	}
	
	public void Download(int hours) throws IOException{
		readXML();
		current = 0;
		client = new FTPClient();
		try {
			client.connect(server);
			System.out.println("connected");
			client.login(un, pw);
			client.enterLocalPassiveMode();
			System.out.println("Logged in");
			FTPFile[] files = client.listFiles("/");
			totalFileSizes = getTotalFileSizes(files);
			installPath = "C:\\Program Files (x86)\\Chalkboard\\";
			System.out.println(Double.toString( totalFileSizes));
			new Registry().write(GUID, installPath, (int) Math.round(totalFileSizes/1000));
			pathList = new ArrayList<String>();
			getPaths("/");
			paths = pathList.toArray(new String[pathList.size()]);
			amtTotal = paths.length;
			System.out.println(Integer.toString(amtTotal));
			System.out.println("Made connections");
			String arch = System.getProperty("os.arch");
			x86 = (arch.contains("64")) ? false : true;
			if(x86)
				installPath = "C:\\Program Files\\Chalkboard\\";
			else
				installPath = "C:\\Program Files (x86)\\Chalkboard\\";

			new File(installPath).mkdirs();
			
			for(String path : paths)
			{
				boolean fileDownloaded = false;
				int exceptionCounter = 0;
				
				while(!fileDownloaded)
				{
					String p = path;
					try
					{
						
						fileLabel.setText(path);
						path = installPath + path;
						URL dl = new URL("http://" + server + "/Chalkboard" + p);
						OutputStream os = new FileOutputStream(new File(path));
						InputStream is = dl.openStream();
						DownloadCountingOutputStream countStream = new DownloadCountingOutputStream(os);
						countStream.setListener(new ProgressListener());
						totalSize = Double.parseDouble(dl.openConnection().getHeaderField("Content-Length"));
						IOUtils.copy(is, countStream);
						amtDownloaded++;
						int pd = (int) Math.round((((double) amtDownloaded)/((double) amtTotal))*100);
						changeBar(totalBar, pd);
						
						if((double) current == totalSize)
							fileDownloaded = true;
					}
					catch(Exception e)
					{
						
						path = p;
						exceptionCounter++;
						e.printStackTrace();
						
						if(exceptionCounter == 5)
						{
							
							JOptionPane.showMessageDialog(null, "There has been an error installing.", "Error", JOptionPane.ERROR_MESSAGE);
							finish("Downloading due to error");
							
						}
						
						continue;
						
					}
				}
				
			}
			client.disconnect();
		} catch (IOException e) {
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
