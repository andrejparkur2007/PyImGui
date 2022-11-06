import dearpygui.dearpygui as dpg

dpg.create_context()

with dpg.window(label="Choto", width=600, height=100, pos=(0, 0)):
    dpg.add_text("andrej")
    a = dpg.add_input_text(label="string", default_value="ID")
    #dpg.add_slider_float(label="float", default_value=0.273, max_value=1)
    dpg.add_button(label="Save Config")
    #dpg.draw_line((0, 10), (100, 100), color=(255, 0, 0, 255), thickness=1)
    pass


with dpg.window(label="Global", width=600, height=100, pos=(0, 100)):
    dpg.add_text("Main")
    # dpg.add_input_text(label="string", default_value="Skin ID")
    dpg.add_button(label="Save Config", callback=callback)
    pass

#kripishi    
print(dpg.get_item_children(dpg.last_root()))


print(dpg.get_item_children(dpg.last_root(), 1))


print(dpg.get_item_slot(dpg.last_item()))

dpg.create_viewport(title='Krip', width=600, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()

