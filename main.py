import os
import geopandas as gpd

path_25k: str = 'data/Polska podział arkuszowy 25k/25k_all.shp'
gdf_25k = gpd.read_file(path_25k)

lista_plikow_vmap: list = os.listdir('data/vmap')
lista_plikow_vmap_shp: list = [file for file in lista_plikow_vmap if file.endswith('.shp')]

tmp_gdf = gpd.read_file(f'data/vmap/{lista_plikow_vmap_shp[0]}', encoding="utf-32")
tmp_name = lista_plikow_vmap_shp[0]
print('to jest przetwarzany plik: ', tmp_name)

for file in lista_plikow_vmap_shp:
    print('TU JEST NAZWA PLIKU', file)
    tmp_file_vmap = gpd.read_file(f'data/vmap/{file}', encoding="utf-16")

    for idx, row in gdf_25k.iterrows():
        tmp_gdf_of_single_25k_sheet = gdf_25k.iloc[[idx]]

        tmp_instersekcja = gpd.overlay(tmp_gdf_of_single_25k_sheet, tmp_file_vmap, how='intersection')
        if not tmp_instersekcja.empty:
            tmp_instersekcja.to_file(f'output/godlo_{idx}_{file}.gpkg', driver='GPKG')
