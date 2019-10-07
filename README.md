# Service Discovery Client #
## Description ##
Updates the status of the client via OPCUA at the service discovery.

## Create .exe from project ##
* Load venv
* cd in your project directory
```
pyinstaller .\SD_Client\__main__.py --clean -p SD_Client
```
* Output directory: YOUR-PROJECT-FOLDER\dist\SD_Client
* A dependency is the VC++ Redistributable(Visual C++ Redistributable for Visual Studio 2015 ), otherwise errors will occur
    * Download here: https://www.microsoft.com/en-us/download/details.aspx?id=48145