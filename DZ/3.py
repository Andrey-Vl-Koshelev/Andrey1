import csv

with open('data2.csv', 'r') as f:
    print(f.read())

# stdout:
# hostname;vendor;model;location
# sw1;Cisco;3750;London
# sw2;Cisco;3850;Liverpool
# sw3;Cisco;3650;Liverpool
# sw4;Cisco;3650;London