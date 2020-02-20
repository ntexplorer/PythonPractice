from Database_Op import *

##########
# MAIN
##########

# question 1
DB_FILE = "PurchaseOrderTransactions.db"

# load the csv data into a list
csv_file = "purchase-orders.csv"
with open(csv_file) as f:
    reader = csv.reader(f)
    DATA = [line for line in reader][1:]

if not os.path.exists(DB_FILE):
    create_database(DB_FILE)
    insert_records(DB_FILE, DATA)

# question 2
total_spent(DB_FILE)
total_spent_by_month(DB_FILE)

# question 3
delete_transaction(DB_FILE, 1)
add_transaction(DB_FILE)

print_records(DB_FILE)
