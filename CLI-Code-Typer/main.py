# Importing the Typer module
import typer  

# Creating an instance of the Typer class
app = typer.Typer()  

# Decorator for defining a func command
@app.command()  
def func():
    print("Welcome to our organization")
    
# Decorator for defining another command called hello with string parameter
@app.command()  
def hello(organization: str):
    print(f"Hello {organization}")

# Run the script
if __name__ == "__main__":
    app()  
