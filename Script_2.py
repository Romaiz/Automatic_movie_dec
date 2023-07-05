from pyvis.network import Network
import json

File = "movies.json"


def get_data(file):
    with open(file, "r") as json_file:
        data = json.load(json_file)
        return data


def map_data(data, name_color="#FB2576", genre_color="#332FD0", edge_color="#DCD6F7", name_shape="dot", genre_shape="triangle"):
    g = Network(height="720px", width="100%",
                bgcolor="#3F0071", font_color="white")

    for tidbit in data:
        name = tidbit["title"]
        g.add_node(name, color=name_color)
        genres = tidbit["genre"]
        for genre in genres:
            g.add_node(genre, color=genre_color, shape=genre_shape)
            g.add_edge(name, genre, color=edge_color)

    g.force_atlas_2based()
    g.write_html("movies_map.html")


movies_data = get_data(File)
map_data(movies_data)
