from nicegui import ui

with ui.scene().classes('w-full h-64') as scene:
    scene.sphere(1).material('gray').move(x=0, y=0, z=1.2)
    scene.box(1.5 , 1.5, 1.5).material('gray').move(x=5, y=5, z=1)

ui.label('''from nicegui import ui 
 
with ui.scene().classes('w-full h-64') as scene: 
    scene.sphere(1).material('gray').move(x=0, y=0, z=1) 
    scene.box().material('gray').move(x=4, y=4, z=1) 
 
    ui.label() 
 
ui.run() ''')

ui.run()