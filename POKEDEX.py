#David Camilo Vinaja Acevedo IRC 9.1
#POKEDEX by Dvinaja
import requests
def obtener_info_pokemon(id_pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{id_pokemon}"
    response = requests.get(url)  
    if response.status_code == 200:
        data = response.json()
        nombre = data['name']
        tipos = [tipo['type']['name'] for tipo in data['types']]
        especie_url = data['species']['url']
        especie_response = requests.get(especie_url)
        especie_data = especie_response.json()
        region_url = especie_data['generation']['url']
        region_response = requests.get(region_url)
        region_data = region_response.json()
        region = region_data['main_region']['name']
        
        return nombre.capitalize(), tipos, region.capitalize()
    else:
        return None, None, None
def main():
    print("Bienvenido a el Pokedex ")
    id_pokemon = input("Introduce el ID del Pokémon: ")
    nombre, tipos, region = obtener_info_pokemon(id_pokemon)
    if nombre:
        print(f"Nombre: {nombre}")
        print("Tipos:")
        for tipo in tipos:
            print(f"- {tipo.capitalize()}")
        print(f"Región: {region}")
    else:
        print("No se pudo encontrar información para ese Pokémon lo siento revisa tu internet.")
if __name__ == "__main__":
    main()
