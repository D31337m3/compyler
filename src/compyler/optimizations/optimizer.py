class CodeOptimizer:
    def __init__(self, optimization_level=1):
        self.optimization_level = optimization_level
        self.optimizations = {
            1: self._basic_optimizations,
            2: self._advanced_optimizations,
            3: self._aggressive_optimizations
        }
        
    def optimize(self, bytecode):
        optimization_func = self.optimizations.get(
            self.optimization_level, 
            self._basic_optimizations
        )
        return optimization_func(bytecode)
