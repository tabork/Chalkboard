package install;

import com.sun.jna.platform.win32.Advapi32Util;
import com.sun.jna.platform.win32.WinReg;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import java.io.File;
import java.time.LocalDateTime;
import java.util.Formatter;

public class Registry {

	private int vmaj, vmin;
	private String version;
	
	private String getDateString(int dateValue)
	{
		
		if(dateValue < 10)
			return "0" + Integer.toString(dateValue);
		
		return Integer.toString(dateValue);
		
	}

	private void readXML()
	{

		try
		{

			File fXmlFile = new File("info.xml");
			DocumentBuilderFactory dbFactory = DocumentBuilderFactory.newInstance();
			DocumentBuilder dBuilder = dbFactory.newDocumentBuilder();
			Document doc = dBuilder.parse(fXmlFile);

			doc.getDocumentElement().normalize();

			NodeList nList = doc.getElementsByTagName("chalkboard");

			Node nNode = nList.item(0);

			if(nNode.getNodeType() == Node.ELEMENT_NODE)
			{

				Element eElement = (Element) nNode;
				vmaj = Integer.parseInt(eElement.getElementsByTagName("major").item(0).getTextContent());
				vmin = Integer.parseInt(eElement.getElementsByTagName("minor").item(0).getTextContent());
				version = eElement.getElementsByTagName("version").item(0).getTextContent();

			}

		} catch(Exception e)
		{
			e.printStackTrace();
		}

	}
	
	public void write(String GUID, String installPath, int estimatedSize)
	{

		readXML();

		String regPath = "Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\{" + GUID + "}";
		
		Advapi32Util.registryCreateKey(WinReg.HKEY_LOCAL_MACHINE, regPath);
		Advapi32Util.registrySetStringValue(WinReg.HKEY_LOCAL_MACHINE, regPath, "DisplayName", "Chalkboard");
		Advapi32Util.registrySetStringValue(WinReg.HKEY_LOCAL_MACHINE, regPath, "DisplayVersion", version);
		Advapi32Util.registrySetStringValue(WinReg.HKEY_LOCAL_MACHINE, regPath, "Publisher", "Kamakwazee Open Source Team");
		Advapi32Util.registrySetIntValue(WinReg.HKEY_LOCAL_MACHINE, regPath, "VersionMajor", vmaj);
		Advapi32Util.registrySetIntValue(WinReg.HKEY_LOCAL_MACHINE, regPath, "VersionMinor", vmin);
		LocalDateTime date = LocalDateTime.now();
		String dateString = Integer.toString(date.getYear()) + getDateString(date.getMonthValue()) + getDateString(date.getDayOfMonth());
		System.out.println(dateString);
		Advapi32Util.registrySetStringValue(WinReg.HKEY_LOCAL_MACHINE, regPath, "InstallDate", dateString);
		Advapi32Util.registrySetStringValue(WinReg.HKEY_LOCAL_MACHINE, regPath, "InstallLocation", installPath);
		Advapi32Util.registrySetIntValue(WinReg.HKEY_LOCAL_MACHINE, regPath, "EstimatedSize", estimatedSize);
		String ad = System.getenv("AppData") + "\\Chalkboard";
		File bat = new File(ad + "\\uninstall.bat");
		try  {
			new File(ad).mkdirs();
			Formatter f = new Formatter(bat);
			String com = "reg delete hklm\\Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\{454f42d9-6f6e-48be-804d-e275fb4a97ed} /f%nrmdir /s /q \"C:\\Program Files (x86)\\Chalkboard\"%ndel %%0%n";
			f.format(com);
			f.close();
		}
		catch(Exception e)
		{
			e.printStackTrace();
		}
		Advapi32Util.registrySetStringValue(WinReg.HKEY_LOCAL_MACHINE, regPath, "UninstallString", ad + "\\uninstall.bat");
		
	}

}
