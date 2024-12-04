class NinjaBuildGenerator:
    def generate_build_file(self, source_files):
        ninja_template = """
rule compile_python
  command = compyler $in -o $out
  description = Compiling $in to $out
"""
        with open("build.ninja", "w") as f:
            f.write(ninja_template)
            for source in source_files:
                f.write(f"\nbuild {source}.exe: compile_python {source}")


