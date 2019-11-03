
import folium
import pandas as pd
import numpy as np
import csv
import folium, branca
import folium as features
import numpy
import plotly.graph_objs as go
import plotly
import plotly.express as px

def check_string_to_float(s):
    try:
        float(s)
        return True
    except:
        return False

with open('long_lat.csv', 'r') as f: 

    r = csv.reader(f,delimiter='\t')     
    l = list(r) # l'itérable est converti en liste
    latitude={}

#dictionnaire latitude
    for i in range(1,len(l)):
        if check_string_to_float(l[i][1]) == True:
            latitude[i]= float(l[i][1])
        else:
            latitude[i]=0

#dictionnaire longitude
    longitude={}
    for i in range(1,len(l)):
        if check_string_to_float(l[i][2]) == True:
            longitude[i]= float(l[i][2])
        else:
            longitude[i]=0

#dictionnaire des pays dans le meme ordre que longitude et latitude
    pays={}
    for i in range(len(l)):
        pays[i]= l[i][3]

#dictionnaire key=pays, values= age moyen en 2015 
age_moyen_par_pays_2015= {}
filename = 'median_age_years.csv'
dataset = pd.read_csv(filename)
country = dataset['country'].unique()
age_moyen_2015=dataset['2015']

for i in range(len(country)):
    age_moyen_par_pays_2015[country[i]]=float(age_moyen_2015[i])

#dictionnaire key=pays, values= indice d'accés à l'eau en 2015 
eau_par_pays_2015= {}
filename = 'at_least_basic_water_source_urban_access_percent (6).csv'
dataset = pd.read_csv(filename)
country_eau = dataset['country'].unique()
eau_2015 =dataset['2015']

for i in range(len(country_eau)):
    eau_par_pays_2015[country_eau[i]]=float(eau_2015[i])


#dictionnaire key=pays, values= indice d'accés à des sanitaires en 2015 
sanitaire_par_pays_2015= {}
filename = 'at_least_basic_sanitation_urban_access_percent.csv'
dataset = pd.read_csv(filename)
country_sanitaire = dataset['country'].unique()
sanitaire_2015 =dataset['2015']

for i in range(len(country_sanitaire)):
    sanitaire_par_pays_2015[country_sanitaire[i]]=float(sanitaire_2015[i])


#dictionnaire key=pays, values= éspérence de vie en 2015 
esperence_par_pays_2015= {}
filename = 'life_expectancy_years.csv'
dataset = pd.read_csv(filename)
country_esperence = dataset['country'].unique()
esperence_2015 =dataset['2015']

for i in range(len(country_esperence)):
    esperence_par_pays_2015[country_esperence[i]]=float(esperence_2015[i])



#Nouveau dictionnaire des éspérences de vie dans le meme ordre de pays que latitude et longitude 
#Deux listes différentes nécessaire pour gérer les problémes dus au type des variables
esperence_2015_ordone={}
for i in range (1,len(pays)):
    esperence_2015_ordone[i]=0

    for x in range (len(country_esperence)):
        if pays[i] == country_esperence[x]:  
            esperence_2015_ordone[i]= esperence_par_pays_2015[pays[i]]

esperence_2015_ordone2={}
for i in range (1,len(pays)):
    esperence_2015_ordone2[i]= np.NaN

    for x in range (len(country_esperence)):
        if pays[i] == country_esperence[x]:  
            esperence_2015_ordone2[i]= esperence_par_pays_2015[pays[i]]


#Nouveau dictionnaire des éspérences de vie dans le meme ordre de pays que latitude et longitude 
#Deux listes différentes nécessaire pour gérer les problémes dus au type des variables
esperence_2015_ordone={}
for i in range (1,len(pays)):
    esperence_2015_ordone[i]=0

    for x in range (len(country_esperence)):
        if pays[i] == country_esperence[x]:  
            esperence_2015_ordone[i]= esperence_par_pays_2015[pays[i]]

esperence_2015_ordone2={}
for i in range (1,len(pays)):
    esperence_2015_ordone2[i]= np.NaN

    for x in range (len(country_esperence)):
        if pays[i] == country_esperence[x]:  
            esperence_2015_ordone2[i]= esperence_par_pays_2015[pays[i]]


#Nouveau dictionnaire des ages moyens dans le meme ordre de pays que latitude et longitude 
#Deux listes différentes nécessaire pour gérer les problémes dus au type des variables
age_moyen_2015_ordone={}
for i in range (1,len(pays)):
    age_moyen_2015_ordone[i]=0

    for x in range (len(country)):
        if pays[i] == country[x]:  
            age_moyen_2015_ordone[i]= age_moyen_par_pays_2015[pays[i]]


age_moyen_2015_ordone2={}
for i in range (1,len(pays)):
    age_moyen_2015_ordone2[i]= np.NaN

    for x in range (len(country)):
        if pays[i] == country[x]:  
            age_moyen_2015_ordone2[i]= age_moyen_par_pays_2015[pays[i]]

#Nouveau dictionnaire des indices d'accés à l'eau dans le meme ordre de pays que latitude et longitude 
#Deux listes différentes nécessaire pour gérer les problémes dus au type des variables
eau_2015_ordone={}
for i in range (1,len(pays)):
    eau_2015_ordone[i]=0

    for x in range (len(country_eau)):
        if pays[i] == country_eau[x]:  
            eau_2015_ordone[i]= eau_par_pays_2015[pays[i]]

eau_2015_ordone2={}
for i in range (1,len(pays)):
    eau_2015_ordone2[i]= np.NaN

    for x in range (len(country_eau)):
        if pays[i] == country_eau[x]:  
            eau_2015_ordone2[i]= eau_par_pays_2015[pays[i]]

#Nouveau dictionnaire des indices d'accés à des sanitaires dans le meme ordre de pays que latitude et longitude 
#Deux listes différentes nécessaire pour gérer les problémes dus au type des variables
sanitaire_2015_ordone={}
for i in range (1,len(pays)):
    sanitaire_2015_ordone[i]=0

    for x in range (len(country_sanitaire)):
        if pays[i] == country_sanitaire[x]:  
            sanitaire_2015_ordone[i]= sanitaire_par_pays_2015[pays[i]]

sanitaire_2015_ordone2={}
for i in range (1,len(pays)):
    sanitaire_2015_ordone2[i]= np.NaN

    for x in range (len(country_sanitaire)):
        if pays[i] == country_sanitaire[x]:  
            sanitaire_2015_ordone2[i]= sanitaire_par_pays_2015[pays[i]]

#création de liste des valeurs des dictionnaires pour plus de fonctionnalitées

esperence_2015_ordone_list = []
for k, v in esperence_2015_ordone.items():
    esperence_2015_ordone_list.append(v)
    esperence_2015_ordone_list

esperence_2015_ordone_list2 = []
for k, v in esperence_2015_ordone2.items():
    esperence_2015_ordone_list2.append(v)
    esperence_2015_ordone_list2

sanitaire_2015_ordone_list = []
for k, v in sanitaire_2015_ordone.items():
    sanitaire_2015_ordone_list.append(v)
    sanitaire_2015_ordone_list

sanitaire_2015_ordone_list2 = []
for k, v in sanitaire_2015_ordone2.items():
    sanitaire_2015_ordone_list2.append(v)
    sanitaire_2015_ordone_list2

eau_2015_ordone_list = []
for k, v in eau_2015_ordone.items():
    eau_2015_ordone_list.append(v)
    eau_2015_ordone_list

eau_2015_ordone_list2 = []
for k, v in eau_2015_ordone2.items():
    eau_2015_ordone_list2.append(v)
    eau_2015_ordone_list2

age_moyen_2015_ordone_list = []
for k, v in age_moyen_2015_ordone.items():
    age_moyen_2015_ordone_list.append(v)
    age_moyen_2015_ordone_list

age_moyen_2015_ordone_list2 = []
for k, v in age_moyen_2015_ordone2.items():
    age_moyen_2015_ordone_list2.append(v)
    age_moyen_2015_ordone_list2

latitude_list = []
for k, v in latitude.items():
    latitude_list.append(v)
    latitude_list

longitude_list = []
for k, v in longitude.items():
    longitude_list.append(v)
    longitude_list   

#création de Array liste a partir de liste pour plus de fonctionnalitées 
age_moyen_2015_ordone_ArrayList = np.asarray(age_moyen_2015_ordone_list)
age_moyen_2015_ordone_ArrayList2 = np.asarray(age_moyen_2015_ordone_list2)

eau_2015_ordone_ArrayList = np.asarray(eau_2015_ordone_list)
eau_2015_ordone_ArrayList2 = np.asarray(eau_2015_ordone_list2)

sanitaire_2015_ordone_ArrayList = np.asarray(sanitaire_2015_ordone_list)
sanitaire_2015_ordone_ArrayList2 = np.asarray(sanitaire_2015_ordone_list2)

esperence_2015_ordone_ArrayList = np.asarray(esperence_2015_ordone_list)
esperence_2015_ordone_ArrayList2 = np.asarray(esperence_2015_ordone_list2)


#fonction permettant le tracer d'un graphe mettant de liste

def create_graph (graph_title,X_list2,X_title,Y_list2,Y_title,name_graph):
    trace = go.Scatter(
        
        x= X_list2 ,
        y= Y_list2,
        mode='markers',)
    data = [trace]
    layout = go.Layout(title=graph_title,
                    xaxis=dict(
                        title=X_title,
                        ticklen=5,
                        zeroline=False,
                        gridwidth=2,
                    ),
                    yaxis=dict(
                        title=Y_title,
                        ticklen=5,
                        zeroline=False,
                        gridwidth=2,
                    ),)
    fig = go.Figure(data=data, layout=layout)
    return fig



#fonction permettant le tracer de carte
def create_map(arayList2,ordoneList,latList,longList,name_map,colors,valeur,unite):

    coords = (46.6299767,1.8489683)
    map = folium.Map(location=coords, tiles='OpenStreetMap', zoom_start=5)

    vmin_age_moyen=  np.nanmin(arayList2) 
    vmax_age_moyen= np.nanmax(arayList2)

    # define a colorbar between min and max values

    cm = branca.colormap.LinearColormap(colors, vmin= vmin_age_moyen, vmax= vmax_age_moyen)
    map.add_child(cm) 

    f = folium.map.FeatureGroup() 
    i=0
    for latList, longList, size, color in zip(latList, longList, ordoneList, ordoneList):
        i= i+1
        if ordoneList[i-1] != 0 :
            f.add_child( 
                folium.CircleMarker(
                    location=[latList, longList],
                    radius=30,
                    color=None,
                    fill=True,
                    fill_color=cm(color),
                    fill_opacity=0.6,

                    tooltip = pays[i] + "  :   "+ valeur +" :  " + str(size) + unite
                        
                        )
        )

    map.add_child(f) 

    map.save(outfile=name_map + '.html')


#création des différentes carte à l'aide de l'appel de la fonction create_map

create_map(eau_2015_ordone_ArrayList2, eau_2015_ordone_list,latitude_list,longitude_list,'map_eau',[(139,0,0),'red','orange','yellow','green'],"indice d'accés à l'eau","%")

create_map(age_moyen_2015_ordone_ArrayList2, age_moyen_2015_ordone_list,latitude_list,longitude_list,'map_age',['red', 'yellow', 'green'],"moyenne d'age","ans")

create_map(sanitaire_2015_ordone_ArrayList2, sanitaire_2015_ordone_list,latitude_list,longitude_list,'map_sanitaire',[(139,0,0),'red','orange','yellow','green'],"indice d'accés à des sanitaires","%")

create_map(esperence_2015_ordone_ArrayList2, esperence_2015_ordone_list,latitude_list,longitude_list,'map_esperence',[(139,0,0),'red','orange','yellow','green'],"éspérence de vie ","ans")

#création des différents graphs à l'aide de l'appel de la fonction create_graph

graph1=create_graph("Age moyen des pays en fonction de leur indice d'accés à des sanitaires ",sanitaire_2015_ordone_list2,"indice d'accés à des sanitaires",age_moyen_2015_ordone_list2,"age moyen de la population","graphe_age_sanitaire")

graph2=create_graph("Age moyen des pays en fonction de leur indice d'accés à l'eau potable ",eau_2015_ordone_list2,"indice d'accés à l'eau potable",age_moyen_2015_ordone_list2,"age moyen de la population","graphe_age_eau")

graph3=create_graph("Espérence de vie par pays en fonction de leur indice d'accés à des sanitaires ",sanitaire_2015_ordone_list2,"indice d'accés à des sanitaires",esperence_2015_ordone_list2,"éspérence de vie","graphe_esperence_sanitaire")

graph4=create_graph("Espérence de vie par pays en fonction de leur indice d'accés à l'eau potable ",eau_2015_ordone_list2,"indice d'accés à l'eau potable",esperence_2015_ordone_list2,"éspérence de vie","graphe_esperence_eau")


minimum_age_moyen = numpy.nanmin(age_moyen_2015_ordone_list2)
maximum_age_moyen = numpy.nanmax(age_moyen_2015_ordone_list2)
mediane_age_moyen = numpy.nanmedian(age_moyen_2015_ordone_list2)
moyenne_age_moyen = numpy.nanmean(age_moyen_2015_ordone_ArrayList2)
variance_age_moyen = numpy.nanvar(age_moyen_2015_ordone_ArrayList2)


esperence_eau_list=np.concatenate((esperence_2015_ordone_list2, eau_2015_ordone_list2))
esperence_eau_sanitaire_list=np.concatenate((esperence_eau_list,sanitaire_2015_ordone_list2))


#Création des deux histogrames
histo1 = px.histogram(esperence_eau_sanitaire_list, x= esperence_eau_sanitaire_list[245:490], y=esperence_eau_sanitaire_list[0:245], histfunc ='avg',title="éspérence de vie (ordonné) en fonction de l'accés à l'eau potable (abscisse)")

histo2 = px.histogram(esperence_eau_sanitaire_list, x= esperence_eau_sanitaire_list[490:735], y=esperence_eau_sanitaire_list[0:245], histfunc ='avg',title="éspérence de vie (ordonné) en fonction de l'accés à des services d'assainissement (abscisse)")



import dash
import dash_core_components as dcc
import dash_html_components as html


app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Projet anlayse de données en python'),
    html.H2(children='Contexte'),

    html.Div(children="""De nos jours, les immenses avancées technologiques et techniques dans de nombreux 
    domaines tel que le transport, la santé, l'énergie, l’informatique.... 
    """),
    html.Div(children="""Nous permettent d’améliorer notre niveau et notre confort de vie, 
    malgrès cela de nombreuses inégalitées subsistent 
    sur notre planète et de nombreux pays ne bénéficient pas de ces avancées.
        
    """),
    html.Div(children="""En effet de nombreux pays majoritairement sur le continent Africain ne bénéficie même pas des 
    infrastructures élémentaires tel que l'accès à l’eau potable, aux soins, ou à des services d’assainissements.
        
    """),
    html.Div(children="""A travers l’étude de données que j’ai effectuée j’ai souhaité mettre en évidence ces
     inégalités de moyens qu’il y’a entre les différents pays et les conséquences direct que celles-ci engendrent.
        
    """),
    
    html.H2(children='Graphiques'),
    dcc.Graph(
        id='graph3',
        figure=graph3,
    ),

    dcc.Graph(
        id='graph4',
        figure=graph4,
    ),

    dcc.Graph(
        id='graph1',
        figure=graph1,
    ),
    dcc.Graph(
        id='graph2',
        figure=graph2,
    ),

    html.Div(children="""A travers ces 4 graphiques nous pouvons voir que les pays ayant un faible accès aux infrastructures tels que des services d’assainissements ou à l’eau potable, on une espérance de vie de leur population beaucoup plus faible.
       
    """),
    html.Div(children="""
    Ce qui influe sur la moyenne d'âge de la population.
       
    """),
    html.H2(children='Histogrammes'),

    dcc.Graph(
        id='histo1',
        figure=histo1
    ),
    html.Div(children=""" A travers ces deux histogrammes nous pouvons observer que le manque d'accès à l’eau potable ainsi qu’à des services d'assainissements influe directement sur sur l'espérance de vie.        
    """),

    dcc.Graph(
        id='histo2',
        figure=histo2
    ),

    html.H2(children='Map'),
    html.Div(children="""Ouvrir les différents fichier HTML intitulé "map_XXXX_XXXX.html" générés à l'éxécution du programme
    """),

   html.Div(children=""" Sur ces différentes cartes nous pouvons bien voir le lien qu’il existe entre les conditions d'accès à l’eau potable et aux infrastructure d’assainissements et les espérances de vie et moyennes d'âge dans les différents pays.       
    """),
])

app.run_server(debug=True)


