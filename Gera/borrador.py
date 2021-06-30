libros = [["1", "Crimen y Castigo", "Fyodor Dostoyevsky", "2014", "Alianza", "Español", "Tapa blanda", 100],
          ["2", "How The World Works", "Noam Chomsky", "2018", "Penguin", "Inglés", "Tapa blanda", 50],
          ["3", "La Revolución Rusa (1891-1924)", "Orlando Figes", "2012", "Edhasa", "Español", "Tapa blanda", 150],
          ["4", "El Aleph", "Jorge Luis Borges", "2013", "De Bolsillo", "Español", "Tapa blanda", 200],
          ["5", "Corazón de Perro", "Mihail Bulgakov", "2010", "Gutenberg", "Español", "Tapa dura", 400],
          ["6", "Aguafuertes Porteñas", "Roberto Arlt", "2008", "Edicol", "Español", "Tapa blanda", 350],
          ["7", "Madame Bovary", "Gustave Flaubert", "2007", "Tusquets", "Español", "Tapa blanda", 90],
          ["8", "Leviatán", "Thomas Hobbes", "2009", "Fondo de Cultura Económica", "Español", "Tapa blanda", 65],
          ["9", "El Lobo Estepario", "Hermann Hesse", "2005", "Losada", "Español", "Tapa blanda", 20],
          ["10", "Cartero", "Charles Bukowski", "2014", "Octaedro", "Español", "Tapa blanda", 40]]

claves_biblioteca = ["ID", "Titulo", "Autor", "Edicion", "Editorial", "Idioma", "Encuadernado", "Stock"]

nueva_list = []

i = 0

while i in range(0, len(libros)-1):
    nueva_list.append(dict(zip(claves_biblioteca, libros[i])))
    i += 1

print(nueva_list)
