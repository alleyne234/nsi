#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
 module, interface, implementation
 Directed by Pascal LUCAS, modified on 10/03/2020

"""

import time_2 as time

t1 = time.create('09:19:45')

# Programme principal
if __name__=='__main__':
    import doctest
    doctest.testmod(verbose=False)
    
    # Création d'une variable de type heure
    t1 = time.create("12:00:00")
    print("t1 :",t1)
    # Comparaison de deux varialbles de type heure
    t2 = time.create("5:45:12")
    if time.comp_time(t1, t2) == 0 :
        print (t1, "=" ,t2)
    elif time.comp_time(t1, t2) == 1 :
        print (t1, ">" ,t2)
    else :
        print(t1, "<" ,t2)
