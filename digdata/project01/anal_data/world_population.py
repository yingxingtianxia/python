import json
import pygal
from country_code import get_country_code
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS

filename = '../source_data/population_data.json'
with open(filename, 'r') as fobj:
    pop_data = json.load(fobj)

    cc_populations = {}
    for pop_dict in pop_data:
        if pop_dict['Year'] == '2010':
            country_name = pop_dict['Country Name']
            population = int(float(pop_dict['Value']))

            code = get_country_code(country_name)
            if code:
                cc_populations[code] = population

    cc_pop_1, cc_pop_2, cc_pop_3 = {}, {}, {}
    for cc, pop in cc_populations.items():
        if pop < 10000000:
            cc_pop_1[cc] = pop
        elif pop < 1000000000:
            cc_pop_2[cc] = pop
        else:
            cc_pop_3[cc] = pop

wm_style = RS('#336699', base_style=LCS)
wm = pygal.Worldmap(style=wm_style)
wm.title = 'World Population in 2010, by Country'
wm.add('0-10m', cc_pop_1)
wm.add('10m-1bn', cc_pop_2)
wm.add('>1bn', cc_pop_3)

wm.render_to_file('world_population.svg')