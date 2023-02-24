t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]

def mini(tab_releve, tab_date):
    '''Renvoie la plus petite valeur rele
    '''
    t_mini = tab_releve[0]
    i_mini = 0
    for i in range(len(tab_releve)):
        if tab_reveve[i] < t_mini:
            t_mini = tab_releve
