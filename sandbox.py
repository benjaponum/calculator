import ui


def button_tapped(sender):
    sender.text = "Tapped!"

view = ui.View()
view.background_color = 'white'
button = ui.Button(title='Button')
button.font = ('<system>', 40)
button.size_to_fit()
button.center = (view.width*0.5, view.height*0.5) 
button.flex = 'LRTB'
button.action = button_tapped
view.add_subview(button)
view.present()
