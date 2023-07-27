world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
# Filtra solo los polígonos de los continentes
continentes = world[world['continent'].isin(['Africa', 'Antarctica', 'Asia', 'Europe', 'North America', 'Oceania', 'South America'])]

