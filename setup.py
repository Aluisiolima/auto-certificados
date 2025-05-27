from cx_Freeze import setup, Executable

setup(
    name="auto_certificacao",
    version="1.0",
    description="gerador de certificados",
    executables=[Executable("main.py")], 
)