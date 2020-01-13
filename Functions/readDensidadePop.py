import pandas as pd

def readDensidadePop(force_download=False, file=None):
    """
    Lê os dados de densidade populacional do site da pordata.
    Limpa a tabela e converte os dados numa tabela de pandas.
    
    Parameters
    -----------

    Returns
    -----------
    df: pandas df
        Dataframe de pandas com a informação das densidades populacionais de Portugal.

    """
    
    # Allows to choose a filename other than the default filename
    if file is None:
        filename_to_load = './Files/DensidadePopulacional.xlsx'
    else:
        filename_to_load = file
    
    # Reads dataframe filename
    df = pd.read_excel(filename_to_load, skiprows=11)
    
    # Deletes columns with no data
    df.drop(df.filter(regex='Unnamed').columns, axis=1, inplace=True)
    
    # Deletes lines with no data
    row_vars = ['NUTS 2013', 'NUTS I', 'NUTS II', 'NUTS III', 'Município']
    df = df.loc[df['Âmbito Geográfico'].isin(row_vars)]
        
    return df