import json

biblioteca = {
    "978-84-376-0494-7": {
        "título": "Cien años de soledad",
        "autor": ["Gabriel García Márquez"],
        "géneros": ["Realismo mágico", "Novela histórica"]
    },
    "978-84-204-1625-5": {
        "título": "Don Quijote de la Mancha",
        "autor": ["Miguel de Cervantes Saavedra"],
        "géneros": ["Novela de caballería", "Satira"]
    }


     "978-84-204-1625-5": {
        "título": "lobo estepario",
        "autor": ["Miguel de Cervantes Saavedra"],
        "géneros": ["Novela de drama", "Satira"]
    }



     "978-84-204-1625-5": {
        "título": "diario de greg",
        "autor": ["jeef kenedy"],
        "géneros": ["comedia", "Satira"]
    }



}

isbn = "978-84-376-0494-7"
info_libro = biblioteca.get(isbn)          
print("\nInformación del libro:", info_libro)