import ui

view = ui.View()
view.background_color = 'white'
button = ui.Button(title='Button')
button.font = ('<system>', 40)
button.size_to_fit()
button.center = (view.width*0.5, view.height*0.5) 
button.flex = 'LRTB'
view.add_subview(button)
view.present()
