import os
import subprocess
from urllib.request import urlretrieve
import ssl
import logging
import warnings

warnings.filterwarnings("ignore")

#create logs
logging.basicConfig(filename=os.getcwd()+"/vnmlogs.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


class PythonInstaller:
    def pythonRename(src, dst):
        os.rename(src, dst)

    def pythonDownload():
        logger.info('Python download attempt')
        url = "https://www.python.org/ftp/python/3.9.12/python-3.9.12-amd64.exe"
        py_filename = os.getcwd() + '/python3.9.exe'
        try:
            _create_unverified_https_context = ssl._create_unverified_context
        except AttributeError:
            pass
        else:
            ssl._create_default_https_context = _create_unverified_https_context

        urlretrieve(url, py_filename)
        print("Python3.9 Successfully Downloaded.")

    def pythonInstall():
        logger.info('Running python installer')
        cmd = 'python3.9.exe /quiet InstallAllUsers=1 PrependPath=1 Include_doc=0 AssociateFiles=1 Shortcuts=0'
        try:
            p = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            # output, error = p.communicate()
            # p = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            logger.info(p.stdout)
            logger.error(p.stderr)
            if p.stderr == '':#TO-DO
                print('Python Successfully Installed')
            else:
                logger.error(p.stderr)
                print("Python not installed completely. Please install it manually")
        except Exception as e:
            logger.error(e)
            print("Fortified due to the below Exception:")
            print(e)
            print("Python not installed.")

class VSCodeInstaller:
    def vscodeRename(src, dst):
        os.rename(src, dst)

    def vscodeDownload():
        logger.info('VSCode download attempt')
        url = "https://update.code.visualstudio.com/1.66.2/win32-x64/stable"
        vs_filename = os.getcwd() + '/VSCode.exe'
        urlretrieve(url, vs_filename)
        print("VSCode v1.66 Successfully Downloaded.")

    def vscodeInstall():
        logger.info('Running vscode installer')
        cmd = 'VSCode.exe /VERYSILENT /NORESTART /MERGETASKS=!runcode,addtopath,desktopicon,associatewithfiles /DIR="C:\Program Files\Microsoft VS Code"'
        try:
            p = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            logger.info(p.stdout)
            if p.stderr == '':#TO-DO
                print('VSCode Successfully Installed')
            else:
                logger.error(p.stderr)
                print("VSCode not installed completely. Please install it manually")
        except Exception as e:
            logger.error(e)
            print("Fortified due to the below Exception:")
            print(e)
            print("VSCode not installed.")
        
class MiniCondaInstaller:
    def minicondaRename(src, dst):
        os.rename(src, dst)

    def minicondaInstall():
        logger.info('Running Miniconda installer')
        cmd = str('start /wait "" Miniconda3.exe /InstallationType=JustMe /RegisterPython=0 /AddToPath=1 /S /D=C:\ProgramData\Miniconda3')
        try:
            p = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            logger.info(p.stdout)
            if p.stderr == '': #TO-DO
                print('Miniconda3 Successfully Installed')
            else:
                logger.error(p.stderr)
                print("Miniconda3 not installed completely. Please install it manually")
        except Exception as e:
            logger.error(e)
            print("Fortified due to the below Exception:")
            print(e)
            print("Miniconda3 not installed.")

    def minicondaDownload():
        logger.info('Miniconda3 download attempt')
        url = "https://repo.anaconda.com/miniconda/Miniconda3-py39_4.11.0-Windows-x86_64.exe"
        mini_filename = os.getcwd() + '/Miniconda3.exe'
        urlretrieve(url, mini_filename)
        print("Miniconda3 Successfully Downloaded.")

def process_vscode(v):
    vs_filename = os.getcwd() + '/VSCode.exe'
    vs_alt_filename = os.getcwd() + '/VSCodeSetup-x64-1.66.2.exe'
    #VSCode Procedure
    print("Checking for VSCode-1.66 Installer.")
    if any((os.path.exists(vs_filename), os.path.exists(vs_alt_filename))):
        print("Installer exists. Attempting to install VSCode-v1.66")
        print("It may take a while, Please wait :-)")
        if os.path.exists(vs_alt_filename):
            logger.info("Renaming Miniconda setup files from complex to simple")
            v.vscodeRename(vs_alt_filename, vs_filename)
        v.vscodeInstall()       
    else:
        print("Installer Not Found.")
        print("Downloading VSCode...It may take a while, Please wait :-)")
        v.vscodeDownload()
        print("Download Completed.")
        print("Installing VSCode...It may take a while, Please wait a bit more :-)")
        v.vscodeInstall()  

def process_miniconda(m):
    mini_filename = os.getcwd() + '/Miniconda3.exe'
    mini_alt_filename = os.getcwd() + '/Miniconda3-py39_4.11.0-Windows-x86_64.exe'
    # Miniconda3 Procedure
    print("Checking for Miniconda3-v4.11.0 Installer.")
    if any((os.path.exists(mini_filename), os.path.exists(mini_alt_filename))):
        print("Installer exists. Attempting to install Miniconda3-v4.11.0")
        print("It may take a while, Please wait :-)")
        if os.path.exists(mini_alt_filename):
            logger.info("Renaming Miniconda setup files from complex to simple")
            m.minicondaRename(mini_alt_filename, mini_filename)
        m.minicondaInstall()       
    else:
        print("Installer Not Found.")
        print("Downloading Miniconda3...It may take a while, Please wait :-)")
        m.minicondaDownload()
        print("Download Completed.")
        print("Installing Miniconda3...It may take a while, Please wait a bit more :-)")
        m.minicondaInstall()

def process_python(p):
    py_filename = os.getcwd() + '/python3.9.exe'
    py_alt_filename = os.getcwd() + '/python-3.9.11.exe.exe'
    # Python ins Procedure
    print("Checking for Miniconda3-v4.11.0 Installer.")
    if any((os.path.exists(py_filename), os.path.exists(py_alt_filename))):
        print("Installer exists. Attempting to install Python3.9")
        print("It may take a while, Please wait :-)")
        if os.path.exists(py_alt_filename):
            logger.info("Renaming python setup files from complex to simple")
            p.pythonRename(py_alt_filename, py_filename)
        p.pythonInstall()       
    else:
        print("Installer Not Found.")
        print("Downloading python...It may take a while, Please wait :-)")
        p.pythonDownload()
        print("Download Completed.")
        print("Installing python...It may take a while, Please wait a bit more :-)")
        p.pythonInstall()


if __name__ == '__main__':
    logger.info('STEP-1 initiated')
    #STEP 1
    #Downloading and Installing VSCode-v1.66 and Miniconda3-v4.11.0-py3.9 
    v = VSCodeInstaller
    m = MiniCondaInstaller
    p = PythonInstaller
    try:
        process_python(p)
    except Exception as e:
        print(e)
        print('Python could not be completed. Skipping...')

    try:
        process_miniconda(m)
    except Exception as e:
        print(e)

        print('Miniconda3 could not be completed. Skipping...')
    
    try:
        process_vscode(v)    
    except Exception as e:
        print(e)

        print('VSCode Installation could not be completed. Skipping...')
    input("Press ENTER to exit...")