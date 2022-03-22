#Imports 
import os
from turtle import clear

#Headers
def header():
    print("Welcome on Nmython /// Made by Raspi_3.14 (Oxooi). \n")
    print("This tool is an Nmap addon. This tool was created to simplify the use of Nmap")
    print()
    print("/*" * 10)
    print()
    print(" -0: help \n -1: Ping \n -2: Fping \n -3: Download (Important) \n -4: STCP \n -5: SUDP \n -6: Full Scan \n -7: A Compact Full Scan")
    print()
    print("/*" * 6)
    print()
    print("If you don't get results at fping, please do '3' to download Nmap")
    print("If you want to know all the commands and see their uses, type: '0' to help")
    print()

#Main
def main():
    header()
    m = input("Type your choice {0/7} : ")
    if(m == '0'):
        help()
    elif(m == '1'):
        Ping()
    elif(m == '2'):
        Fping()
    elif(m == '3'):
        Download()
    elif(m == '4'):
        Stcp()
    elif(m == '5'):
        Sudp()
    elif(m == '6'):
        fullScan()
    elif(m == '7'):
        afullscan()
        
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# now, to clear the screen
cls()

#BackToMain
def backToMain():
    b = input("\nType ENTER to go back : \n")
    if b == (""):
        cls()
        main()

#Help
def help():
    print("/*/*/*/* \nModule: Help \nAction: Show all commands \n/*/*/*/*")
    print()
    print("-0 Help : Show this menu")
    print("-1 Ping : Ping a remote or local server \nto know if it is online and to have some additional information")
    print("-2 Fping : fping is a small command line tool to send ICMP (Internet Control Message Protocol) echo request to \n network hosts, similar to ping, but much higher performing when pinging multiple hosts. fping totally differs \n from ping in that you can define any number of hosts on the command line or specify a file with the list of IP \n addresses or hosts to ping")
    print("-3 Downloads: Download the necessary tools for this script (Nmap, Fping)")
    print("-4 STCP: Run a TCP Scan")
    print("-5 SUDP: Run a UDP Scan")
    print("-6 FullScan: Run a Full Scan to see every details on the server (OS, Service & Version info, Default Script")
    print("-7 AlsoFullScan: Run a simplified complete analysis")
    backToMain()

#Stcp
def Stcp():
    print("\n/*/*/*/* \nModule: Stcp \nAction: Scan TCP Ports \n/*/*/*/*\n")
    tip = input("IP : ")
    print("\nScan Launch\n")
    os.system("sudo nmap -sS -sT -Pn " + tip)
    backToMain()

#Sudp
def Sudp():
    print("\n/*/*/*/* \nModule: Sudp \nAction: Scan UDP Ports \n/*/*/*/*\n")
    uip = input("IP : ")
    print("\nScan Launch\n")
    os.system("sudo nmap -sU -Pn " + uip)
    backToMain()

#fullscan
def fullScan():
    print("\n/*/*/*/* \nModule: completScan \nAction: Run a full scan \n/*/*/*/*\n")
    fip = input("IP : ")
    print("\nScan Launch\n")
    os.system("sudo nmap -sV -sT -O -Pn " + fip)
    backToMain()

#AlsoFullScan
def afullscan():
    print("\n/*/*/*/* \nModule: completCompactScan \nAction: Run a compact full scan \n/*/*/*/*\n")
    fip2 = input("Ip : ")
    print("\nScan Launch\n")
    os.system("sudo nmap -A -Pn " + fip2)
    backToMain()

#Ping 
def Ping():
    print("\n/*/*/*/* \nModule: Ping \nAction: Check if server is online \n/*/*/*/*\n")
    pingip = input("IP (On Linux use CTRL+C to stop ping): ")
    print("\nPing Launch\n")
    os.system("ping " + pingip)
    backToMain()

#Fping
def Fping():
    print("\n/*/*/*/* \nModule: Fping \nAction: Launch a Fping (similar to ping, but much higher performing when pinging multiple hosts.) \n/*/*/*/*\n")
    fpip = input("IP : ")
    print("\nFPing Launch\n")
    os.system("fping " + fpip)
    backToMain()

#Download
def Download():
    print("\n/*/*/*/* \nModule: Download \nAction: Download dependencies \n/*/*/*/*\n")
    d = input("Do you want download all dependencies ? (y/n) : ")
    if(d == 'y'):
        os.system("sudo apt-get install nmap && sudo apt-get install fping")
        print("\nDownload end")
        backToMain()
    else :
        backToMain()

#Ignite Main
main()