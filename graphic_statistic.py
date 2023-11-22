from importlib.metadata import requires
import pandas as pd
import matplotlib.pyplot as plt

# Inclure toutes les colonnes nécessaires
colonnes_a_lire = ['Continent', 'Utilisateurs', 'Taux de rebond', 'Sessions', 'Chiffre d\'affaires', 'Catégorie d\'appareil', 'Date']

# Lire le fichier CSV
df = pd.read_csv('bdd_python_base.csv', sep=';', usecols=colonnes_a_lire)

# Convertir et nettoyer les données
df['Date'] = pd.to_datetime(df['Date'], format='%Y%m%d')
df['Utilisateurs'] = pd.to_numeric(df['Utilisateurs'], errors='coerce')
df['Sessions'] = pd.to_numeric(df['Sessions'], errors='coerce')
df['Chiffre d\'affaires'] = pd.to_numeric(df['Chiffre d\'affaires'], errors='coerce')
df['Taux de rebond'] = df['Taux de rebond'].str.rstrip('%').astype('float') / 100
df.fillna(0, inplace=True)

# Créer les graphiques
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(15, 10))
df.groupby('Continent')['Utilisateurs'].sum().plot(kind='bar', ax=axes[0,0], title='Utilisateurs par Continent')
df.groupby('Date')['Chiffre d\'affaires'].sum().plot(kind='line', ax=axes[0,1], title='Chiffre d\'affaires au Fil du Temps')
df.groupby('Catégorie d\'appareil')['Sessions'].sum().plot(kind='pie', autopct='%1.1f%%', ax=axes[1,0], title='Sessions par Catégorie d\'appareil')
df['Taux de rebond'].plot(kind='hist', bins=20, ax=axes[1,1], title='Distribution du Taux de Rebond', edgecolor='white')

plt.tight_layout()
plt.show()