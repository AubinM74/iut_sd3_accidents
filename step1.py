import pandas as pd

# Chargement des fichiers CSV
data_carac = pd.read_csv('data/carac.csv', sep=';')
data_lieux = pd.read_csv('data/lieux.csv', sep=';')
data_veh = pd.read_csv('data/veh.csv', sep=';')
data_vict = pd.read_csv('data/vict.csv', sep=';')

# Fusion des DataFrames sur la colonne commune 'id'
merged_data = pd.merge(data_carac, data_lieux, on='Num_Acc')
merged_data = pd.merge(merged_data, data_veh, on='Num_Acc')
merged_data = pd.merge(merged_data, data_vict, on='Num_Acc')

merged_data.to_csv('merged_data.csv', index=False)
