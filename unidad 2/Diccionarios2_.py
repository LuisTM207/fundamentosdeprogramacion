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

    },
     "978-84-204-5025-8": {
        "título": "lobo estepario",
        "autor": ["Miguel de Cervantes Saavedra"],
        "géneros": ["Novela de drama", "satira"]
    

    },

     "978-84-204-6000-9": {
        "título": "diario de greg",
        "autor": ["jeef kenedy"],
        "géneros": ["comedia", "ficcion"]



    },

     "978-84-204-7000-10": {
        "título": "pedro paramo",
        "autor": ["juan rulfo"],
        "géneros": ["novela", "ficcion"]
{


}

isbn = "978-84-376-0494-7"
info_libro = biblioteca.get(isbn)          
print("\nInformación del libro:", info_libro)

