package launch;
import java.awt.BorderLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.Scanner;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JProgressBar;
import javax.swing.SwingUtilities;

import org.apache.commons.io.*;

public class Downloader extends JFrame{
	
	public static String progress;
	public static double totalSize;
	public static boolean start = true;
	public static long current;
	public static int percentage;
	public static String percent;
	public JLabel l;
    public static JProgressBar bar;
    public JButton yes;
    public JButton no;
    public JPanel yn;
	
	private class ButtonListener implements ActionListener{
		
		public void actionPerformed(ActionEvent event){
			if(event.getSource() == yes){
				try {
					yes.setEnabled(false);
					no.setEnabled(false);
					l.setText("Downloading Updates");
					l.update(l.getGraphics());
					update(getGraphics());
					Download();
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}
			else{
				try {
					Continue();
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}
		}
		
	}

    private static class ProgressListener implements ActionListener {

        public void actionPerformed(ActionEvent e){
            // e.getSource() gives you the object of DownloadCountingOutputStream
            // because you set it in the overriden method, afterWrite().
        	current = ((DownloadCountingOutputStream) e.getSource()).getByteCount();
            percentage = (int) Math.round((current/totalSize)*100);
            changeBar(percentage);
        }
    }

    
    
    public Downloader(){
    	super("Downloading Updates");
    	l = new JLabel("Would you like to download new updates?");
    	bar = new JProgressBar();
    	yes = new JButton("Yes");
    	yes.addActionListener(new ButtonListener());
    	no = new JButton("No");
    	no.addActionListener(new ButtonListener());
    	yn = new JPanel();
    	yn.add(yes); yn.add(no);
    	add(l, BorderLayout.NORTH);
    	add(yn, BorderLayout.SOUTH);
    	add(bar, BorderLayout.CENTER);
    }

	public void Continue() throws IOException {
		new program().start();
		terminate();
	}

	public void Download() throws IOException {
    	Scanner scan = new Scanner(new File("update.txt"));
        URL dl = null;
        File fl = null;
        String x = null;
        OutputStream os = null;
        InputStream is = null;
        ProgressListener progressListener = new ProgressListener();
        try {
            fl = new File("update.exe");
            dl = new URL("http://kamakwazee.net/Chalkboard/update.exe");
            scan.close();
            os = new FileOutputStream(fl);
            is = dl.openStream();

            DownloadCountingOutputStream dcount = new DownloadCountingOutputStream(os);
            dcount.setListener(progressListener);

            // this line give you the total length of source stream as a String.
            // you may want to convert to integer and store this value to
            // calculate percentage of the progression.
            totalSize = Double.parseDouble(dl.openConnection().getHeaderField("Content-Length"));

            // begin transfer by writing to dcount, not os.
            IOUtils.copy(is, dcount);

        } catch (Exception e) {
            System.out.println(e);
        } finally {
            if (os != null) { 
                os.close(); 
            }
            if (is != null) { 
                is.close(); 
            }
            finished();
        }
		
	}
	private void finished() throws MalformedURLException, IOException {
		new Update().runUpdate();
		terminate();
	}

	public static void changeBar(int p){
		bar.setValue(p);
		bar.setStringPainted(true);
		bar.update(bar.getGraphics());
	}

	public void terminate() {
		super.setVisible(false);
		super.dispose();
		
	}
}