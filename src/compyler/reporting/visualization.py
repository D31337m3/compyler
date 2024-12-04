class MetricsVisualizer:
    def __init__(self):
        self.plot_types = {
            'line': self._create_line_plot,
            'bar': self._create_bar_plot,
            'heatmap': self._create_heatmap
        }
        
    def create_visualization(self, data, plot_type='line'):
        if plot_type in self.plot_types:
            figure = self.plot_types[plot_type](data)
            return self._save_plot(figure)
