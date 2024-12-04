class MakefileGenerator:
    def generate_makefile(self, source_files, output_dir):
        makefile_content = f"""
PYTHON_FILES = {' '.join(str(f) for f in source_files)}
OUTPUT_DIR = {output_dir}

all: $(PYTHON_FILES)
\t@mkdir -p $(OUTPUT_DIR)
\t@for file in $(PYTHON_FILES); do \
\t\tcompyler $$file -o $(OUTPUT_DIR); \
\tdone

clean:
\t@rm -rf $(OUTPUT_DIR)
"""
        with open("Makefile", "w") as f:
            f.write(makefile_content)
