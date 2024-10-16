import pandas as pd





def find_plant_info(plants):
    nutrients_file = 'static/data_uptake.csv'
    water_file = 'static/water_data.csv'
    nutrients_df = pd.read_csv(nutrients_file, sep=';', encoding='ISO-8859-1')
    water_df = pd.read_csv(water_file)

    ##plants = input("Entrez le(s) nom(s) de plante(s) que vous voulez (séparées par 'et') : ").strip().lower()
    plants_list = [plant.strip() for plant in plants.split('et')]

    available_plants_nutrients = nutrients_df['Culture'].str.lower().tolist()
    available_plants_water = water_df['Culture'].str.lower().tolist()
    
    
    results = {}

    for plant in plants_list:
        if plant in available_plants_nutrients and plant in available_plants_water:

            nutrients = nutrients_df[nutrients_df['Culture'].str.lower() == plant].iloc[0]
            water = water_df[water_df['Culture'].str.lower() == plant].iloc[0]

            results[plant.capitalize()] = {
                'azote': nutrients['Azote (N)'],
                'phosphore': nutrients['Phosphore (P2O5)'],
                'potassium': nutrients['Potassium (K2O)'],
                'soufre': nutrients['Soufre (S)'],
                'water_requirement': water['Water Requirement (litres/day)']
            }
        else:
            results[plant.capitalize()] = {
                'message': f"Désolé, les données pour la plante '{plant.capitalize()}' ne sont pas disponibles."
            }

    if not results:
        return {"message": "Aucune plante valide n'a été trouvée."}

    return results

            
 

if __name__ == "__main__" : 
    find_plant_info()
