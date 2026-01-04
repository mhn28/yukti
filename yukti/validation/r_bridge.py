import subprocess
import shutil

def r_available():
    return shutil.which("Rscript") is not None

def run_r(script_path, args):
    if not r_available():
        raise RuntimeError("Rscript not found on PATH")
    cmd = ["Rscript", script_path] + args
    return subprocess.check_output(cmd, text=True).strip()
