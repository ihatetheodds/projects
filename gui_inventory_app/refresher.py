import sys
import random
import customtkinter


class item:
    def __init__(self,name,quantity,price):
        self.name = name
        self.quanity = quantity 
        self.price = price

    def displayItem(self):
        print(f"I am a {self.name}")

    def amount(self):
        print(f"The amount is {self.quanity}")

    def __str__(self):
        return f"{self.name} (Qty: {self.quanity}, Price: {self.price})"
    

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x150")
        self.inventory = [item("test",1,1)]
        
        self.inventory_button = customtkinter.CTkButton(self,text="Display the inventory", command=self.display_inventory)
        self.inventory_button.pack(padx=20, pady=20)
        
        self.search_item_button = customtkinter.CTkButton(self,text="Search Items", command=self.search_items)
        self.search_item_button.pack(padx=40, pady=20)

        self.add_item_button = customtkinter.CTkButton(self,text="Add Items", command=self.add_items)
        self.add_item_button.pack(padx=60, pady=20)

        self.delete_item_button = customtkinter.CTkButton(self,text="Delete Items", command=self.delete_items)
        self.delete_item_button.pack(padx=60, pady=20)
        
        
        self.textbox = customtkinter.CTkTextbox(master=self,width=300,corner_radius=0)
        self.textbox.pack(padx=50, pady=50)
        
        self.inputbox = customtkinter.CTkEntry(self)
        self.inputbox.pack(padx=20, pady=5)
       
        
    def delete_items(self):
        self.cleartextbox()
        
        itemName = self.inputbox.get()
        found = False

        for items in self.inventory:
            if items.name == itemName:
                self.inventory.remove(items)
        self.clearinputbox()

        

        # Text box
       
    def search_items(self):
        self.cleartextbox()
        self.clearinputbox()

        found = False

        itemName = self.inputbox.get()

        for items in self.inventory:
            if items.name == itemName:
                self.textbox.insert("end",items)
                found = True
        if not found:
            self.textbox.insert("end","item not found")
                

    def add_items(self):
        self.cleartextbox()
        
        items = self.inputbox.get()
        
        name, qty, price = items.split()
        self.inventory.append(item(name,qty,price))
        self.clearinputbox()

        
        
    
        

    def display_inventory(self):
        self.cleartextbox()
        self.clearinputbox()
        
        
        for items in self.inventory:

            self.textbox.insert("end",str(items) + "\n")
            

    

    def cleartextbox(self):
        self.textbox.delete(0.0, "end")

    def clearinputbox(self):
        self.inputbox.delete(0,"end")

        