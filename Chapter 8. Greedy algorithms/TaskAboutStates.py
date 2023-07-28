states_needed = {"id", "nv", "ut", "wa", "mt", "or", "ca", "az"}
radiostations = {
    "kone": {'id', 'nv', 'ut'},
    'ktwo': {'id', 'wa', 'mt'},
    'kthree': {'or', 'nv', 'ca'},
    'kfour': {'ut', 'nv'},
    'kfive': {'az', 'ca'}
}
final_stations = set()
# стратегия - на каждом шаге брать ту радиостанцию, которая захватывает наибольшее количество еще не захваченных штатов
while states_needed:
    best_station = None
    max_states_intersection = 0
    for radiostation, avaliable_states in radiostations.items():
        intersection_states = states_needed & avaliable_states
        len_intersection_states = len(intersection_states)
        if len_intersection_states > max_states_intersection:
            max_states_intersection = len_intersection_states
            best_station = radiostation
    final_stations.add(best_station)
    states_needed -= radiostations[best_station]

print(final_stations)
