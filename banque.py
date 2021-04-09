class Compte:
    def __init__(self, numeroCompte: int, nomProprietaire: str, solde: float):
        self.numeroCompte = numeroCompte
        self.nomProprietaire = nomProprietaire
        self.solde = solde

    def retrait(self, montant: float):
        self.solde = self.solde - montant

    def versement(self, montant: float):
        self.solde = self.solde + montant

    def afficherSolde(self):
        return self.solde


class CompteCourant(Compte):
    def __init__(self, numeroCompte: int, nomProprietaire: str, solde: float, autorisationDecouvert, pourcentageAgios):
        super().__init__(numeroCompte, nomProprietaire, solde)
        self.autorisationDecouvert = autorisationDecouvert
        self.pourcentageAgios = pourcentageAgios

    def appliquerAgios(self, agios: float):
        if self.solde < 0 and self.autorisationDecouvert == False:
            self.agios = agios


class CompteEpargne(Compte):
    def __init__(self, numeroCompte: int, nomProprietaire: str, solde: float, pourcentageInterets):
        super().__init__(numeroCompte, nomProprietaire, solde)
        self.pourcentageInterets = pourcentageInterets

    def appliquerInterets(self, interets: float):
        self.solde = self.solde + interets


def banque():

    compteEpargne = CompteEpargne(2019864, "Guy Tar ", 7650, 10)
    compteCourant = CompteCourant(3336667, "Guy Tar", 1250, True, 1)
    global montant

    nn = input("Quel compte voulez-vous utiliser ? Tapez 1 pour courant ou 2 pour épargne.")
    if nn == "1":
        print(f"Votre solde est de : {compteCourant.afficherSolde()}")
        nn = input("Quelle action souhaitez-vous effectuer ? Tapez 1 pour un versement ou 2 pour retrait ? ")
        if nn == "1":
            montant = float(input("De quel montant ?"))
            compteCourant.versement(montant)
            print(f"Votre nouveau solde est de : {compteCourant.afficherSolde()}")
        if nn == "2":
            montant = float(input("De quel montant ?"))
            compteCourant.retrait(montant)
            print(f"Votre nouveau solde est de : {compteCourant.afficherSolde()}")

    if nn == "2":
        print(f"Votre solde est de : {compteEpargne.afficherSolde()}")
        nn = input("Quelle action souhaitez-vous effectuer ? Tapez 1 pour un versement ou 2 pour retrait ? ")
        if nn == "1":
            montant = float(input("De quel montant ?"))
            compteEpargne.versement(montant)
            print(f"Votre nouveau solde est de : {compteEpargne.afficherSolde()}")
        if nn == "2":
            montant = float(input("De quel montant ?"))
            compteEpargne.retrait(montant)
            print(f"Votre nouveau solde est de : {compteEpargne.afficherSolde()}")



banque()
