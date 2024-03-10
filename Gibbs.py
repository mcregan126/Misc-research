import pandas as pd
from jazzy.api import deltag_from_smiles
from jazzy.api import molecular_vector_from_smiles
df = pd.read_csv('linker_infoR copy.csv')


for index, row in df.iterrows():
    abbreviation = row['Abbreviations']
    name = row['Name']
    smiles = row['Smiles']
    # Print out the data for each element
    #print(f"Abbreviation: {abbreviation}")
    #print(f"SMILES: {smiles}")

   # print(molecular_vector_from_smiles(smiles))
    vector_data = molecular_vector_from_smiles(smiles)
    sdc_value = vector_data['dgtot']
    print(sdc_value)

    #print(deltag_from_smiles(smiles))

  