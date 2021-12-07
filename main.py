import argparse
import os 

def clear(): 
    return os.system('cls' if os.name == 'nt' else 'clear')
print("")

title = '''
            |                                                                         
\ \  \   /  __ \    _ \   __|   _ \        _` |   __|   _ \       |   |   _ \   |   | 
 \ \  \ /   | | |   __/  |      __/       (   |  |      __/       |   |  (   |  |   | 
  \_/\_/   _| |_| \___| _|    \___|      \__._| _|    \___|      \__. | \___/  \__._| 
                                                                 ____/                



  V0.1

'''
print(title)
print("")
parser = argparse.ArgumentParser("katana-ds.py",formatter_class=argparse.RawTextHelpFormatter)


parser.add_argument("-x","--xary", help="Analysis Xray log", action='store_true' )
args = parser.parse_args()

if args.xary :
 clear() 
 from Analysis import xraylog
 

