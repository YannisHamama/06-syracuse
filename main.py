"""Permet de calculer la suite de syracuse et am tv tva"""
from typing import List
#### Fonctions secondaires


# imports
from plotly.graph_objects import Scatter, Figure

### NE PAS MODIFIER ###
def syr_plot(lsyr):
    """Trace la suite de Syracuse à l’aide de Plotly.

    Cette fonction génère et affiche un graphique représentant l’évolution
    des valeurs de la suite de Syracuse (ou suite de Collatz) en fonction du
    nombre d’itérations. L’axe des abscisses représente le rang de chaque
    terme, et l’axe des ordonnées sa valeur correspondante.

    Args:
        lsyr (list[int]): la suite de Syracuse à tracer, typiquement obtenue
            via la fonction `syracuse_l`.

    Returns:
        None: cette fonction ne renvoie rien, elle affiche simplement la figure.
    """
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({  'layout':   { 'title': {'text': title},
                                'xaxis': {'title': {'text':"x"}},
                                'yaxis': {'title': {'text':"y"}},
                                }
                }
    )

    x = [ i for i in range(len(lsyr)) ]
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color = "blue")
    fig.add_trace(t)
    fig.show()
    # fig.write_html('fig.html', include_plotlyjs='cdn')
    return None
#######################

def syracuse_l(n: int) -> List[int]:
    """Retourne la suite de Syracuse (Collatz) en partant de la source n.

    Args:
        n (int): la valeur initiale (source) > 0

    Returns:
        list[int]: la suite de Syracuse qui finit par 1 (inclut 1)
    """
    suite_syracuse: List[int] = []
    while n != 1:
        suite_syracuse.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    suite_syracuse.append(1)
    return suite_syracuse

def temps_de_vol(l):
    """Retourne le temps de vol d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol
    """    
    return len(l)-1

def temps_de_vol_en_altitude(l):
    """Retourne le temps de vol en altitude d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol en altitude
    """
    if not l:
        return 0
    origine = l[0]
    # commencer à partir de l'indice 1 (indice 0 est la source)
    for i in range(1, len(l)):
        if l[i] < origine:
            return i - 1
    return len(l) -1     


def altitude_maximale(l):
    """retourne l'altitude maximale d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: l'altitude maximale
    """    
    if not l:
        return 0
    return max(l)
#### Fonction principale


def main():
    """
    lance les fonctions secondaire et definit les arguments
    """
    # vos appels à la fonction secondaire ici
    lsyr = syracuse_l(15)
    # affichage / tracé (syr_plot doit être défini ailleurs)
    try:
        syr_plot(lsyr)
    except NameError:
        # si syr_plot n'existe pas, on ignore le tracé (utile pour tests unitaires)
        pass

    print(temps_de_vol(lsyr))
    print(temps_de_vol_en_altitude(lsyr))
    print(altitude_maximale(lsyr))

if __name__ == "__main__":
    main()
