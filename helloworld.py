#!/usr/bin/env python

# example helloworld.py

import pygtk
pygtk.require('2.0')
import gtk

class HelloWorld:

    # This is a callback function. The data arguments are ignored
    # in this example. More on callbacks below.
    def hello(self, widget, data=None):
        print "Hello World"

    def __init__(self):
        # create a new window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
    
        self.window.connect("delete_event", lambda x: gtk.main_quit())
        self.window.connect("destroy", lambda x: gtk.main_quit())
    
        # Sets the border width of the window.
        self.window.set_border_width(10)
    
	button_x_plus = gtk.Button("X+")
	button_x_plus.set_size_request(30,30)
	button_x_minus = gtk.Button("X-")
	button_x_minus.set_size_request(30,30)
	button_y_plus = gtk.Button("Y+")
	button_y_plus.set_size_request(30,30)
	button_y_minus = gtk.Button("Y-")
	button_y_minus.set_size_request(30,30)
	button_z_plus = gtk.Button("Z+")
	button_z_plus.set_size_request(30,30)
	button_z_minus = gtk.Button("Z-")
	button_z_minus.set_size_request(30,30)

	button_home = gtk.Button("HOME")
	button_origin = gtk.Button("Origin")
	button_origin_x = gtk.Button("X=0")
	button_origin_y = gtk.Button("Y=0")
	button_origin_z = gtk.Button("Z=0")
	button_hold = gtk.Button("FEED HOLD")
	button_resume = gtk.Button("Resume")

	table = gtk.Table(rows=3, columns=5, homogeneous=True)
	table.set_row_spacings(5)
	table.set_col_spacings(5)
	table.attach(button_z_plus, left_attach=0, right_attach=1, top_attach=0,bottom_attach=1)
	table.attach(button_z_minus, left_attach=0, right_attach=1, top_attach=2,bottom_attach=3)

	table.attach(button_x_plus, left_attach=3, right_attach=4, top_attach=0,bottom_attach=1)
	table.attach(button_x_minus, left_attach=3, right_attach=4, top_attach=2,bottom_attach=3)

	table.attach(button_y_minus, left_attach=2,right_attach=3, top_attach=1, bottom_attach=2)
	table.attach(button_y_plus, left_attach=4,right_attach=5, top_attach=1, bottom_attach=2)
	
	homing_hbox = gtk.HBox()
	homing_vbox = gtk.VBox()
	homing_vbox.pack_start(homing_hbox, False, False)
	homing_hbox.pack_start(button_home, False, False)
	homing_hbox.pack_start(button_origin, False, False)

	homing_frame = gtk.Frame("Homing Controls")
	homing_frame.add(homing_vbox)

	o_hb = gtk.HBox()
	o_vb = gtk.VBox()
	o_vb.pack_start(o_hb, False, False)
	o_hb.pack_start(button_origin_x, False, False)
	o_hb.pack_start(button_origin_y, False, False)
	o_hb.pack_start(button_origin_z, False, False)

	origin_frame = gtk.Frame("Origin-Setting")
	origin_frame.add(o_vb)

	t_hbox = gtk.HBox()
	t_vbox = gtk.VBox()
	t_vbox.pack_start(t_hbox)
	t_hbox.pack_start(table)
	motion_frame = gtk.Frame("Motion Controls")
	t_vbox.set_size_request(160, 120)
	motion_frame.add(t_vbox)

	window_table = gtk.Table(rows=1, columns=3, homogeneous=False)
	window_table.attach(motion_frame, left_attach=0, right_attach=1, top_attach=0, bottom_attach=1)	
	window_table.attach(homing_frame, left_attach=1, right_attach=2, top_attach=0, bottom_attach=1)	
	window_table.attach(origin_frame, left_attach=2, right_attach=3, top_attach=0, bottom_attach=1)	

	master_frame = gtk.Frame("Pete Pendant")
	master_frame.add(window_table)





	self.window.add(master_frame)
    
	self.window.show_all()

    def main(self):
        # All PyGTK applications must have a gtk.main(). Control ends here
        # and waits for an event to occur (like a key press or mouse event).
        gtk.main()

# If the program is run directly or passed as an argument to the python
# interpreter then create a HelloWorld instance and show it
if __name__ == "__main__":
    hello = HelloWorld()
    hello.main()
