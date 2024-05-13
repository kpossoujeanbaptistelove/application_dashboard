import streamlit as st

# Données factices pour les véhicules et les dépenses
vehicules = []
depenses = []

def main():
    st.title("Dashboard")

    page = st.sidebar.selectbox("Menu", ["Accueil", "Historique des enregistrements", "Enregistrer un véhicule", "Enregistrer une dépense"])

    if page == "Accueil":
        afficher_accueil()
    elif page == "Historique des enregistrements":
        afficher_historique()
    elif page == "Enregistrer un véhicule":
        enregistrer_vehicule()
    elif page == "Enregistrer une dépense":
        enregistrer_depense()

def afficher_accueil():
    st.header("Accueil")
    st.write("Bienvenue sur notre dashboard. Utilisez le menu sur la gauche pour naviguer.")

def afficher_historique():
    st.header("Historique des enregistrements")
    st.subheader("Véhicules enregistrés :")
    for vehicule in vehicules:
        st.write(f"{vehicule['nom']} - {vehicule['modele']} ({vehicule['annee']})")

    st.subheader("Dépenses enregistrées :")
    for depense in depenses:
        st.write(f"{depense['vehicule']} - {depense['montant']}€ : {depense['description']}")

def enregistrer_vehicule():
    st.header("Enregistrer un nouveau véhicule")
    nom = st.text_input("Nom")
    modele = st.text_input("Modèle")
    annee = st.text_input("Année")
    if st.button("Enregistrer"):
        vehicules.append({'nom': nom, 'modele': modele, 'annee': annee})
        st.success("Véhicule enregistré avec succès.")

def enregistrer_depense():
    st.header("Enregistrer une dépense de véhicule")
    vehicule = st.selectbox("Véhicule", [v['nom'] for v in vehicules])
    montant = st.text_input("Montant")
    description = st.text_area("Description")
    if st.button("Enregistrer"):
        depenses.append({'vehicule': vehicule, 'montant': montant, 'description': description})
        st.success("Dépense enregistrée avec succès.")

if __name__ == "__main__":
    main()
