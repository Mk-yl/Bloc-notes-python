import os
from datetime import datetime

class Note:
    def __init__(self, contenu, date=datetime.now()):
        self.contenu = contenu
        self.date = date

class NotePersonnelle(Note):
    def __init__(self, contenu, auteur):
        super().__init__(contenu)
        self.auteur = auteur

class BlocNotes:
    def __init__(self, fichier="bloc_notes.txt"):
        self.fichier = fichier
        self.liste_notes = self.charger_notes()

    def ajouter_note(self, contenu_note, auteur):
        note = NotePersonnelle(contenu_note, auteur)
        self.liste_notes.append(note)
        print("Note ajoutée avec succès.")

    def lire_notes(self):
        if not self.liste_notes:
            print("Le bloc-notes est vide.")
        else:
            print("Contenu du bloc-notes :")
            for index, note in enumerate(self.liste_notes, start=1):
                print(f"{index}. Auteur: {note.auteur}, Contenu: {note.contenu}")

    def rechercher_notes(self, mot_cle):
        notes_correspondantes = [note for note in self.liste_notes if mot_cle in note.contenu]
        if not notes_correspondantes:
            print(f"Aucune note ne contient le mot-clé '{mot_cle}'.")
        else:
            print(f"Notes correspondantes au mot-clé '{mot_cle}' :")
            for index, note in enumerate(notes_correspondantes, start=1):
                print(f"{index}. Auteur: {note.auteur}, Contenu: {note.contenu}")

    def afficher_notes_par_auteur(self, auteur):
        notes_auteur = [note for note in self.liste_notes if isinstance(note, NotePersonnelle) and note.auteur == auteur]
        if not notes_auteur:
            print(f"Aucune note pour l'auteur '{auteur}'.")
        else:
            print(f"Notes de l'auteur '{auteur}' :")
            for index, note in enumerate(notes_auteur, start=1):
                print(f"{index}. Contenu: {note.contenu}")

    def sauvegarder_notes(self):
        with open(self.fichier, 'w') as fichier:
            for note in self.liste_notes:
                if isinstance(note, NotePersonnelle):
                    fichier.write(f"{note.auteur}: {note.contenu}\n")
        print("Le bloc-notes a été sauvegardé avec succès dans le fichier", self.fichier)

    def charger_notes(self):
        if os.path.exists(self.fichier):
            with open(self.fichier, 'r') as fichier:
                lignes = fichier.readlines()
                return [self.creer_note_de_ligne(ligne.strip()) for ligne in lignes]
        else:
            return []

    def creer_note_de_ligne(self, ligne):
        elements = ligne.split(": ", 1)
        if len(elements) == 2:
            auteur, contenu = elements
            return NotePersonnelle(contenu, auteur)
        else:
            return NotePersonnelle(ligne, "Auteur Inconnu")

if __name__ == "__main__":
    bloc_notes = BlocNotes()

    while True:
        print("\nMenu du bloc-notes:")
        print("1. Ajouter une note")
        print("2. Lire le bloc-notes")
        print("3. Rechercher dans le bloc-notes")
        print("4. Afficher les notes par auteur")
        print("5. Sauvegarder le bloc-notes")
        print("6. Quitter")

        choix = input("Faites votre choix : ")

        if choix == "1":
            contenu_note = input("Entrez votre note : ")
            auteur = input("Entrez le nom de l'auteur : ")
            bloc_notes.ajouter_note(contenu_note, auteur)
        elif choix == "2":
            bloc_notes.lire_notes()
        elif choix == "3":
            mot_cle = input("Entrez un mot-clé à rechercher : ")
            bloc_notes.rechercher_notes(mot_cle)
        elif choix == "4":
            auteur = input("Entrez le nom de l'auteur : ")
            bloc_notes.afficher_notes_par_auteur(auteur)
        elif choix == "5":
            bloc_notes.sauvegarder_notes()
        elif choix == "6":
            print("Merci d'avoir utilisé le bloc-notes. Au revoir!")
            break
        else:
            print("Choix invalide. Veuillez sélectionner une option valide.")
