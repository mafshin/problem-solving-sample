from nicegui import ui
import P003

Number_Input1 = ui.input('first year')
Number_Input2 = ui.input('second year')

ui.button('OK' , on_click=lambda: Clik())

ui.run()

def Clik():
    number_1 = int(Number_Input1.value)
    number_2 = int(Number_Input2.value)

    result = P003.Year(number_1 , number_2)

    ui.notify(result)
    ui.label(result)