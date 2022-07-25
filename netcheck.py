import os
import numpy
import pandas
import subprocess
def main():
    is_up=True
    ip_addresses=pandas.read_csv("ip addresses.csv")
    for i,row in ip_addresses.iterrows():
        with open(os.devnull, 'w') as DEVNULL:
            try:
                subprocess.check_call(
            ['ping', '-n', '3', row['ip_addr']],
            stdout=DEVNULL,  # suppress output
            stderr=DEVNULL
            )
                is_up = True
            except subprocess.CalledProcessError:
                is_up = False
        if is_up:
            print(row['ip_addr']+" is up")
        else:
            print(row['ip_addr']+" is down")    
if __name__ == '__main__':
    main()