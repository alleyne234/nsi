### IMPORTS ###
import parcours_sequentiel as ps
import time
import tris



### CODES ###

tab = ps.create_tab(10000)

start_time = time.perf_counter()
tris.tri_insert(tab)
end_time = time.perf_counter()

print('La valeur minimale est :', ps.min_value(tab))
print("Les opérations ont duré ", end_time - start_time, "secondes.")
print('La valeur maximale est :', ps.max_value(tab))
print('La valeur moyenne est :', ps.moyenne(tab))
