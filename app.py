from dash import Dash, html, dcc, dash_table
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_csv('csv/data.csv')
df.drop(columns=['Unnamed: 2','Unnamed: 7','Title'], inplace=True)


# Grafico de Barras: Consolas
def grafico1():
    top_consolas = df['Platform'].value_counts()
    fig = px.bar(y=top_consolas.values, x=top_consolas.index, title='Top Consolas mas utilizadas', text=top_consolas.values,
            labels={'x': 'Consola', 'y': 'Número de juegos'})
    return fig

fig1 = grafico1()


# Garfico de Torta: Consolas
def grafico1_2():
    top_consolas = df['Platform'].value_counts()
    fig = px.pie(values = top_consolas.values, names = top_consolas.index, title = 'Promedio de consolas mas utilizadas',
                 labels={'x': 'Consola', 'y': 'Número de juegos'})
    return fig

fig1_2 = grafico1_2()


# Grafico de Torta: Puntuaciones Metascore
def grafico2():
    meta_score = df['Metascore'].value_counts()
    fig2 = px.pie(values = meta_score.values, names = meta_score.index, title = 'Metascore Promedio')
    return fig2

fig2 = grafico2()


# Grafico de Barras: Cantidad de juegos lanzados por años
def grafico3():
    df['Years'] = pd.DatetimeIndex(df['Date']).year
    top15_años = df['Years'].value_counts()
    top15_años = top15_años.sort_index()
    top15_años.index = top15_años.index.astype(str)
    fig3 = px.bar(y=top15_años.values, x=top15_años.index, text=top15_años.values,
            title = 'Años con Mejores Juegos', labels={'x': 'Año', 'y': 'Cantidad de juegos'})
    return fig3
fig3 = grafico3()


app.layout = html.Div([
    html.Div(
        className='caja-titulo',
        children=[
            html.H1('Visualización de Datos')
        ]),
    
    html.Div(
        className='div-tabla',
        children=[
            html.H2('DataSet: Mejores Video Juegos de todos los tiempos'),
            dash_table.DataTable(
                id='tabla',
                columns=[{"name": i, "id": i} for i in df.columns],
                data=df.to_dict('records'), 
                page_size=10,
                style_cell={'textAlign': 'center', 'minWidth': '0px', 'maxWidth': '180px', 'border': '1px solid black'},
                style_table={'font-size': '16px'},
                style_header={'backgroundColor': '#f39f5a', 'fontWeight': 'bold', 'fontSize': '18px'},
            ),
        ]
    ),

    html.H2('Top 3 Mejores Videojuegos'),

    html.Div(
        className='caja-imagenes',
        children=[
            html.Div(
                className='div-img', 
                children=[
                    html.P('TOP 1: The Legend of Zelda: OFT'),
                    html.Img(src='assets/img/Zelda-Ocarina.jpg', className='img-mejor-juego'),
                ]
            ),
            
            html.Div(
                className='div-img',
                children=[
                    html.P("TOP 2: Tony Hawk's Pro Skater 2"),
                    html.Img(src='assets/img/tony-skater.jpeg', className='img-mejor-juego'),
                ]
            ),

            html.Div(
                className='div-img',
                children=[
                    html.P("TOP 3: Grand Theft Auto IV"),
                    html.Img(src='assets/img/gtaiv.jpeg', className='img-mejor-juego'),
                ]
            ),
        ],
    ),
   
    dcc.Graph(id='graph-consolas', figure=fig1),

    html.H2('Top 3 Mejores Consolas', className='h2-consolas'),

    html.Div(
        className='caja-imagenes',
        children=[
            html.Div(
                className='div-img', 
                children=[
                    html.P('TOP 1: PC'),
                    html.Img(src='assets/img/pc.jpeg', className='img-mejor-juego'),
                ]
            ),
            
            html.Div(
                className='div-img',
                children=[
                    html.P("TOP 2: Play Station 3"),
                    html.Img(src='assets/img/ps3.jpeg', className='img-mejor-juego'),
                ]
            ),

            html.Div(
                className='div-img',
                children=[
                    html.P("TOP 3: Xbox 360"),
                    html.Img(src='assets/img/xbox.jpeg', className='img-mejor-juego'),
                ]
            ),
        ],
    ),

    dcc.Graph(id='graph-consolas2', figure=fig1_2),

    dcc.Graph(id='graph-metascore', figure=fig2),

    dcc.Graph(id='graph-years', figure=fig3),
])

app.run_server(debug=True)