from tkinter import *
from tkinter import scrolledtext
#import prolog_connection as prolog_connection




def openwindow(prolog):
    window = Tk()
    window.title("Consulta de prolog")

    fatherlabel = Label(window, text="¿Qué plato puedo preparar con el ingrediente...?")
    fatherlabel.grid(column=0, row=0)
    firstquestiontext = Entry(window, width=20)
    firstquestiontext.grid(column=1, row=0)

    sonlabel = Label(window, text="¿Cuáles platos se pueden preparar si tengo 3 ingredientes específicos?")
    sonlabel.grid(column=2, row=0)
    secondquestion1 = Entry(window, width=20)
    secondquestion1.grid(column=3, row=0)
    secondquestion2 = Entry(window, width=20)
    secondquestion2.grid(column=3, row=1)
    secondquestion3 = Entry(window, width=20)
    secondquestion3.grid(column=3, row=2)

    thirdquestionlabel = Label(window, text="¿Cuáles platos implican usar la batidora (ej.: Batir la masa) como procedimiento?")
    thirdquestionlabel.grid(column=0, row=1)
    thirdquestiontext = Entry(window, width=20)
    thirdquestiontext.grid(column=1, row=1)

    fourthquestionlabel = Label(window, text="Si no tengo batidora, ¿cuáles platos puedo hacer?")
    fourthquestionlabel.grid(column=0, row=2)
    fourthquestiontext = Entry(window, width=20)
    fourthquestiontext.grid(column=1, row=2)

    fifthquestionlabel = Label(window, text="Si no tengo mantequilla, ¿qué plato puedo preparar?")
    fifthquestionlabel.grid(column=0, row=3)
    fifthquestiontext = Entry(window, width=20)
    fifthquestiontext.grid(column=1, row=3)

    sixthlabel = Label(window, text="Si no tengo huevos ni tengo batidora, ¿qué platos puedo preparar?")
    sixthlabel.grid(column=2, row=4)
    sixthtext = Entry(window, width=20)
    sixthtext.grid(column=3, row=4)
    sixthquestion2 = Entry(window, width=20)
    sixthquestion2.grid(column=3, row=5)


     

    def save():
        valorfinal = list(prolog.query("buscar_ingrediente(%s ,Y)" % firstquestiontext.get().lower()))
        for valor in valorfinal:
            firstquestionlist.insert(
                INSERT, "1- " , firstquestiontext.get(), "==>", valor["Y"])

        valorfinalQ2 = list(prolog.query("ingredientes_especificos(%s, %s, %s ,Y)" % (secondquestion1.get().lower(), secondquestion2.get().lower(), secondquestion3.get().lower())))
        for valorQ2 in valorfinalQ2:
            firstquestionlist.insert(
                INSERT, "2- ", secondquestion1.get(), secondquestion2.get(), secondquestion3.get(), "==>", valorQ2["Y"])

        valorfinalQ3 = list(prolog.query("batir_la_masa(Plato, %s)" % thirdquestiontext.get().lower()))

        for valorQ3 in valorfinalQ3:
            firstquestionlist.insert(
                INSERT, "3- ", valorQ3["Plato"])

        valorfinalQ4 = list(prolog.query("noIngrediente(%s, Plato)" % fourthquestiontext.get().lower()))

        for batidora in valorfinalQ4:
            firstquestionlist.insert(
                INSERT, "4- ", batidora["Plato"])

        valorfinalQ5 = list(prolog.query("noIngrediente(%s, Plato)" % fifthquestiontext.get().lower()))

        for mantequilla in valorfinalQ5:
             firstquestionlist.insert(
                INSERT, "5- ", mantequilla["Plato"])

        valorfinalQ6 = list(prolog.query("noIngredientes(%s,%s, Plato)" % (sixthtext.get().lower(), sixthquestion2.get().lower())))

        for huevo_nor_batidora in valorfinalQ6:
            firstquestionlist.insert(
                INSERT, "6- ", huevo_nor_batidora["Plato"])


    btn = Button(window, text="Guardar", command=save)
    btn.grid(column=6, row=0)


    firstquestionlist = scrolledtext.ScrolledText(window, width=40, height=10)
    firstquestionlist.grid(column=2, row=7)

    window.geometry('1368x768')
    window.mainloop()

#prolog = prolog_connection.startprolog()
openwindow("")