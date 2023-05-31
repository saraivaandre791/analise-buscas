import mysql.connector #importando conector para banco de dados
from flask import Flask,make_response, render_template, redirect, url_for #importando o flask
from datetime import  datetime
import pandas as pd # importando pandas para criar um DataFrame
import json 
import plotly # importando plotly para criar graficos
import plotly.express as px # para criar graficos
from waitress import serve



mydb = mysql.connector.connect( # criando variavel q vai receber o connector com o banco de dados
    host="vps.arenavidros.com.br",
    user="devandre",
    password="Arena@428#156481klqi=",
    database="tigenios"
)
app = Flask(__name__) # iniciando flask

# tabela 'produtos não encontrados' + grafico ///
@app.route('/', methods=['GET'])  # criando rota
def get_pesquisas(): # criando função pegar pesquisas

    mycursor = mydb.cursor()#mycursor recebe conector com MYSQL para executar comandos no banco de dados
    mycursor.execute("SELECT * FROM TAB_NAO_PRODUTO_LOG WHERE CARRO <> '' and TAB_NAO_PRODUTO_LOG.DATA BETWEEN DATE_ADD(CURRENT_DATE(), INTERVAL -30 DAY) AND CURRENT_DATE()")#Executando comando SQL com cursor
    minhas_pesquisas = mycursor.fetchall()#variavel recebe todos os dados que o cursor trouxe do banco de dados

    pesquisas = []#criando lista chamada PESQUISAS
    for pesquisa in minhas_pesquisas:#para cada item na variavel MINHAS PESQUISAS
        pesquisas.append(# a lista PESQUISAS vai receber os dados abaixo
            {
            'ID':pesquisa[0],
            'DATA':pesquisa[1].strftime("%d/%m/%Y %H:%M:%S"),#formatando o modo q a data deve ser exibida
            'IP':pesquisa[2],
            'MARCA':pesquisa[3],
            'CARRO':pesquisa[4],
            'PESQUISA':pesquisa[5],
            'Buscas': 1
            }
        )

    dataFrame  = pd.DataFrame(pesquisas) # colocando os dados que estão na lista PESQUISAS dentro de um DATAFRAME

    fig = px.pie(dataFrame, values="Buscas", names="PESQUISA")# definindo o tipo de grafico e o modo como sera tratado os dados

    graphJSONs1 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)# criando grafico

    

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM TAB_NAO_PRODUTO_LOG WHERE CARRO <> '' and TAB_NAO_PRODUTO_LOG.DATA BETWEEN DATE_ADD(CURRENT_DATE(), INTERVAL -30 DAY) AND CURRENT_DATE()")
    meus_carros = mycursor.fetchall()

    carros = []
    for carro in meus_carros:
        carros.append(
            {
            'ID':carro[0],
            'DATA':carro[1].strftime("%d/%m/%Y %H:%M:%S"), 
            'IP':carro[2],
            'MARCA':carro[3],
            'CARRO':carro[4],
            'PESQUISA':carro[5],
            'Buscas': 1
             
            
            
            
            }
        ) 
        
    df3  = pd.DataFrame(carros)#colocando carros dentro de um DataFrame

    fig = px.bar(df3, x="CARRO", y="Buscas", color_discrete_sequence=['red'])# Definindo como o grafico vai exibir os dados
    
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)# Criando grafico



    return make_response(
        render_template('carros.html', dados=pesquisas, graphJSON1=graphJSONs1, graphJSON=graphJSON)# comando para ler o template
    )




# Tabela de orcamentos   /////////////////////////////////////////////////////////////////////
@app.route('/orcamentos', methods=['GET'])
def get_orçamentos():

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM TAB_NAO_PRODUTO   WHERE TELEFONE <> '' ORDER BY DATA DESC")
    meus_orcamentos = mycursor.fetchall()

    orcamentos = []
    for orcamento in meus_orcamentos:
        orcamentos.append(
            {
            'ID':orcamento[0],
            'NOME':orcamento[1],
            'TELEFONE':orcamento[2],
            'PESQUISA':orcamento[3],
            'MSG':orcamento[4],
            'MARCA':orcamento[5],
            'CARRO':orcamento[6],
            'IP':orcamento[7],
            'DATA':orcamento[8].strftime("%d/%m/%Y %H:%M:%S"),
            
            'BUSCAS':1
        
           
            }
        )
   
    dataframe2 = pd.DataFrame(orcamentos)


    fig= px.pie(dataframe2, values="BUSCAS", names="PESQUISA")

    graphJSON= json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)


    return make_response(
       render_template('orcamentos.html', infos=orcamentos, graphJSON=graphJSON)
    )
    
# procura por borrachas
@app.route('/borrachas', methods=['GET'])  # criando rota
def get_borrachas(): # criando função pegar pesquisas

   
    

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM TAB_NAO_PRODUTO_LOG WHERE PESQUISA = 'BORRACHAS' and TAB_NAO_PRODUTO_LOG.DATA BETWEEN DATE_ADD(CURRENT_DATE(), INTERVAL -30 DAY) AND CURRENT_DATE()")
    minhas_borrachas= mycursor.fetchall()

    borrachas = []
    for borracha in minhas_borrachas :
        borrachas.append(
            {
            'ID':borracha[0],
            'DATA':borracha[1].strftime("%d/%m/%Y %H:%M:%S"), 
            'IP':borracha[2],
            'MARCA':borracha[3],
            'CARRO':borracha[4],
            'PESQUISA':borracha[5],
            'Buscas': 1
             
            
            
            
            }
        ) 
        
    df4  = pd.DataFrame(borrachas)#colocando carros dentro de um DataFrame

    fig = px.bar(df4, x="CARRO", y="Buscas", color_discrete_sequence=['black'])# Definindo como o grafico vai exibir os dados
    
    barra= json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)# Criando grafico



    return make_response(
        render_template('borrachas.html', dados=borrachas, graphJSON=barra)# comando para ler o template
    )


  

  # procura por vidros para teto solar
  
#procura por vidros para teto solar
@app.route('/tetosolar', methods=['GET'])  # criando rota
def get_tetosolar(): # criando função pegar pesquisas

    

    

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM TAB_NAO_PRODUTO_LOG WHERE PESQUISA = 'Vidros Para Teto Solar' and TAB_NAO_PRODUTO_LOG.DATA BETWEEN DATE_ADD(CURRENT_DATE(), INTERVAL -30 DAY) AND CURRENT_DATE()")
    meus_tetosolar= mycursor.fetchall()

    tetosolar = []
    for teto in meus_tetosolar:
        tetosolar.append(
            {
            'ID':teto[0],
            'DATA':teto[1].strftime("%d/%m/%Y %H:%M:%S"), 
            'IP':teto[2],
            'MARCA':teto[3],
            'CARRO':teto[4],
            'PESQUISA':teto[5],
            'Buscas': 1
             
            
            
            
            }
        ) 
        
    df4  = pd.DataFrame(tetosolar)#colocando carros dentro de um DataFrame

    fig = px.bar(df4, x="CARRO", y="Buscas", color_discrete_sequence=['blue'])# Definindo como o grafico vai exibir os dados
    
    barra= json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)# Criando grafico



    return make_response(
        render_template('tetosolar.html', dados=tetosolar, graphJSON=barra)# comando para ler o template
    )

@app.route('/laterais', methods=['GET'])
def get_vidrolateral():

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM TAB_NAO_PRODUTO_LOG WHERE PESQUISA = 'Vidros das Laterais' and TAB_NAO_PRODUTO_LOG.DATA BETWEEN DATE_ADD(CURRENT_DATE(), INTERVAL -30 DAY) AND CURRENT_DATE()")
    minhas_pt= mycursor.fetchall()

    portas = []
    for porta in minhas_pt:
        portas.append(
            {
            'ID':porta[0],
            'DATA':porta[1].strftime("%d/%m/%Y %H:%M:%S"), 
            'IP':porta[2],
            'MARCA':porta[3],
            'CARRO':porta[4],
            'PESQUISA':porta[5],
            'Buscas': 1
             
            
            
            
            }
        ) 
        
    df6  = pd.DataFrame(portas)#colocando carros dentro de um DataFrame

    fig = px.bar(df6, x="CARRO", y="Buscas", color_discrete_sequence=['red'])# Definindo como o grafico vai exibir os dados
    
    barra= json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)# Criando grafico



    return make_response(
        render_template('laterais.html', dados=portas, graphJSON=barra)# comando para ler o template
    )

    
@app.route('/vidropb',methods=['GET'])
def get_vidropb():

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM TAB_NAO_PRODUTO_LOG WHERE PESQUISA = 'Vidros Para-Brisa' and TAB_NAO_PRODUTO_LOG.DATA BETWEEN DATE_ADD(CURRENT_DATE(), INTERVAL -30 DAY) AND CURRENT_DATE()")
    meus_pb= mycursor.fetchall()

    parabrisas = []
    for pb in meus_pb:
        parabrisas.append(
            {
            'ID':pb[0],
            'DATA':pb[1].strftime("%d/%m/%Y %H:%M:%S"), 
            'IP':pb[2],
            'MARCA':pb[3],
            'CARRO':pb[4],
            'PESQUISA':pb[5],
            'Buscas': 1
             
            
            
            
            }
        ) 
        
    df7  = pd.DataFrame(parabrisas)#colocando carros dentro de um DataFrame

    fig = px.bar(df7, x="CARRO", y="Buscas", color_discrete_sequence=['blue'])# Definindo como o grafico vai exibir os dados
    
    barra= json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)# Criando grafico



    return make_response(
        render_template('PB.html', dados=parabrisas, graphJSON=barra)# comando para ler o template
    )


@app.route('/vidrovg', methods=['GET'])
def get_vidrovg():
    mycursor=mydb.cursor()
    mycursor.execute("SELECT * FROM TAB_NAO_PRODUTO_LOG WHERE PESQUISA = 'Vidros Traseiros Vigia' and TAB_NAO_PRODUTO_LOG.DATA BETWEEN DATE_ADD(CURRENT_DATE(), INTERVAL -30 DAY) AND CURRENT_DATE()")
    meus_vg = mycursor.fetchall()

    vigias=[]
    for vigia in meus_vg:
        vigias.append(
            {
            'ID':vigia [0],
            'DATA':vigia [1].strftime("%d/%m/%Y %H:%M:%S"), 
            'IP':vigia [2],
            'MARCA':vigia [3],
            'CARRO':vigia [4],
            'PESQUISA':vigia [5],
            'Buscas': 1
            }
        )
        
    df8 = pd.DataFrame(vigias)
    fig = px.bar(df8, x='CARRO', y='Buscas', color_discrete_sequence=['red'])
    barra=json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return make_response(
        render_template('vg.html', dados=vigias, graphJSON=barra)
    )

#pesquisas por periodo
@app.route('/periodo', methods=['GET'])
def get_periodo():
    mycursor=mydb.cursor()
    mycursor.execute("SELECT monthname(DATA) AS MES, COUNT(*) AS BUSCAS FROM TAB_NAO_PRODUTO_LOG GROUP BY MES")
    meus_periodos=mycursor.fetchall()
    periodos=[]
    for periodo in meus_periodos:
        periodos.append(
            {
            'MES':periodo[0],
            'BUSCAS':periodo[1]

            }
        )

    df9=pd.DataFrame(periodos)
    fig = px.bar(df9, x='MES', y='BUSCAS', color_discrete_sequence=['blue'])
    barra=json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    return make_response(
        render_template('periodo.html', dados=periodos, graphJSON=barra)
    )

if __name__=="__main__":
    app.run(debug=True) # esse comando faz com q a pagina atualize automaticamente a cada auteração