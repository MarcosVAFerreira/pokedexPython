import requests
import time


class Pokemon:
    BASE_URL = "https://pokeapi.co/api/v2/pokemon/"

    @classmethod
    def buscar(cls, nome):
        return requests.get(
            f"{cls.BASE_URL}{nome.lower()}"
        )


pesquisar = input("Invoque um Pokémon: ")

print("Invocando seu Pokémon...")
time.sleep(2)

pokemon = Pokemon.buscar(pesquisar)

if pokemon.status_code == 200:
    dados = pokemon.json()

    print(f"Nome: {dados['name'].title()}")
    print(f"ID: {dados['id']}")
else:
    print("Pokémon não encontrado.")