# -*- coding: utf-8 -*-
#!/usr/bin/python

import time

ahora = time.strftime("%c")
## representacion de fecha y hora
print "Fecha y hora " + time.strftime("%c")

## representacion del tiempo
print "Fecha "  + time.strftime("%x")

## representacion de la hora
print "Hora " + time.strftime("%X")

## Muestra fecha y hora actual a partir de la variable 
print ("Fecha y hora de la variable %s"  % ahora )
