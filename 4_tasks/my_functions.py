from rich import print as rprint

def greet(name):
    rprint(f"[italic red]Hello {name}[/italic red]")

def change_name(name):
    new_name = ""
    for i in range(len(name)):
        if i % 2 == 1:
            new_name += name[i].upper()
        else:
            new_name += name[i]
    return new_name

if __name__ == '__main__':
    greet("Deva")
    rprint(change_name("deva"))