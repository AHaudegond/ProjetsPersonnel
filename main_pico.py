#a renommer en main.py pour run on boot sur raspberry pi pico
#programme utiliser pour ma carte raspberry pi pico pour mon projet de stand de tir personnel avec ventilateur pour perturber la trajectoire des ballons

import machine
import utime
import math
ventilo_1= machine.Pin(2, machine.Pin.OUT)
ventilo_2= machine.Pin(14, machine.Pin.OUT)
ventilo_3= machine.Pin(16, machine.Pin.OUT)
while True:
    utime.sleep(2)
    x=randint(0,7)# 0= aucun ventilo, 1= v1 2= v2,3= v3, 4=v1+v2,5=v1+v3,6v=v2+v3,7=tous, potentiellement 4éme ventilo sur pin run pour maintenir ballon en l'air (et pas juste les perturber)
    if x==0: #on fait très peu de calculs par raport à la puissance de la carte et le temps n'est pas important ici, pas besoin d'optimiser
        ventilo_1.value(0)
        ventilo_2.value(0)
        ventilo_3.value(0)
    elif x==1:
        ventilo_1.value(1)
        ventilo_2.value(0)
        ventilo_3.value(0)
    elif x==2:
        ventilo_1.value(0)
        ventilo_2.value(2)
        ventilo_3.value(0)
    elif x==3:
        ventilo_1.value(0)
        ventilo_2.value(0)
        ventilo_3.value(3)
    elif x==4:
        ventilo_1.value(1)
        ventilo_2.value(1)
        ventilo_3.value(0)
    elif x==5:
        ventilo_1.value(1)
        ventilo_2.value(0)
        ventilo_3.value(1)
    elif x==6:
        ventilo_1.value(0)
        ventilo_2.value(1)
        ventilo_3.value(1)
    elif x==7:
        ventilo_1.value(1)
        ventilo_2.value(1)
        ventilo_3.value(1)
    
