import requests
import gradio as gr

def buscar_pokemon(nome):
    resposta = requests.get(f"https://pokeapi.co/api/v2/pokemon/{nome.lower()}")

    if resposta.status_code != 200:
        return None, "Pokémon não encontrado"

    dados = resposta.json()

    imagem = dados["sprites"]["other"]["official-artwork"]["front_default"]
    tipos = ", ".join(tipo["type"]["name"].title() for tipo in dados["types"])

    texto = f"""
    Nº {dados['id']:04d}
    Nome: {dados['name'].title()}
    Tipos: {tipos}
    """

    return imagem, texto


interface = gr.Interface(
    fn=buscar_pokemon,
    inputs=gr.Textbox(label="Pokémon"),
    outputs=[
        gr.Image(label="Imagem"),
        gr.Textbox(label="Informações")
    ]
)

interface.launch()