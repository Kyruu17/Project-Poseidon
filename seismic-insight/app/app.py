from flask import Flask, render_template_string
import folium
import os

app = Flask(__name__)

def create_world_map():
    # Erstelle eine einfache Weltkarte
    world_map = folium.Map(location=[0, 0], zoom_start=2)
    return world_map

@app.route('/worldmap')
def worldmap():
    try:
        # Erstelle die Weltkarte
        world_map = create_world_map()

        # Speichere die Karte als HTML-String
        map_html = world_map._repr_html_()

        # Render die Karte direkt im Browser
        return render_template_string("""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Weltkarte</title>
        </head>
        <body>
            <h2>Weltkarte</h2>
            {{ map_html|safe }}
        </body>
        </html>
        """, map_html=map_html)
    except Exception as e:
        return f"<h2>Fehler: {str(e)}</h2>"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')