package update;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.URL;
import java.util.Scanner;

import org.apache.commons.io.*;

public class Downloader {
	
	public static String progress;
	public static double totalSize;
	public static boolean start = true;
	public static long current;
	public static int percentage;
	public static String percent;

    private static class ProgressListener implements ActionListener {

        public void clear(){
        	for(int i = 0;i<25;i++){
        		System.out.print("\n");
        	}
        }
        @Override
        public void actionPerformed(ActionEvent e){
        	if(start != true){
        		clear();
        	}
        	else{
        		start = false;
        	}
            // e.getSource() gives you the object of DownloadCountingOutputStream
            // because you set it in the overriden method, afterWrite().
        	current = ((DownloadCountingOutputStream) e.getSource()).getByteCount();
            percentage = (int) Math.round((current/totalSize)*100);
            percent = "] " + Integer.toString(percentage) + "%";
            if(percentage >= 0 && percentage <= 10){
            	progress = "[                    ";
            }
            else if(percentage >= 10 && percentage <= 20){
            	progress = "[--                  ";
            }
            else if(percentage >= 20 && percentage <= 30){
            	progress = "[----                ";
            }
            else if(percentage >= 30 && percentage <= 40){
            	progress = "[------              ";
            }
            else if(percentage >= 40 && percentage <= 50){
            	progress = "[--------            ";
            }
            else if(percentage >= 50 && percentage <= 60){
            	progress = "[----------          ";
            }
            else if(percentage >= 60 && percentage <= 70){
            	progress = "[------------        ";
            }
            else if(percentage >= 70 && percentage <= 80){
            	progress = "[--------------      ";
            }
            else if(percentage >= 80 && percentage <= 90){
            	progress = "[----------------    ";
            }
            else if(percentage >= 90 && percentage < 100){
            	progress = "[------------------  ";
            }
            else{
            	progress = "[--------------------";
            }
            System.out.println(progress + percent);
        }
    }

    public Downloader() throws IOException {
    	progress = "[                    ";
    	File update;
    	if(new File("C:\\Program Files (x86)").isDirectory()){
    		update = new File("C:\\Program Files (x86)\\Chalkboard\\update.txt");
    	}
    	else{
    		update = new File("C:\\Program Files\\Chalkboard\\update.txt");
    	}
    	Scanner scan = new Scanner(update);
        URL dl = null;
        File fl = null;
        String x = null;
        OutputStream os = null;
        InputStream is = null;
        ProgressListener progressListener = new ProgressListener();
        try {
        	if(new File("C:\\Program Files (x86)").isDirectory()){
        		fl = new File("C:\\Program Files (x86)\\Chalkboard\\updater.exe");
        	}
        	else{
        		fl = new File("C:\\Program Files\\Chalkboard\\updater.exe");
        	}
            dl = new URL("http://kamakwazee.net/Downloads/Chalkboard/Chalkboard-" + scan.nextLine() + "-win32-setup");
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
        }
    }
}