import pytest
import tempfile
import shutil

@pytest.fixture(scope="function")
def temp_dir():
    dir_path = tempfile.mkdtemp()
    yield dir_path
    shutil.rmtree(dir_path)

@pytest.fixture(scope="session")
def sample_script(temp_dir):
    script_path = Path(temp_dir) / "sample.py"
    with open(script_path, "w") as f:
        f.write("print('Test Script')")
    return script_path
