import subprocess
import optparse

# 'optparse' module allows us to get arguments from the user and parse them and use them in the code.
# raw_input() -> python 2.7 & input() -> python3
# interface = raw_input("Enter a interface example -> eth0,wlan0 :-")

'''
    OptionParser is a class which holds all the user input arguments by
    creating a object 'parser' i.e we cant use the class without making an instance or 
    object of the class here it is 'parser'.   
'''

# from optparse import OptionParser
parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="interface modules like eth0, wlan0, etc.")
parser.add_option("-m", "--mac", dest="new_mac", help="example -> 00:xx:xx:xx:xx:xx")

'''
    when we call .parse_args(), it will go through everything the user inputs and
    separate it into two sets of information the first is arguments which is --interface and --mac and the
    second one is the values i.e eth0 or wlan and the mac address
'''
'''   
    .parse_args() method will return two sets of information arguments and options, and to capture that we 
    are using two variables, we are calling them (options and arguments) which is equal to whatever it will return
    through parser.parse_args()
'''
(options, arguments) = parser.parse_args()

# variables 1. interface 2. new_mac
# interface = input("Enter a interface example -> eth0,wlan0 :-")
# new_mac = input("Enter new Mac example -> 00:xx:xx:xx:xx:xx :-")

# to use the user input options we need to use options.interface and options.new_mac
interface = options.interface
new_mac = options.new_mac

print("[+] Changing MAC address for " + interface + " to " + new_mac)

''' 
    with this this script can be manipulated 
    by wlan0;ls;(in linux we can run multiple commands using ;) -> we are injecting two another extra command which 
    is not secure for out script
'''
# subprocess.call("ifconfig " + interface + " down", shell=True)
# subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
# subprocess.call("ifconfig " + interface + " up", shell=True)

'''
    This is an another process to run subprocess in a secure way
    using a list here we close quotations in place of space in the command and 
    as interface is a variable we doesn't need to put that in quotations
'''

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])
