#include <iostream>
#include<stdlib.h>
#include<fstream>
#include<string>
#include<conio.h>

using namespace std;

int main()
{
	ofstream xmlFile;
	ifstream xmlFile1;

	string name = "", pass = "";
	string ntyp = "Wi-Fi", netType, fileTest = ">test.txt", check, ntype, fil, xfileName, fileName = "myWlan.xml";
	char c = '"', cho = '2', cho1 = '1', c1;
	netType = c + ntyp + c + fileTest;
	xfileName = c + fileName + c;
	int succ = 0;

	do
	{
		system("netsh wlan show networks");
		cout << "   >--------------------         TO REFRESS PRESS :1       \n\n   >--------------------         TO CHOOSE NETWORK PRESS : 2              \n\n   >   ";
		cho = getchar();
	} while (cho != '2');

	cout << "\n    Enter the desired network name-------:       ";
	cin >> name;
	do
	{
		cout << "\n    Enter wifi Password------:        ";
		cin >> pass;
		xmlFile.open(fileName.c_str());

		//Writing a xml file .....................

		xmlFile << "<?xml version=" << c << "1.0" << c << "?>\n";
		xmlFile << "<WLANProfile xmlns=" << c << "http://www.microsoft.com/networking/WLAN/profile/v1" << c << ">\n";
		xmlFile << "<name>";
		xmlFile << name;
		xmlFile << "</name>\n<SSIDConfig>\n<SSID>\n<hex>";
		for (int i = 0; i < name.length(); i++)
			xmlFile << hex << (int)name.at(i);
		xmlFile << "</hex>\n<name>";
		xmlFile << name;
		xmlFile << "</name>\n</SSID>\n</SSIDConfig>\n<connectionType>ESS</connectionType>\n<connectionMode>auto</connectionMode>\n<MSM>\n<security>\n<authEncryption>";
		xmlFile << "\n<authentication>WPA2PSK</authentication>\n<encryption>AES</encryption>\n<useOneX>false</useOneX>\n</authEncryption>\n<sharedKey>";
		xmlFile << "\n<keyType>passPhrase</keyType>\n<protected>false</protected>\n<keyMaterial>";
		xmlFile << pass;
		xmlFile << "</keyMaterial>\n</sharedKey>\n</security>\n</MSM>\n";
		xmlFile << "<MacRandomization xmlns=" << c << "http://www.microsoft.com/networking/WLAN/profile/v3" << c << ">\n";
		xmlFile << "<enableRandomization>false</enableRandomization>\n</MacRandomization>\n</WLANProfile>";
		xmlFile.close();

		//addd the xml file to system profile.............
		system(("netsh wlan add profile filename=" + xfileName).c_str());
		//to let system realize what changes have been made...............
		system("timeout /t 2");
		//to check if connected...........
		system(("netsh interface show interface name=" + netType).c_str());

		xmlFile1.open("test.txt");
		while (!xmlFile1.eof())
		{
			xmlFile1 >> c1;
			if (c1 == ':')
			{
				for (int i = 0; i < 9; i++)
				{
					xmlFile1 >> c1;
					check = check + c1;
				}
			}
			if (check == "Connected")
			{
				cout << "...............................................You are connected!!.................................";
				succ = 1; break;
			}
			if (check != "Connected")check = "";



		}
		xmlFile1.close();
		if (succ == 1)break;
	} while (succ != 1);
	return 0;
}
