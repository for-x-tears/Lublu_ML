from rich import print as rprint
rprint("[bold blue] Privet moi drug")
rprint("Segodny u nas pokaz filma [bold red] Chelovek pauk")
decision = input("poidesh so mnoy? [Da/Net]:")

print(decision)
if decision.lower == "da":
    rprint('Slushai, a tebe esti 18')
    
elif decision.lower == "net":
    print("Хороший ответ")
print ('fhergr')