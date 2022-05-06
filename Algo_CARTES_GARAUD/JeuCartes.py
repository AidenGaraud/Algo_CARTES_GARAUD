
#Exo 1 :
#Définition de la classe Carte
class Carte :
    def __init__(self,name, life, mana, description) :
        self.mana = mana
        self.nom = name
        self.vie = life
        self.description = description
    def afficheCarte (self):
        print (self.nom, self.vie, self.mana, self.description)
    def perteDeVie (self,damage):
        print (self.nom,"n'a plus que ",self.vie-damage)

#Exo 3 :
#Définition de la classe Cristal
class Cristal(Carte) :
    def __init__(self, value, cost) :
        self.valeur = value
        self.cout = cost

#Exo 4 :
#Définition de la classe Creature
class Creature(Carte) :
    def __init__(self, life, attack, cost)  :
        self.vie = life
        self.attaque = attack
        self.cout = cost
    def attaqueMage (self) :
        self.vie - self.attaque         

#Exo 5 :
#Définition de la classe Blast
class Blast(Carte) :
    def __init__(self, value, name) :
        Carte.__init__(self, name)
        self.valeur = value
    def perteVie (self, damage) :
        print  ("Il ne reste plus que",self.vie-damage ,"de vie à", self.nom, "a cause des dégâts du Blast")
    def defausseBlast (self) :
        self.valeur = 0


#Exo 2 :
#Définition de la classe Mage
class Mage :
    def __init__(self,name, life, mana) :
        self.nom = name
        self.vie = life
        self.mana = mana
        self.zoneJeu = []
        self.main = [Creature(Carte)("Feu follet",11,5,3),Creature(Carte)("Esprit du vent",8,7,3)]
        self.defausse =[]
    def afficheMage (self):
        print (self.nom, self.vie, self.mana)
    def mainMage(self):
        for i in self.main:
            i.afficheCarte()
    def invocation (self, cost, choix):
        self.mana - cost 
        self.zoneJeu.append(self.main[choix])
    def attaqueMage (self):
        damage = 2
        for i in self.zoneJeu:
            i.afficheCarte()
            damage = int(i.attaque)
        print (self.nom,"n'a plus que ",self.vie-damage)



#Joueurs Mages
j1 = Mage("Dumbeldore",15,5)
j2 = Mage("Gandalf",15,5)

j1.mainMage()
j2.mainMage()

#Introduction
print("Bienvenue au Royaume des cartes !")
print("Le jeu va commencer :")

#Choix des cartes
nbchoisi = int(input("Dumbeldore, veuillez choisir la carte que vous souhaitez invoquer via sa place dans votre main :"))
j1.invocation(2,nbchoisi-1)
j1.zoneJeu[0].afficheCarte()

nbchoisi = int(input("Gandalf, veuillez choisir la carte que vous souhaitez invoquer via sa place dans votre main :"))
j2.invocation(2,nbchoisi-1)
j2.zoneJeu[0].afficheCarte()
