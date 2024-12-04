class BytecodeOptimizer:
    def __init__(self):
        self.peephole_optimizations = {
            'constant_folding': self._fold_constants,
            'dead_code_elimination': self._eliminate_dead_code,
            'instruction_combining': self._combine_instructions
        }
        
    def optimize_bytecode(self, code_object):
        for optimization in self.peephole_optimizations.values():
            code_object = optimization(code_object)
        return code_object
