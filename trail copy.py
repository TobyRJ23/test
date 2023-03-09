import requests 
from rich.console import Console

console = Console()

data = requests.get("https://www.anapioficeandfire.com/api/characters/1").json()

console.print(data)