import numpy as np
import matplotlib.pyplot as plt

import argparse
import time

# Pour réaliser ce code on a suivi le tutoriel disponible ici -> https://www.tutorialspoint.com/conway-s-game-of-life-using-python


# Ici on créée notre tableau
class Board(object):
    def __init__(self, size, seed='Random'):
        if seed == 'Random':
            self.state = np.random.randint(2, size=size)

        # On initialise la case dans l'état du tableau (state)
        self.engine = Engine(self)

        # On commence notre cycle à 0
        self.iteration = 0

    def animate(self):
        i = self.iteration
        im = None
        plt.title("Conway's Game of Life")

        # On exécute le code en boucle pour toutes les cases du tableau
        while True:
            # Active l'interaction avec l'interface (save, etc...)
            if i == 0:
                plt.ion()
                im = plt.imshow(self.state, vmin=0, vmax=2, cmap=plt.cm.gray)
            else:
                im.set_data(self.state)

            # On passe au tour suivant
            i += 1
            # On applique les règle à notre case
            self.engine.applyRules()

            print('Life Cycle: {} Birth: {} Survive: {}'.format(
                i, self.engine.nBirth, self.engine.nSurvive))

            # Vitesse de défilement
            plt.pause(1)

            # On utilise 'yield' pour générer l'objet que l'on vient de d'initialiser plus haut
            yield self


# Ici on créée la classe associée à une case
class Engine(object):
    def __init__(self, board):
        self.state = board.state

    # Définition des règles par rapport au voisinnage
    def countNeighbors(self):
        state = self.state
        n = (state[0:-2, 0:-2] + state[0:-2, 1:-1] + state[0:-2, 2:] +
             state[1:-1, 0:-2] + state[1:-1, 2:] + state[2:, 0:-2] +
             state[2:, 1:-1] + state[2:, 2:])
        return n

    # Définition des règles générales
    # C'est ici où l'on va potentiellement pouvoir faire varier les conditions
    # de départ de notre jeu
    def applyRules(self):
        n = self.countNeighbors()  # Nombre de voisin
        state = self.state
        birth = (n == 3) & (state[1:-1, 1:-1] == 0)  # Règle pour une naissance
        survive = ((n == 2) | (n == 3)) & (
            state[1:-1, 1:-1] == 1)  # Règle pour survivre
        state[...] = 0
        state[1:-1, 1:-1][birth | survive] = 1
        nBirth = np.sum(birth)  # Nombre de naissance totale
        self.nBirth = nBirth
        nSurvive = np.sum(survive)  # Nombre de survie au moment t
        self.nSurvive = nSurvive
        return state


# Dans notre main() on exécute le jeu
def main():

    # On définit la taile de notre tableau
    board_size = 128

    ap = argparse.ArgumentParser(add_help=False)  # Intilialize Argument Parser

    ap.add_argument('-h', '--height', help='Board Height',
                    default=board_size)
    ap.add_argument('-w', '--width', help='Board Width', default=board_size)

    args = vars(ap.parse_args())  # Gather Arguments
    bHeight = int(args['height'])
    bWidth = int(args['width'])
    board = Board((bHeight, bWidth))

    for _ in board.animate():  # On anime notre tableau en boucle
        pass


if __name__ == '__main__':
    main()
