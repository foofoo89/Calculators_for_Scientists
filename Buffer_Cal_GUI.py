from tkinter import *
from tkinter import ttk
from builtins import int
from pygments.styles.paraiso_dark import BLUE

def bufferC(*args):
    try:
        Vol = float(Volume.get())
        Wvol1 = Vol
        try:
            Stchema1 = float(Stchem1.get())
            Dechema1 = float(Dechem1.get())
            if Stchema1 > 0 and Dechema1 >0:
                Vchema1 = ((Dechema1 * Vol) / Stchema1)
                G1.set(Vchema1)
                Wvol1 -= Vchema1
                
                if Vchema1 > Vol:
                    G1.set("Error")
            else:
                G1.set(0)
                    
        except ValueError:
            G1.set("Numerical value only")
            
        if Wvol1 > 0:
             Y1.set(Wvol1)
        if Wvol1 <= 0:
            Y1.set("Error")    
            
        try:
            Stchema2 = float(Stchem2.get())
            Dechema2 = float(Dechem2.get())
            if Stchema2 > 0 and Dechema2 >0:
                Vchema2 = ((Dechema2 * Vol) / Stchema2)
                G2.set(Vchema2)
                Wvol1 -= Vchema2
                
                if Vchema2 > Vol:
                    G2.set("Error")
                    
            else:
                G2.set(0)
                    
        except ValueError:
            G2.set("Numerical value only")
            
        if Wvol1 > 0:
            Y1.set(Wvol1)
        if Wvol1 <= 0:
            Y1.set("Error")
            
        try:
            Stchema3 = float(Stchem3.get())
            Dechema3 = float(Dechem3.get())
            if Stchema3 > 0 and Dechema3 >0:
                Vchema3 = ((Dechema3 * Vol) / Stchema3)
                G3.set(Vchema3)
                Wvol1 -= Vchema3
                
                if Vchema3 > Vol:
                    G3.set("Error")
                    
            else:
                G3.set(0)
                    
        except ValueError:
            G3.set("Numerical value only")
            
        if Wvol1 > 0:
            Y1.set(Wvol1)
        if Wvol1 <= 0:
            Y1.set("Error")
                      
        try:
            Stchema4 = float(Stchem4.get())
            Dechema4 = float(Dechem4.get())
            if Stchema4 > 0 and Dechema4 >0:
                Vchema4 = ((Dechema4 * Vol) / Stchema4)
                G4.set(Vchema4)
                Wvol1 -= Vchema4
                
                if Vchema4 > Vol:
                    G4.set("Error")
                    
            else:
                G4.set(0)
                    
        except ValueError:
            G4.set("Numerical value only")
            
        if Wvol1 > 0:
            Y1.set(Wvol1)
        if Wvol1 <= 0:
            Y1.set("Error")
                
        try:
            Stchema5 = float(Stchem5.get())
            Dechema5 = float(Dechem5.get())
            if Stchema5 > 0 and Dechema5 >0:
                Vchema5 = ((Dechema5 * Vol) / Stchema5)
                G5.set(Vchema5)
                Wvol1 -= Vchema5
                
                if Vchema5 > Vol:
                    G5.set("Error")
                    
            else:
                G5.set(0)
                    
        except ValueError:
            G5.set("Numerical value only")
            
        if Wvol1 > 0:
            Y1.set(Wvol1)
        if Wvol1 <= 0:
            Y1.set("Error")
            
        try:
            Stchema6 = float(Stchem6.get())
            Dechema6 = float(Dechem6.get())
            if Stchema6 > 0 and Dechema6 >0:
                Vchema6 = ((Dechema6 * Vol) / Stchema6)
                G6.set(Vchema6)
                Wvol1 -= Vchema6
                
                if Vchema6 > Vol:
                    G6.set("Error")
                    
            else:
                G6.set(0)
                    
        except ValueError:
            G6.set("Numerical value only")
            
        if Wvol1 > 0:
            Y1.set(Wvol1)
        if Wvol1 <= 0:
            Y1.set("Error")
    
    except ValueError:
        S1.set("Enter a value >0")





root = Tk()
root.title("Buffer Calculator")

mainframe = ttk.Frame(root, padding="5 5 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

NumReagent = StringVar()
Volume = StringVar()
G1 = StringVar()
G2 = StringVar()
G3 = StringVar()
G4 = StringVar()
G5 = StringVar()
G6 = StringVar()
Y1 = StringVar()
Nachem1 = StringVar()
Nachem1.set("eg. NaCl")
Stchem1 = StringVar()
Stchem1.set(0)
Dechem1 = StringVar()
Dechem1.set(0)
Nachem2 = StringVar()
Stchem2 = StringVar()
Stchem2.set(0)
Dechem2 = StringVar()
Dechem2.set(0)
Nachem3 = StringVar()
Stchem3 = StringVar()
Stchem3.set(0)
Dechem3 = StringVar()
Dechem3.set(0)
Nachem4 = StringVar()
Stchem4 = StringVar()
Stchem4.set(0)
Dechem4 = StringVar()
Dechem4.set(0)
Nachem5 = StringVar()
Stchem5 = StringVar()
Stchem5.set(0)
Dechem5 = StringVar()
Dechem5.set(0)
Nachem6 = StringVar()
Stchem6 = StringVar()
Stchem6.set(0)
Dechem6 = StringVar()
Dechem6.set(0)
S1 = StringVar()



Volume_entry = ttk.Entry(mainframe, width=7, textvariable=Volume)
Volume_entry.grid(column=3, row=1, sticky=(W, E))

Nachem1_entry = ttk.Entry(mainframe, width=5, textvariable=Nachem1)
Nachem1_entry.grid(column=2, row=3, sticky=(W, E))

Stchem1_entry = ttk.Entry(mainframe, width=5, textvariable=Stchem1)
Stchem1_entry.grid(column=3, row=3, sticky=(W, E))

Dechem1_entry = ttk.Entry(mainframe, width=5, textvariable=Dechem1)
Dechem1_entry.grid(column=4, row=3, sticky=(W, E))

Nachem2_entry = ttk.Entry(mainframe, width=5, textvariable=Nachem2)
Nachem2_entry.grid(column=2, row=4, sticky=(W, E))

Stchem2_entry = ttk.Entry(mainframe, width=5, textvariable=Stchem2)
Stchem2_entry.grid(column=3, row=4, sticky=(W, E))

Dechem2_entry = ttk.Entry(mainframe, width=5, textvariable=Dechem2)
Dechem2_entry.grid(column=4, row=4, sticky=(W, E))

Nachem3_entry = ttk.Entry(mainframe, width=5, textvariable=Nachem3)
Nachem3_entry.grid(column=2, row=5, sticky=(W, E))

Stchem3_entry = ttk.Entry(mainframe, width=5, textvariable=Stchem3)
Stchem3_entry.grid(column=3, row=5, sticky=(W, E))

Dechem3_entry = ttk.Entry(mainframe, width=5, textvariable=Dechem3)
Dechem3_entry.grid(column=4, row=5, sticky=(W, E))

Nachem4_entry = ttk.Entry(mainframe, width=5, textvariable=Nachem4)
Nachem4_entry.grid(column=2, row=6, sticky=(W, E))

Stchem4_entry = ttk.Entry(mainframe, width=5, textvariable=Stchem4)
Stchem4_entry.grid(column=3, row=6, sticky=(W, E))

Dechem4_entry = ttk.Entry(mainframe, width=5, textvariable=Dechem4)
Dechem4_entry.grid(column=4, row=6, sticky=(W, E))

Nachem5_entry = ttk.Entry(mainframe, width=5, textvariable=Nachem5)
Nachem5_entry.grid(column=2, row=7, sticky=(W, E))

Stchem5_entry = ttk.Entry(mainframe, width=5, textvariable=Stchem5)
Stchem5_entry.grid(column=3, row=7, sticky=(W, E))

Dechem5_entry = ttk.Entry(mainframe, width=5, textvariable=Dechem5)
Dechem5_entry.grid(column=4, row=7, sticky=(W, E))

Nachem6_entry = ttk.Entry(mainframe, width=5, textvariable=Nachem6)
Nachem6_entry.grid(column=2, row=8, sticky=(W, E))

Stchem6_entry = ttk.Entry(mainframe, width=5, textvariable=Stchem6)
Stchem6_entry.grid(column=3, row=8, sticky=(W, E))

Dechem6_entry = ttk.Entry(mainframe, width=5, textvariable=Dechem6)
Dechem6_entry.grid(column=4, row=8, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command= bufferC).grid(column=8, row=9, sticky=W)

ttk.Label(mainframe, text="Total Volume (mL)").grid(column=2, row=1, sticky=W)
ttk.Label(mainframe, text="Chemical Name").grid(column=2, row=2, sticky=W)
ttk.Label(mainframe, text="Stock \nConcentration (mM)").grid(column=3, row=2, sticky=W)
ttk.Label(mainframe, text="Desired \n Concentration (mM)").grid(column=4, row=2, sticky=W)
ttk.Label(mainframe, text="Reagent to add (mL)").grid(column=5, row=2, sticky=W)
ttk.Label(mainframe, text="Water to add (mL)").grid(column=4, row=9, sticky=W)
ttk.Label(mainframe, textvariable=G1, background = "lightblue").grid(column=5, row=3, sticky=(W, E))
ttk.Label(mainframe, textvariable=Y1, background = "lightyellow").grid(column=5, row=9, sticky=(W, E))
ttk.Label(mainframe, textvariable=G2, background = "lightblue").grid(column=5, row=4, sticky=(W, E))
ttk.Label(mainframe, textvariable=G3, background = "lightblue").grid(column=5, row=5, sticky=(W, E))
ttk.Label(mainframe, textvariable=G4, background = "lightblue").grid(column=5, row=6, sticky=(W, E))
ttk.Label(mainframe, textvariable=G5, background = "lightblue").grid(column=5, row=7, sticky=(W, E))
ttk.Label(mainframe, textvariable=G6, background = "lightblue").grid(column=5, row=8, sticky=(W, E))
ttk.Label(mainframe, textvariable=S1, foreground = "red").grid(column=4, row=1, sticky=(W, E))

for child in mainframe.winfo_children(): child.grid_configure(padx=4, pady=4)

Volume_entry.focus()
root.bind('<Return>', bufferC)

root.mainloop()
        
