import pickle
import PySimpleGUI as sg
import pandas as pd

with open("modelo_final.pkl", "rb") as file:
    modelo = pickle.load(file)

sg.theme("DarkBlue16")

layout=[[sg.Text("Classe:"), sg.Input("", key="cl")],
        [sg.Text("Genero:"), sg.Input("", key="sex")],
        [sg.Text("Idade:"), sg.Input("", key="id")],
        [sg.Text("nº Conjuge/nº irmaos:"), sg.Input("", key="conj")],
        [sg.Text("nº filhos/nº Pais:"), sg.Input("", key="filhos")],
        [sg.Text("Preço"), sg.Input("", key="fare")],
        [sg.Button("Prever"), sg.Button("Sair")],
        #[sg.Combo(["", "Masculino", "Feminino"], key="gen")]
        ]

janela = sg.Window("Modelo de previsão Titanic", layout)

while True:

    eventos, valores = janela.read()
    if eventos=="Prever":

        ler_valores={}
        ler_valores["Pclass"]=[int(valores["cl"])]
        ler_valores["Sex"]=[int(valores["sex"])]
        ler_valores["Age"]=[float(valores["id"])]
        ler_valores["SibSp"]=[int(valores["conj"])]
        ler_valores["Parch"]=[int(valores["filhos"])]
        ler_valores["Fare"]=[float(valores["fare"])]

        data=pd.DataFrame(ler_valores)

        surv=modelo.predict(data)
        prob=modelo.predict_proba(data)
        if surv==0:
            sg.Popup(" Não Consegues sobreviver ...")
            aux=round(prob[0][0]*100, 1)
            sg.Popup(f" Com probabilidade de {aux}%")
        if surv==1:
            sg.Popup(" Consegues sobreviver (Parabens)...")
            aux=round(prob[0][1]*100, 1)
            sg.Popup(f" Com probabilidade de {aux}%")
        print(prob)

    if eventos==sg.WIN_CLOSED or eventos=="Sair":
        break
    
    print(eventos, valores)

janela.close()

