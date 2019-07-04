from heuristics_and_algorithms.costs import count_total_cost, reset_all_nodes
from heuristics_and_algorithms.path_finding import dijkstra, get_nodes
# Po wygenerowaniu pierwszej trasy dijkstra:
#   (trasa dijkstry [start, ..., ..., finish] )
#   Przejdz do nastepnego wezla A po starcie
#   Ustal wezel A jako start
#       Wygeneruj dla wezla startu dostepne polaczonia
#       Jesli nastepny wezel B w dijkstrze jest polaczony ze startem ustal B start i powtorz inaczej przerwij


def keep_going(start, finish):
    final_route = []
    dijkstra_route = []
    new_start = None
    while finish not in final_route:
        start_index = 1
        if new_start is None:
            new_start = start
            new_start.set_start()
            final_route.append(start)
        elif len(dijkstra_route) < 2:
            print("Last connection lost")
        else:
            new_start = dijkstra_route[start_index]
            new_start.set_start()
            final_route.append(new_start)
        edges = new_start.get_edges()
        viable_nodes = new_start.get_nodes()
        reset_all_nodes(viable_nodes)
        new_start.set_start()

        while start_index + 1 < len(dijkstra_route) and dijkstra_route[start_index+1] in viable_nodes:
            start_index += 1
            new_start = dijkstra_route[start_index]
            new_start.set_start()
            edges = new_start.get_edges()
            reset_all_nodes(viable_nodes)
            viable_nodes = new_start.get_nodes()
            final_route.append(new_start)

        tag = False
        while finish not in viable_nodes:
            if tag:
                return -1, "No connection"
            new_start.set_start()
            edges = new_start.get_edges()
            viable_nodes = get_nodes(new_start, edges)
            tag = True
        reset_all_nodes(viable_nodes)
        new_start.set_start()
        dijkstra_route = dijkstra(finish, edges, viable_nodes)
        dijkstra_route.append(new_start)
        dijkstra_route.reverse()

    total_cost = count_total_cost(final_route)

    return total_cost, final_route

# Wybierz start i koniec
#   Dodaj start do koncowej sciezki
#   Rozlosuj polaczenia rzeczywiste z wezlu start i dodaj wszystkich polaczonych wezlow
#   Koszt do start = 0 pozostale inf
#   Sprawdz czy start polaczony z koncem
#   Poki start i koniec sa rozne wykonuj dijkstre
#       Poki koniec nie jest w liscie odwiedzonych punktow
#       Wez nieodwiedzony wezel A o najmniejszym koszcie
#       Wez wezel B (nieodwiedzony) polaczony do A
#       Wyznacz koszt do B z A
#       Jesli mniejszy niz poprzedni koszt do B to podmien i ustaw poprzednik B jako A
#       Dodaj A do listy odwiedzonych
#   Kiedy koniec znajdzie sie w liscie odwiedzonych punktow, wykonaj podroz od startu do kolejnego punktu C
#   Do calkowitego kosztu dodaj koszt podrozy z startu do C
#   Punkt C jest uznawany za start


def rechecking(start, finish):
    final_route = []
    dijkstra_route = []

    while finish not in final_route:
        if start not in final_route:
            new_start = start
        else:
            new_start = dijkstra_route[1]
        viable_nodes = []
        edges = []
        tag = False
        while finish not in viable_nodes:
            if tag:
                return -1, "No connection"
            new_start.set_start()
            edges = new_start.get_edges()
            viable_nodes = get_nodes(new_start, edges)
            tag = True

        reset_all_nodes(viable_nodes)
        new_start.set_start()
        dijkstra_route = dijkstra(finish, edges, viable_nodes)
        dijkstra_route.append(new_start)
        dijkstra_route.reverse()
        final_route.append(new_start)

    total_cost = count_total_cost(final_route)

    return total_cost, final_route


# def weighted_keep_going(map_):
#     pass
#
#
# def weighted_rechecking(map_):
#     pass


# End of file
