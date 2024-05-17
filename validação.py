empresas = {"Enerbras",
            "Itambe", 
            "C.A.W", 
            "RasLog", 
            "Incepa"}

empresa = input(("Digite a empresa desejada:"))
if empresa in empresas:
    print ("empresa aberta")
else:
    print("empresa fechada")