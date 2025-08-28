import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from tkinter import filedialog

class settingsWindow(tk.Toplevel):
    """
    Opens a window showing the current settings (edge type, multilayer view and stats type),
        to allow user to change them.
    """    
    def __init__(self, root, app):
        super().__init__(root)
        self.root = root
        self.app = app
        self.title("Settings")
        self.geometry("400x300")
        
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        
        self.tabControl = ttk.Notebook(self)

        tab1 = ttk.Frame(self.tabControl)
        tab2 = ttk.Frame(self.tabControl)
        tab3 = ttk.Frame(self.tabControl)
        tab4 = ttk.Frame(self.tabControl)
        
        self.tabControl.add(tab1, text ='General')
        self.tabControl.add(tab2, text ='Graph Plot')
        self.tabControl.add(tab3, text ='Histogram')
        self.tabControl.add(tab4, text ='Animation')
        self.tabControl.pack(expand = 1, fill ="both")
        
        self.edge_type_var = tk.IntVar(value = 1) # variable for changing affinity/distance in settings window
        self.view_var = tk.IntVar(value = 1)      # variable for changing view from 3D to average in settings window
        self.histo_type_var = tk.IntVar(value = 1) # variable for side by side or stacked histogram
        self.loops_var = tk.IntVar(value = 1)     # variable for the removal of feedback loops in graph display

        edge_label = tk.Label(tab1, text="Edge type")
        edge_label.grid(row = 1, column = 1)
        dist_button = tk.Radiobutton(tab1, text="Distance", variable = self.edge_type_var, value = 2, command = self.switch_edge_type)
        dist_button.grid(row = 1, column = 2)    
        aff_button = tk.Radiobutton(tab1, text="Affinity", variable = self.edge_type_var, value = 1, command = self.switch_edge_type)
        aff_button.grid(row = 1, column = 3)
        # need to remove event listeners from radiobutton: they get triggered by hovering otherwise
        dist_button.bind('<Enter>', lambda e: None)
        dist_button.bind('<Leave>', lambda e: None)       
        aff_button.bind('<Enter>', lambda e: None)
        aff_button.bind('<Leave>', lambda e: None)
        
        multilayer_label = tk.Label(tab2, text="Multilayer display")
        multilayer_label.grid(row = 2, column = 1)
        avg_button = tk.Radiobutton(tab2, text="Average", variable = self.view_var, value = 2, command = self.switch_view_type)
        avg_button.grid(row = 2, column = 2)
        multilayer_button = tk.Radiobutton(tab2, text="3D", variable = self.view_var, value = 1, command = self.switch_view_type)
        multilayer_button.grid(row = 2, column = 3)
        # need to remove event listeners from radiobutton: they get triggered by hovering otherwise
        avg_button.bind('<Enter>', lambda e: None)
        avg_button.bind('<Leave>', lambda e: None)       
        multilayer_button.bind('<Enter>', lambda e: None)
        multilayer_button.bind('<Leave>', lambda e: None)
        
        multilayer_label = tk.Label(tab3, text="Histogram type")
        multilayer_label.grid(row = 1, column = 1)
        sbs_button = tk.Radiobutton(tab3, text="Side-by-side", variable = self.histo_type_var, value = 1, command = self.switch_histo_type)
        sbs_button.grid(row = 1, column = 2)
        stacked_button = tk.Radiobutton(tab3, text="Stacked", variable = self.histo_type_var, value = 2, command = self.switch_histo_type)
        stacked_button.grid(row = 1, column = 3)
        # need to remove event listeners from radiobutton: they get triggered by hovering otherwise
        sbs_button.bind('<Enter>', lambda e: None)
        sbs_button.bind('<Leave>', lambda e: None)       
        stacked_button.bind('<Enter>', lambda e: None)
        stacked_button.bind('<Leave>', lambda e: None)
        
        # necessary because of tkinter foul handling of radiobuttons. Values do not get set properly, events get triggered when they shouldn't...
        if self.app.edge_type == "distance":
            original_command = dist_button.cget('command')
            dist_button.config(command=lambda: None)
            dist_button.invoke()
            dist_button.config(command=original_command)

        if self.app.view_type == "avg":
            original_command = avg_button.cget('command')
            avg_button.config(command=lambda: None)
            avg_button.invoke()
            avg_button.config(command=original_command)
            
        if self.app.histo_type == "side-by-side":
            original_command = sbs_button.cget('command')
            sbs_button.config(command=lambda: None)
            sbs_button.invoke()
            sbs_button.config(command=original_command)

        show_legend_label = tk.Label(tab3, text="Show legend: ")
        show_legend_label.grid(row = 2, column = 1)
        show_legend_button = tk.Checkbutton(tab3, text="", command = self.show_legend_clicked)
        if self.app.show_histogram_legend:
            show_legend_button.select()
        show_legend_button.grid(row = 2, column = 2)
        
        fbloop_label = tk.Label(tab1, text="Remove feedback loops in plots: ")
        fbloop_label.grid(row = 4, column = 1)
        fb_loop_button = tk.Checkbutton(tab1, text="", variable = self.loops_var, onvalue = 1, offvalue = 0, command = self.loops_button_clicked)
        if self.loops_var.get() == 1:
            fb_loop_button.select()
        fb_loop_button.grid(row = 4, column = 2)
        
        scale_edge_label = tk.Label(tab1, text="Scale edge width: ")
        scale_edge_label.grid(row = 5, column = 1)
        scale_edge_button = tk.Checkbutton(tab1, text="", command = self.scale_edge_clicked)
        if self.app.scale_edge_width:
            scale_edge_button.select()
        scale_edge_button.grid(row = 5, column = 2)
        
        tk.Label(tab4, text="Time between frames (ms):").grid(row=1, column=1)
        self.animation_speed_var = tk.StringVar() 
        self.animation_speed_entry = tk.Entry(tab4, textvariable=self.animation_speed_var)
        self.animation_speed_entry.insert(0, self.app.animation_speed_var.get())
        self.animation_speed_entry.bind('<Return>', lambda event: self.on_enter_pressed(event))
        self.animation_speed_entry.grid(row=1, column=2)
        
        tk.Label(tab1, text="Edge thickness:").grid(row=6, column=1)
        self.edge_thickness_var = tk.StringVar() 
        self.edge_thickness_entry = tk.Entry(tab1, textvariable=self.edge_thickness_var)
        self.edge_thickness_entry.insert(0, self.app.edge_thickness_var.get())
        self.edge_thickness_entry.bind('<Return>', lambda event: self.on_enter_pressed(event))
        self.edge_thickness_entry.grid(row=6, column=2)
        
        tk.Label(tab1, text="Node thickness:").grid(row=7, column=1)
        self.node_thickness_var = tk.StringVar() 
        self.node_thickness_entry = tk.Entry(tab1, textvariable=self.node_thickness_var)
        self.node_thickness_entry.insert(0, self.app.node_thickness_var.get())
        self.node_thickness_entry.bind('<Return>', lambda event: self.on_enter_pressed(event))
        self.node_thickness_entry.grid(row=7, column=2)
        
        between_layer_label = tk.Label(tab2, text="Draw edges between layers: ")
        between_layer_label.grid(row = 8, column = 1)
        between_layer_button = tk.Checkbutton(tab2, text="", command = self.between_layer_clicked)
        if self.app.between_layer_edges:
            between_layer_button.select()
        between_layer_button.grid(row = 8, column = 2)
        
    def redraw(self):
        if self.app.display_type == "plot":
            self.app.plot_in_frame()
        elif self.app.display_type == "stats":
            self.app.stats_in_frame()
        elif self.app.display_type == "animation":
            self.app.animation_in_frame()

    def on_enter_pressed(self, event):
        edge_thickness_value = self.edge_thickness_entry.get()  
        node_thickness_value = self.node_thickness_entry.get() 
        animation_speed_value = self.animation_speed_entry.get()
        self.app.edge_thickness_var.set(edge_thickness_value)
        self.app.node_thickness_var.set(node_thickness_value)
        self.app.animation_speed_var.set(animation_speed_value)
        self.redraw()
        
    def switch_edge_type(self):
        if self.app.edge_type == "affinity":
            self.app.edge_type = "distance"
            self.redraw()
            return
        else:
            self.app.edge_type = "affinity"
            self.redraw()
            return

    def switch_view_type(self):
        if self.app.view_type == "3D":
            self.app.view_type = "avg"
            self.redraw()
            return
        else:
            self.app.view_type = "3D"
            self.redraw()
            return

    def switch_histo_type(self):
        if self.app.histo_type == "stacked":
            self.app.histo_type = "side-by-side"
            self.redraw()
            return
        else:
            self.app.histo_type = "stacked"
            self.redraw()
            return

    def loops_button_clicked(self):
        self.app.remove_loops = not self.app.remove_loops
        self.redraw()

    def scale_edge_clicked(self):
        self.app.scale_edge_width = not self.app.scale_edge_width
        self.redraw()

    def show_legend_clicked(self):
        self.app.show_histogram_legend = not self.app.show_histogram_legend
        self.redraw()

    def between_layer_clicked(self):
        self.app.between_layer_edges = not self.app.between_layer_edges
        self.redraw()
        
    def on_close(self):
        self.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    t = settingsWindow(root, None)
    root.mainloop()