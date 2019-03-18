import pygal
from die import Die

die_1 = Die()
die_2 = Die(10)

res = []
for roll_num in range(5000):
    result = die_1.roll() + die_2.roll()
    res.append(result)

frequencies = []
max_res = die_1.num_sides + die_2.num_sides
for value in range(2, max_res):
    frequency = res.count(value)
    frequencies.append(frequency)


hist = pygal.Bar()

hist.title = 'Result of rolling a D6 and a D10 5000 times'
hist.x_labels = [
    '1','2','3','4','5','6','7','8',
    '9','10','11','12','13','14','15','16'
]
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6+D10', frequencies)
hist.render_to_file('different_dice.svg')