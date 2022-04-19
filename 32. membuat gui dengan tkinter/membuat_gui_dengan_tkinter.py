import tkinter

main_window = tkinter.Tk()
def event_tekan():
    label2 = tkinter.Label(main_window, text = 'aku di tekan ^_^')
    label.pack()

label = tkinter.Label(main_window,text = 'halo, saya adalah,\n Gui sederhana \nmenggunakanpython')
tombol = tkinter.Button(main_window,text = 'tekan akuh',command = event_tekan())

label.pack()
tombol.pack()
main_window.mainloop()