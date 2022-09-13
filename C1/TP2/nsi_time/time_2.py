#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''

:mod:`Time_2` time management module

 Directed by Pascal LUCAS, modified on 09/03/2020


'''

#
import builtins


def create(hour):
    '''
    Return a couple of three integers corresponding to the hours, minutes and seconds
    :param (str) time provided as a string hh: mm: ss
    :return (tuple) (hh, mm, ss)
    :CU
    '''

    try:
        hms=hour.split(':')
    except:
        return(0, 0, 0)
    if len(hms)==3:
        try:
            h=int(hms[0])
            m=int(hms[1])
            s=int(hms[2])
        except:
            return(0, 0, 0)
        if int(h)<0 or h>23 or m<0 or m>59 or s<0 or s>59:
            return(0, 0, 0)
        return (h, m, s)
            
    else:
        return(0, 0, 0)

def get_h(t):
    return t[0]

def get_m(t):
    return t[1]

def get_s(t):
    return[2]

def comp_time(t1, t2):
    '''
    Compare two time objects. Returns -1 if t1 < t2, 0 if t1 = t2 and 1 if t1 > t2
    :param t1, t2: hour number
    :return: (int)
    '''
    if get_h(t1) > get_h(t2):
        return 1
    elif get_h(t1) < get_h(t2):
        return -1
    else:
        if get_m(t1) > get_m(t2):
            return 1
        elif get_m(t1) < get_m(t2):
            return -1
        else:
            if get_s(t1) > get_s(t2):
                return 1
            elif get_s(t1) < get_s(t2):
                return -1
            else:
                return 0

def sub_time(t1, t2):
    '''
    Subtract t1 from t2, returns the number of seconds between t1 and t2
    :param t1, t2: hour number
    :return: (dict of int) if t2>t1 returns {'h': 0, 'm': 0, 's': 0}
    '''
    
    h1 = get_h(t1)
    m1 = get_m(t1)
    s1 = get_s(t1)
    h2 = get_h(t2)
    m2 = get_m(t2)
    s2 = get_s(t2)
    diff = (h1 - h2) * 3600 + \
           (m1 - m2) * 60 + \
           (s1 - s2)
    if diff >= 0:
        return seconds_hour(diff)
    else:
        return create('00:00:00')

def seconds_hour(nb_s):
    '''
    Convert a number of seconds to a time object
    If the time object isn't between 00:00:00 to 23:59:29, the function return a object time equal to 00:00:00
    :param (int) number of seconds
    :return hour
    '''
    
    if nb_s >= 0 and nb_s < 86400:
        h=nb_s // 3600
        m=(nb_s - h * 3600) // 60
        s=nb_s - h * 3600 - m * 60
        return create(str(h)+':'+str(m)+':'+str(s))
    return create('00:00:00')

def __format_time(time):
    '''
    Return the representation a dictionary time in the form of a character string 'hh: mm: ss'
    :param (dict): time (hh, mm, ss) tuple of int
    :return: (str) Character string formatted on 2 digits per element
    :CU : the tuple is made up of integers from 0 to 99
    '''
    h=get_h(time)
    m=get_m(time)
    s=get_s(time)
    return "%02d"%h+":%02d"%m+":%02d"%s

def conv_s_time(nb_s):
    '''
    Convert a number of seconds to a time object
    If the time object isn't between 00:00:00 to 23:59:29, the function return (0, 0, 0)
    :param (int) number of seconds
    :return (tuple of int) a time objetc (h, m, s)
    '''
    if nb_s>=0 and nb_s<86400:
        h=nb_s//3600
        m=(nb_s-h*3600)//60
        s=nb_s-h*3600-m*60
        return(h, m, s)
    return (0, 0, 0)


def print(t, end='\n'):
    '''
    Print the hour object t with string form `hh:mm:ss`
    :param t: time number to print
    :param end: [optional] separator (default is '\\\\n')
    :type end: string
    :return: None
    :UC: none  
    '''
#    builtins.print(__format_time(t), end=end)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    time1=create('12:00:00')
    print(time1)

    pass

