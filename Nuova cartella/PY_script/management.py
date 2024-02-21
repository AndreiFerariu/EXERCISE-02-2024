from crud_operations import CRUDOperations

# Creazione di un'istanza della classe CRUDOperations
crud = CRUDOperations(
    host="192.168.2.200",
    user="ferariu_andrei",
    password="masking.assurance.vitiating.",
    database="ferariu_andrei_DBproducts"
)

# Funzione per eseguire operazioni CRUD
def execute_crud_operation(request_type, data):
    if request_type == "POST":  # Creare un nuovo prodotto
        nome = data.get('nome')
        prezzo = data.get('prezzo')
        disponibilita = data.get('disponibilita')
        if nome is not None and prezzo is not None and disponibilita is not None:
            crud.create(
                table="Products",
                nome=nome,
                prezzo=prezzo,
                disponibilita=disponibilita
            )
        else:
            print("Dati mancanti per l'operazione POST.")
    elif request_type == "GET":  # Leggere i prodotti
        prodotti = crud.read(table="Products")
        print("Record presenti nella tabella Products:")
        for prodotto in prodotti:
            print(prodotto)
    elif request_type == "PUT":  # Aggiornare un prodotto esistente
        product_id = data.get('id')
        nome = data.get('nome')
        prezzo = data.get('prezzo')
        disponibilita = data.get('disponibilita')
        if product_id is not None and nome is not None and prezzo is not None and disponibilita is not None:
            crud.update(
                table="Products",
                set_values={"nome": nome, "prezzo": prezzo, "disponibilita": disponibilita},
                conditions=f"id = {product_id}"
            )
        else:
            print("Dati mancanti per l'operazione PUT.")
    elif request_type == "DELETE":  # Eliminare un prodotto
        product_id = data.get('id')
        if product_id is not None:
            crud.delete(
                table="Products",
                conditions=f"id = {product_id}"
            )
        else:
            print("ID del prodotto mancante per l'operazione DELETE.")
    else:
        print("Comando non supportato.")
