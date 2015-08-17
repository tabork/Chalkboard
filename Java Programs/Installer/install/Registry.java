package install;

import java.time.LocalDateTime;

import com.sun.jna.platform.win32.Advapi32Util;
import com.sun.jna.platform.win32.WinReg;

public class Registry {
	
	private String getDateString(int dateValue)
	{
		
		if(dateValue < 10)
			return "0" + Integer.toString(dateValue);
		
		return Integer.toString(dateValue);
		
	}
	
	public void write(String GUID, String installPath, int estimatedSize)
	{
		
		String regPath = "Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\{" + GUID + "}";
		
		Advapi32Util.registryCreateKey(WinReg.HKEY_LOCAL_MACHINE, regPath);
		Advapi32Util.registrySetStringValue(WinReg.HKEY_LOCAL_MACHINE, regPath, "DisplayName", "Chalkboard");
		Advapi32Util.registrySetStringValue(WinReg.HKEY_LOCAL_MACHINE, regPath, "DisplayVersion", "3.0");
		Advapi32Util.registrySetStringValue(WinReg.HKEY_LOCAL_MACHINE, regPath, "Publisher", "Kamakwazee Open Source Team");
		Advapi32Util.registrySetIntValue(WinReg.HKEY_LOCAL_MACHINE, regPath, "VersionMajor", 3);
		Advapi32Util.registrySetIntValue(WinReg.HKEY_LOCAL_MACHINE, regPath, "VersionMinor", 0);
		LocalDateTime date = LocalDateTime.now();
		String dateString = Integer.toString(date.getYear()) + getDateString(date.getMonthValue()) + getDateString(date.getDayOfMonth());
		System.out.println(dateString);
		Advapi32Util.registrySetStringValue(WinReg.HKEY_LOCAL_MACHINE, regPath, "InstallDate", dateString);
		Advapi32Util.registrySetStringValue(WinReg.HKEY_LOCAL_MACHINE, regPath, "InstallLocation", installPath);
		Advapi32Util.registrySetIntValue(WinReg.HKEY_LOCAL_MACHINE, regPath, "EstimatedSize", estimatedSize);
		Advapi32Util.registrySetStringValue(WinReg.HKEY_LOCAL_MACHINE, regPath, "UninstallString", installPath + "uninstall.exe");
		
	}

}
