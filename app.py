from dash import Dash, html, dcc, dash_table, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_csv('csv/data.csv')
df.drop(columns=['Unnamed: 2','Unnamed: 7','Title'], inplace=True)


# Grafico de Barras: Consolas
def grafico1():
    top_consolas = df['Platform'].value_counts()
    fig = px.bar(y=top_consolas.values, x=top_consolas.index, title='Top Consolas mas utilizadas',
            labels={'x': 'Consola', 'y': 'Número de juegos'})
    return fig

fig1 = grafico1()


# Grafico de Barras: Puntuaciones Metascore
def grafico2():
    meta_score = df['Metascore'].value_counts()
    fig2 = px.pie(values = meta_score.values, names = meta_score.index, title = 'Metascore Promedio')
    return fig2

fig2 = grafico2()


def grafico3():
    df['Years'] = pd.DatetimeIndex(df['Date']).year
    top15_años = df['Years'].value_counts()[:15]
    fig3 = px.bar(y = top15_años.values, x = top15_años.index, 
            text = top15_años.values, title = 'Top 15 años con mejores juegos')
    fig3.update_layout(xaxis_title = "Año", yaxis_title = "Count")
    return fig3

fig3 = grafico3()

app.layout = html.Div(children=[
    html.H1(children='Visualización de Datos', style={'textAlign': 'center'}),

    html.H3(children='DataSet: Mejores Video Juegos de todos los tiempos', style={}),

    dash_table.DataTable(
        id='tabla',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'), 
        page_size=10,
        style_cell={
            'textAlign': 'center',  
            'minWidth': '0px',      
            'maxWidth': '180px',    
            'whiteSpace': 'normal', 
            'overflow': 'hidden',   
            'textOverflow': 'ellipsis', 
        },
    ),

    html.Button('Mostrar Gráfico', id='boton-mostrar-grafico'), # Boton para mostrar grafico de barras
    html.Div(id='contenedor-grafico', children=[]), # Caja donde se cargará el gráfico de consolas

    dcc.Graph(id='graph-content', figure=fig2), # Dibujar grafico de torta

    dcc.Graph(id='graph-years', figure=fig3) # Dibujar grafico de barras horizontales

])


@app.callback(
    [Output(component_id='contenedor-grafico', component_property='style'),
    Output(component_id='contenedor-grafico', component_property='children')],
    Input(component_id='boton-mostrar-grafico', component_property='n_clicks')
)


def mostrar_grafico1(click):
    if click:
        style = {'display': 'block'}
        graph = dcc.Graph(id='grafico_barras_consola', figure=fig1)
    else:
        style = {'display': 'none'}
        graph = None
    return style, graph



app.run_server(debug=True)