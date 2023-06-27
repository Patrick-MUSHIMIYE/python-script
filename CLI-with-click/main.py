# import the required modules
import click
from datetime import datetime
from colorama import Fore

# Define a Click group 
@click.group()  
def parentCLI():
    pass

@click.command()
@click.option("--name", type=str, prompt="Enter your name")  # Define an option for the name
@click.option("--age", type=int, prompt="Enter your Age")  # Define an option for the age
def person(name, age):
    click.echo(f"Hello {name}")  # Print a greeting with the provided name
    if age <= 18:
        click.echo(Fore.RED + "Your age is under 18")  # Print a message if age is under 18
    else:
        click.echo(Fore.BLUE + "You're an adult")  # Print a message if age is 18 or above
        

@click.command() # decorator
@click.option("--current_years", type=int, default=datetime.now().year)  # Define an option for current years
@click.option("--age", type=int, prompt="Enter your Age")  # Define an option for the age
def hundred_years(current_years, age):
    result = current_years + (100 - age)  # Calculate the year when the person will turn 100
    click.echo(Fore.GREEN + f"You will turn hundred years in this year: {result}")  # Print the result

@click.command()
@click.option("--favorite", type=click.Choice(["Croissant", "burger", "pizza"]), help="Favorite food")  # Define an option for the favorite food
def fav_food(favorite):
    if favorite is None:
        click.echo("You didn't pick your favorite food in the list")  # Print a message if no favorite food is selected
    else:
        click.echo(f"Your favorite food is {favorite}")  # Print the selected favorite food

#add the (person, hundred_years, fav_food) command to the parentCLI group
parentCLI.add_command(person)  
parentCLI.add_command(hundred_years) 
parentCLI.add_command(fav_food)

 
# Run the script
if __name__ == "__main__":
    parentCLI()  
