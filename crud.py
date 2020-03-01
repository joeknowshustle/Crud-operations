


store_items2 = {
            "Apples": {
                "Cost": .5,
                "Qty": 10},

            "Banana": {
                "Cost": .99,
                "Qty": 10},

            "Oranges": {
                "Cost": .99,
                "Qty": 10},

            "Wheat": {
                "Cost": 2.00,
                "Qty": 10}
            }


def put():
    name = input("enter item name to update: ")
    if name in store_items2:
        cost = float(input("enter new cost"))
        qty = int(input("enter new qty"))
        store_items2[name]["Cost"] = cost
        store_items2[name]["Qty"] = qty
        print(store_items2)


def get():
    running = True
    while running:
        name = input("enter name to view it's attrabutes press ENTER to quit ")
        if name == '':
            running = False
        elif name not in store_items2:
            print("Item does not exist try again")
            continue
        elif name in store_items2. keys():
            print(store_items2[name])


def delete():
    running = True
    while running:
        name = input("Enter Item name to delete")
        if name in store_items2.keys():
            del store_items2[name]
            print(store_items2)



def post():
    running = True
    while running:
        name = input("Enter the name to add")
        if name in store_items2:
            print("item already exists!")
            continue
        else:
            cost = float(input("Enter Price "))
            qty = int(input("Enter qty "))
            if name not in store_items2.keys():
                store_items2[f"{name}"] = {"Cost": cost, "Qty": qty,}
                print(store_items2)
        more_items = input("Would you like to add more items? ")
        if more_items == 'y':
            continue
        else:
            running = False


if __name__ == "__main__":
    print("1) post")
    print("2) Put")
    print("3) Get")
    print("4) Delete")
    sel_input = input("Make a selection from the following choices")
    if sel_input =='1':
        post()
    elif sel_input =='2':
        put()

    elif sel_input == '3':
        get()
    elif sel_input == '4':
        delete()







