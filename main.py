import customtkinter as ctk

root = ctk.CTk()


class InventoryManagement(ctk.CTkFrame):

    # Creates constructor for main frame of application

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.title('Inventory Management')
        self.grid()
        self.items = []
        root.geometry("650x450")

        self.itemCount = len(self.items)

        # Lines 23 - 36 are top of application, search feature labels/entry/buttons

        ctk.Label(self, text='Search (Item Number): ').grid(row=0,
                                                            column=1, padx=6, pady=20, sticky=ctk.E)

        self._box1 = ctk.CTkIntVar()
        self._input = ctk.CTkEntry(self, width=20, textvariable=self._box1)
        self._input.grid(row=0, column=2, padx=8, pady=20, sticky=ctk.W)

        self.btn1 = ctk.CTkButton(self, text='Search',
                                  command=self.searchInventory)
        self.btn1.grid(row=0, column=3, padx=8, pady=20, sticky=ctk.W)

        self.btn2 = ctk.CTkButton(self, text='Reset', command=self.clearSearch)
        self.btn2.grid(row=0, column=4, padx=4, pady=20, sticky=ctk.W)

        # Lines 40 - 45 is the main text area for inventory display

        self.scroll = ctk.CTkScrollbar(self)
        self.scroll.grid(row=3, column=4)
        self.text = ctk.CTkText(self, width=60, height=10, wrap=ctk.WORD,
                                yscrollcommand=self.scroll.set)
        self.text.grid(row=3, column=0, columnspan=5, padx=20, pady=20)
        self.scroll.config(command=self.text.yview)

        ctk.Label(self, text="Item Count: " + str(self.itemCount)).grid(row=4, column=0, pady=5, sticky=ctk.N)

        # Lines 49 - 75 are labels/entry boxes for new/edit item entry

        ctk.Label(self, text='Item Number ').grid(row=6, column=0, padx=6,
                                                  pady=6, sticky=ctk.W)

        self._box2 = ctk.CTkStringVar()
        self._input1 = ctk.CTkEntry(self, width=20, textvariable=self._box2)
        self._input1.grid(row=6, column=1, padx=8, pady=10, sticky=ctk.E)

        ctk.Label(self, text='Item Name ').grid(row=6, column=2, padx=6,
                                                pady=6, sticky=ctk.E)

        self._box3 = ctk.CTkStringVar()
        self._input = ctk.CTkEntry(self, width=20, textvariable=self._box3)
        self._input.grid(row=6, column=3, padx=8, pady=10, sticky=ctk.E)

        ctk.Label(self, text='On Hand ').grid(row=10, column=0, padx=6,
                                              pady=6, sticky=ctk.E)

        self._box4 = ctk.CTkStringVar()
        self._input = ctk.CTkEntry(self, width=20, textvariable=self._box4)
        self._input.grid(row=10, column=1, padx=8, pady=10, sticky=ctk.W)

        ctk.Label(self, text='Price ').grid(row=10, column=2, padx=6,
                                            pady=6, sticky=ctk.E)

        self._box5 = ctk.CTkStringVar()
        self._input = ctk.CTkEntry(self, width=20, textvariable=self._box5)
        self._input.grid(row=10, column=3, padx=8, pady=10)

        # Lines 79 - 88 are buttons for corresponding functions to add/edit/delete items from text area

        self.btn3 = ctk.CTkButton(self, text='Add Item', command=self.addItem)
        self.btn3.grid(row=11, column=1, padx=5, pady=20, sticky=ctk.W)

        self.btn4 = ctk.CTkButton(self, text='Edit Item',
                                  command=self.editItem)
        self.btn4.grid(row=11, column=2, padx=5, pady=20, sticky=ctk.W)

        self.btn4 = ctk.CTkButton(self, text='Delete Item',
                                  command=self.deleteItem)
        self.btn4.grid(row=11, column=3, padx=5, pady=20, sticky=ctk.W)

        # Lines 91 - 98 inserts headers into text area and sets focus to Item Number entry box
        self.text.insert(ctk.CTkEnd, 'Item Number' + '\t\t' + 'Item Name'
                         + '\t\t' + 'On Hand' + '\t\t' + 'Price'
                         + '\t\t')
        self.text.insert(ctk.CTkEnd,
                         '------------------------------------------------------------'
                         )
        self.text.configure(state="disabled")
        self._input1.focus_set()

    ''' addItem() function inserts headers into text area, grabs values from entry boxes 
        and appends them to a list of dictionaries if entry boxes are not empty.  It then prints
        each item(dictionary) to the text area and clears the entry boxes. '''

    def addItem(self):

        self.text.configure(state="normal")
        self.text.delete(ctk.CTkEnd, ctk.CTkEnd)
        self.text.insert(ctk.CTkEnd, 'Item Number' + '\t\t' + 'Item Name'
                         + '\t\t' + 'On Hand' + '\t\t' + 'Price'
                         + '\t\t')
        self.text.insert(ctk.CTkEnd,
                         '------------------------------------------------------------'
                         )

        items = self.items

        iNum = self._box2.get()
        iName = self._box3.get()
        oHand = self._box4.get()
        iPrice = self._box5.get()

        if (iNum != '' and iName != '' and oHand != '' and iPrice != ''):
            record = {
                0: iNum,
                1: iName,
                2: oHand,
                3: iPrice,
            }
            items.append(record)

            for item in items:
                self.text.insert(ctk.ctkEnd, item[0] + '\t\t' + item[1] + '\t\t'
                                 + item[2] + '\t\t' + item[3] + '\t\t')
        else:
            self.text.delete(1.0, ctk.ctkEnd)
            self.text.insert(ctk.ctkEnd, 'Error: One or more fields have been left blank.')

        self._box2.set('')
        self._box3.set('')
        self._box4.set('')
        self._box5.set('')
        self._input1.focus_set()

        self.text.configure(state="disabled")

        return

    ''' searchInventory() function inserts headers into text area, gets value of search box entry and compares to
        list of dictionaries.  If the search box value matches the item number key,
         it inserts the dictionaries values into the text area. '''

    def searchInventory(self):
        self.text.configure(state="normal")
        self.text.delete(1.0, ctk.ctkEnd)
        self.text.insert(ctk.ctkEnd, 'Item Number' + '\t\t' + 'Item Name'
                         + '\t\t' + 'On Hand' + '\t\t' + 'Price'
                         + '\t\t')
        self.text.insert(ctk.ctkEnd,
                         '------------------------------------------------------------'
                         )

        searchVal = str(self._box1.get())

        for item in self.items:
            if item[0] == searchVal:
                self.text.insert(ctk.ctkEnd, item[0] + '\t\t' + item[1]
                                 + '\t\t' + item[2] + '\t\t' + item[3]
                                 + '\t\t')

        self.text.configure(state="disabled")

    # Simple function attached to reset button to clear the search box

    def clearSearch(self):
        self._box1.set('')

    ''' editItem() function clears the entry boxes to prevent errors.  It then grabs the search box value and compares
        to the list of dictionaries.  If the dictionary's item number matches the value it inserts the value of the 
        dictionary into the entry boxes for editing. '''

    def editItem(self):
        self.text.configure(state="normal")
        self._box2.set('')
        self._box3.set('')
        self._box4.set('')
        self._box5.set('')

        items = self.items

        searchVal = str(self._box1.get())

        for item in items:
            if item[0] == searchVal:
                self.items.remove(item)
                self._box2.set(item[0])
                self._box3.set(item[1])
                self._box4.set(item[2])
                self._box5.set(item[3])

        self._box1.set('')
        self._input1.focus_set()

        self.text.configure(state="disabled")

    # Simple function to delete dictionary with item number that matches the search box value

    def deleteItem(self):
        self.text.configure(state="normal")
        self.text.delete(1.0, ctk.ctkEnd)
        self.text.insert(ctk.ctkEnd, 'Item Number' + '\t\t' + 'Item Name'
                         + '\t\t' + 'On Hand' + '\t\t' + 'Price'
                         + '\t\t')
        self.text.insert(ctk.ctkEnd,
                         '------------------------------------------------------------'
                         )

        items = self.items

        searchVal = str(self._box1.get())

        for item in items:
            if item[0] == searchVal:
                self.items.remove(item)

        for item in items:
            self.text.insert(ctk.ctkEnd, item[0] + '\t\t' + item[1] + '\t\t'
                             + item[2] + '\t\t' + item[3] + '\t\t')

        self._box1.set('')
        self.text.configure(state="disabled")


def main():
    InventoryManagement().mainloop()


main()
