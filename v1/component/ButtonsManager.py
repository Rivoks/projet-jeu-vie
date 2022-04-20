from tkinter import *
from component.Board import *

class ButtonsManager:

    def __init__(self, mainGame):
        self.mainGame = mainGame

    def Go(self):
        #"démarrage de l'animation"
        if self.mainGame.flag == 1:
            return
        self.mainGame.flag = 1
        self.mainGame.board.Draw(self.mainGame.graphicSetting)
        self.mainGame.mainLoop()
        self.mainGame.window.mainloop()

    def Stop(self):
        #"arrêt de l'animation"
        self.mainGame.flag = 0
        print("Arrêt de la simulation")
    
    def Change_vit(self, event): #fonction pour changer la vitesse(l'attente entre chaque Ã©tape)
        self.mainGame.TARGETEDDELTATIME = int(eval(self.entree.get()))
        print("Changement du temps d'update du Board : {tdr}".format(tdr = self.mainGame.TARGETEDDELTATIME))

    def Change_rayon(self, event): #fonction pour changer la vitesse(l'attente entre chaque étape)        
        Board.neighbourRadius = int(eval(self.entree2.get()))
        print("Changement du rayon du Board : {neig}".format(neig = Board.neighbourRadius))

    def CreateButtons(self, window):
        self.b1 = Button(window, text = 'Go!', command = self.Go)
        self.b1.pack(side = LEFT, padx = 3, pady = 3)
        self.b2 = Button(window, text = 'Stop', command = self.Stop)
        self.b2.pack(side = LEFT, padx = 3, pady = 3)
        self.entree = Entry(window)
        self.entree.bind("<Return>", self.Change_vit)
        self.entree.pack(side = RIGHT)
        self.chaine = Label(window)
        self.chaine.configure(text = "TIME (ms) :")
        self.chaine.pack(side = RIGHT)
        self.chaine2 = Label(window)
        self.chaine2.configure(text = "Rayon :")
        self.chaine2.pack(side = LEFT, padx = 3, pady = 3)
        self.entree2 = Entry(window)
        self.entree2.bind("<Return>", self.Change_rayon)
        self.entree2.pack(side = LEFT, padx = 3, pady = 3)