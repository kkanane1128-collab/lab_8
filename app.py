import utils                       
from utils import moyenne, est_admis  

notes = [12, 9, 15, 8, 17, 13, 19, 10]
prix = 100

if __name__ == "__main__":
    print("Exécution depuis app.py")
    
    rapport = utils.formater_rapport(notes)
    print(rapport)
    
    m = moyenne(notes)
    print(f"\nMoyenne calculée (from import) : {m:.2f}")

    prix_ttc = utils.prix_ttc(prix)
    taux_formatte = utils.TAUX_TVA * 100
    print(f"Prix TTC pour {prix} € HT (taux {taux_formatte:.0f}%) : {prix_ttc:.2f} €")

    note_test = 11
    print(f"Admis ? {est_admis(note_test)}")