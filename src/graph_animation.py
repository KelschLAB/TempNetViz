import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import igraph as ig
from matplotlib.animation import FuncAnimation
import numpy as np
import matplotlib as mpl


class GraphAnimator:
    def __init__(self, graphs, layout, styles, ax = None):
        self.graphs = graphs
        self.layout = layout
        self.styles = styles # store all the layout information, node sizes, edges width etc...
        self.is_playing = False
        self.animation = None
        self.ax = ax
        if self.ax is None:
            self.fig, self.ax = plt.subplots(figsize=(12, 9))
        else:
            self.fig = self.ax.figure
        self.precompute_plots()
        self.setup_ui()
        
    def setup_ui(self):
        """Set up the matplotlib figure and widgets"""
        plt.ion()
        self.ax.axis('off')
        self.fig.subplots_adjust(bottom=0.3)
        self.ax_slider = plt.axes([0.25, 0.2, 0.65, 0.03])
        self.ax_play = plt.axes([0.7, 0.05, 0.1, 0.04])
        self.ax_pause = plt.axes([0.81, 0.05, 0.1, 0.04])
        self.slider = Slider(self.ax_slider, 'Frame', 0, len(self.graphs)-1, valinit=0, valstep=1)
        self.play_button = Button(self.ax_play, 'Play')
        self.pause_button = Button(self.ax_pause, 'Pause')
        self.slider.on_changed(self.update_slider)
        self.fig.canvas.mpl_connect('button_press_event', self._on_click)
        self.play_button.on_clicked(self.play_animation)
        self.pause_button.on_clicked(self.pause_animation)
        self.img_obj = self.ax.imshow(self.frame_images[0])
        
    def precompute_plots(self):
        plt.ioff()
        self.frame_images = []
        for idx, g in enumerate(self.graphs):
            fig_tmp, ax_tmp = plt.subplots()
            ig.plot(g, target=ax_tmp, layout = self.layout.coords, **self.styles[idx])
            ax_tmp.axis('off')
            fig_tmp.canvas.draw()
            buf = fig_tmp.canvas.buffer_rgba()  # memoryview
            img = np.asarray(buf)  # Convert to NumPy array (H x W x 4)
            self.frame_images.append(img)
            plt.close(fig_tmp)
            
    def _on_click(self, event):
        if event.inaxes == self.slider.ax:
            if self.is_playing and self.animation and getattr(self.animation, "event_source", None):
                self.animation.event_source.stop()
            self.is_playing = False
           
    def update_plot(self, frame_idx):
        """Update the plot with the graph at the given frame index"""
        self.img_obj.set_data(self.frame_images[frame_idx])
        self.ax.set_title(f'Frame {frame_idx + 1}/{len(self.graphs)}')
        self.fig.canvas.draw_idle()
    
    def update_slider(self, val):
        """Handle slider changes"""
        if not self.is_playing:
            self.update_plot(int(val))
    
    def play_animation(self, event):
        """Start animation playback"""
        if self.is_playing: return
        self.is_playing = True

        def animate(frame):
            self.slider.set_val(frame)
            self.update_plot(frame)
            return [self.img_obj]

        self.animation = FuncAnimation(
            self.fig, animate, frames=len(self.frame_images),
            interval=200, blit=True, repeat=False
        )
    
    def pause_animation(self, event):
        """Pause animation playback"""
        if self.is_playing and self.animation and getattr(self.animation, "event_source", None):
            self.animation.event_source.stop()
            self.is_playing = False
    

 