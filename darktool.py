#librys   المكتبات
import os
import sys
import time
import datetime
import random
import compileall
#+++++++++++++++++++++++++++++++++
c = ['\033[1;30m','\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m','\033[1;37m']
#_________________________________________
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(00000.02)
os.system('clear' )
os.system('clear') 
print(random.choice(c))
jalan("loading.....! "*3)
#jalan("loading.....! "*3)
#jalan("loading.....! "*3)
#jalan("loading.....! "*3)
#jalan("loading.....! "*3)
#jalan("loading.....! "*3)
#jalan("loading.....! "*3)
#time.sleep(2)
os.system('clear')
print('\033[1;32m#########################################')
print('\033[1;31m 1 - youtube channel :  \033[1;35mhttps://www.youtube.com/channel/UC8AZLQfg12ZTCkUDnvCRsjA')
print("\033[1;31m 2 - whatsapp groub link :  \033[1;35mhttps://chat.whatsapp.com/ERd6SWDqzHMFYq5AUT2zR8")
print('\033[1;32m#########################################')
#________________________________________
def main():
    print("\033[1;31m[1] \033[1;34mInstall pkg Termux\033[1;31m(termux)")
    time.sleep(0.3)
#________________
    print("\033[1;31m[2] \033[1;34mInstall metasploit\033[1;31m(termux)")
    time.sleep(0.3)
#__________________
    print("\033[1;31m[3] \033[1;34mInstall ngrok\033[1;31m(termux,kali)")
    time.sleep(0.3)
#___________________
    print("\033[1;31m[4] \033[1;34mEncrypt tools\033[1;31m(termux)")
    time.sleep(0.3)
#____________________
    print('\033[1;31m[5] \033[1;34mscript metesploit\033[1;31m(termux,kali)')
    time.sleep(0.3)
#____________________
    print("\033[1;31m[6] \033[1;34mEvil-Droid\033[1;31m(kali)")
    time.sleep(0.3)
#______________________
    print("\033[1;31m[7] \033[1;34mnexphisher\033[1;31m(termux,kali)")
    time.sleep(0.3)
#______________________
    
    #print("\033[1;31m[8] \033[1;34mfacebook hacking\033[1;31m(termux)")
    #print(logo)
main()
choose = input("\033[1;37mChoose an option : ")
time.sleep(0.3)
##############################################################
if choose == '1':
    jalan("Just wait for the download to finish")
    os.system('pip install --upgrade pip ')
    os.system('pkg update && upgrade -y ;pip install --upgrade pip ; pkg install git -y ; pkg install nano -y ; pkg install python -y ; pkg install python2 -y ; pkg install php -y;pkg install unzip -y ; pkg install openssh -y ; pkg install cat -y ; pkg install curl -y ; pkg install wget -y ; pkg install w3m -y ;pkg install golang -y ; pkg install havij -y ; pkg install db -y ; pkg install postgresql -y ; pkg install uftrace -y ; pkg install ruby -y ; pkg install perl -y; pkg install bash -y ;pkg install figlet -y;pkg install cowsay -y; pkg install tar -y;pkg install zip -y; pkg install tor -y; pkg install toilet -y;pkg install proot -y; pkg install golang -y; pkg install openssl -y;pkg install cmatrix -y ; pkg install macchanger ;pkg install root-repo -y;pkg install unstable-repo -y;pkg install x11-repo -y ; pip install --upgrade pip ')
    os.system('clear')
    print("\033[1;31mThe installation was successful")
    time.sleep(3)
##############################################################
elif choose == '2':
    y  = input('metesploit {1} metesploit {2} <<<<<<<<<<<_<<<<<<<: ')
    if y =='1':     
        jalan("please wait ..")
        try:
            os.system('pkg install root-repo ; pkg install unstable-repo ; pkg install x11-repo ; pkg update && pkg upgrade && pkg install git curl wget nmap -y && curl -LO raw.githubusercontent.com/Hax4us/Metasploit_termux/master/metasploit.sh && chmod 777 metasploit.sh && ./metasploit.sh ; bash metasploit.sh ')
            print("The installation was successful")
        except:
            print("Installation failed")
            time.sleep(3)
            os.system('exit') 
    elif y =='2':
        try:
            os.system('clear')
            os.system('pkg update && pkg upgrade -y && pkg install wget curl openssh git –y')
            os.system("clear")
            os.system('Cd $HOME')
            os.system('Wget Auxilus.github.io/metasploit.sh')
            os.system('Bash metasploit.sh')
            print('to Run the tool please write : msfconsole')
        except:
            print('the instaltion is faild')
##############################################################
elif choose == '3':
    q=input("install termux[1] linux[2] : ")
    if q =='1':
        os.system('cd $HOME')
        os.system("clear")
        os.system('pkg install tar ')
        os.system('wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.tgz')
        os.system('cd /sdcard/Download')
        os.system('tar zxvf ngrok-stable-linux-arm.tgz')
        os.system('mv ngrok $HOME')
        os.system('cd')
        os.system('chmod +x ngrok')
        jalan ('\033[1;31mThe tool was loaded successfully')
        os.system('clear')
        print("Done")
        time.sleep(3)
        #print(logo)
        main()
        time.sleep(0.3)
    elif q == '2':
        os.system("cd /root/Desktop")
        os.system('wget  https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip  ')
        os.system('unzip ngrok-stable-linux-amd64.zip ')
        os.system('xdg-open https://dashboard.ngrok.com/signup ')
        os.system('chmod +x ngrok')
        os.system("rm -rf ngrok-stable-linux-amd64.zip")
        os.system("mv ngrok /root/Desktop")
        print('\033[1;31m please copy the {2}  to Connect your account:  and copy paste here ')
        jalan ('\033[1;31mThe tool was loaded successfully')
##############################################################
elif choose == '4':
    tool_list = str(input(" \033[1;36mType the path for the tool: "))
    compileall.compile_file(tool_list)
    e=input("linux[1] TERMUX [2] : ")
    if e =='1':
        jalan('\033[1;31mEncryption successful')
        jalan("\033[1;36mSave to /Desktop/)_____Dark_____") 
        time.sleep(3)
        os.system('exit')
    elif e=="2":
        jalan('\033[1;31mEncryption successful')
        jalan("\033[1;36mSave to /sdcard/)_____Dark_____")
################################################################
elif choose =='5':
    os.system('clear')
    e=input("linux[1] TERMUX [2] : ")
    if e =='1':
        os.system('xdg-open https://drive.google.com/file/d/1Qr9ieS5h6PPaDjwm6AT1suQc8iwkMdnc/view')
        jalan ('\033[1;31mThe tool was loaded successfully')
    elif e =='2':
        jalan ('\033[1;31mThe tool was loaded successfully')
        os.system('xdg-open https://drive.google.com/file/d/1Qr9ieS5h6PPaDjwm6AT1suQc8iwkMdnc/view')
#################################################################################################
elif choose =='6':
    os.system('git clone https://github.com/M4sc3r4n0/Evil-Droid.git')
    print('#################################')
    print('please copy and paste here 😗️>>>>>>>>>>>>>>>>..🥰️:')
    print("##################################")
    print('====================================')
    print('cd Evil-Droid')
    print('chmod +x *')
    print('./evil-droid')
    print('=====================================')
######################################################
elif choose =='7':
    os.system('clear')
    os.system('cd $HOME ' )
    os.system('git clone https://github.com/htr-tech/nexphisher.git')
    os.system('clear')
    print('please copy and paste here 😗>>>>>>>>>>>>>>>>..🥰:')
    print("##################################")
    print('====================================')
    print('cd nexphisher ')
    print('chmod +x *')
    print('bash setup(kali)')
    print('bash tmux_setup(termux)')
    print('=====================================')
#############################################################
#######################################
                
###############################################

