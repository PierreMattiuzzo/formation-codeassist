"""Petite application Streamlit : liste et filtre des tickets de support.

Lancer avec :  streamlit run app.py
"""
import streamlit as st
from data import charger_tickets, filtrer_tickets

st.set_page_config(page_title="Tickets de support", page_icon="🎫")
st.title("🎫 Tickets de support")

df = charger_tickets()

# Filtres dans la barre latérale
st.sidebar.header("Filtres")
priorites = ["Toutes"] + sorted(df["priorite"].unique().tolist())
priorite = st.sidebar.selectbox("Priorité", priorites)
recherche = st.sidebar.text_input("Rechercher dans la description")

tickets = filtrer_tickets(df, priorite, recherche)

# Affichage
st.subheader(f"{len(tickets)} ticket(s)")
st.dataframe(tickets, use_container_width=True, hide_index=True)

st.subheader("Répartition par priorité")
st.bar_chart(tickets["priorite"].value_counts())
