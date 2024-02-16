from crud_operations import CRUDOperations

# Creazione di un'istanza della classe CRUDOperations
crud = CRUDOperations(
    host="192.168.2.200",
    user="ferariu_andrei",
    password="masking.assurance.vitiating.",
    database="ferariu_andrei_DBproducts"
)

# Esempio di inserimento di un record nella tabella "Products"
crud.create(
    table="Products",
    nome="Prodotto1",
    prezzo=19.99,
    disponibilita=True
)

# Funzione per eseguire operazioni CRUD
def execute_crud_operation(operation):
    if operation == 1:  # Creare un nuovo prodotto
        nome = input("Inserisci il nome del prodotto: ")
        prezzo = float(input("Inserisci il prezzo del prodotto: "))
        disponibilita = input("Il prodotto è disponibile? (Sì/No): ").lower() == "sì"
        crud.create(
            table="Products",
            nome=nome,
            prezzo=prezzo,
            disponibilita=disponibilita
        )
    elif operation == 2:  # Leggere i prodotti
        prodotti = crud.read(table="Products")
        print("Record presenti nella tabella Products:")
        for prodotto in prodotti:
            print(prodotto)
    elif operation == 3:  # Aggiornare un prodotto esistente
        product_id = int(input("Inserisci l'ID del prodotto da aggiornare: "))
        nome = input("Inserisci il nuovo nome del prodotto: ")
        prezzo = float(input("Inserisci il nuovo prezzo del prodotto: "))
        disponibilita = input("Il prodotto è ancora disponibile? (Sì/No): ").lower() == "sì"
        crud.update(
            table="Products",
            set_values={"nome": nome, "prezzo": prezzo, "disponibilita": disponibilita},
            conditions=f"id = {product_id}"
        )
    elif operation == 4:  # Eliminare un prodotto
        product_id = int(input("Inserisci l'ID del prodotto da eliminare: "))
        crud.delete(
            table="Products",
            conditions=f"id = {product_id}"
        )
    else:
        print("Operazione non valida. Scegli tra '1', '2', '3' o '4'.")

# Esempi di utilizzo dello switch case per le operazioni CRUD
while True:
    print("\nMenu Operazioni CRUD:")
    print("1. Creare un nuovo prodotto")
    print("2. Leggere i prodotti")
    print("3. Aggiornare un prodotto esistente")
    print("4. Eliminare un prodotto")
    print("5. Uscire")
    choice = input("Scelta: ")

    if choice == "5":
        print("Uscita...")
        break

    try:
        operation = int(choice)
        execute_crud_operation(operation)
    except ValueError:
        print("Input non valido. Inserisci un numero da 1 a 5.")