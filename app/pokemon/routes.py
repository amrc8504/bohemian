from flask import Blueprint, redirect, render_template, request, url_for
import requests as r

pokemon = Blueprint('pokemon', __name__, template_folder="pokemon_templates")


@pokemon.route('/pokemon', methods=["POST"])
def myPokemon():
    name = request.form.to_dict()['name']
    data = r.get(f"https://pokeapi.co/api/v2/pokemon/{name}")
    if data.status_code == 200:
        my_data = data.json()
        moves = my_data['moves']
        my_moves = []
        for item in moves:
            my_moves.append((item['move']['name']))
        my_img = my_data['sprites']['front_default']
        return render_template('pokemon.html', moves=my_moves, img_url=my_img, name=name)
    return redirect(url_for('home'))