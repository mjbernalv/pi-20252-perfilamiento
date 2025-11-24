import subprocess
import sys
import os

def main():
    path = os.path.dirname(os.path.abspath(__file__))
    subprocess.run([sys.executable, "-m", "streamlit", "run", f"{path}/🚀_Inicio.py"], check = True)

if __name__ == "__main__":
    main()