from covid19 import covid_data
jhu_data = covid_data.load_jhu_data()

import datetime
import matplotlib.pyplot as plt
import matplotlib.ticker as tkr

from covid19 import covid_data

#jhu_data = covid_data.load_jhu_data()
country_meta_datas = [
    {'alpha_2': 'IN', 'color': 'orange'},
    {'alpha_2': 'LK', 'color': 'maroon'},
    {'alpha_2': 'PK', 'color': 'lightgreen'},
    {'alpha_2': 'NP', 'color': 'blue'},
    {'alpha_2': 'BD', 'color': 'darkgreen'},
    {'alpha_2': 'AF', 'color': 'lightblue'},
    {'alpha_2': 'MV', 'color': 'red'},
    {'alpha_2': 'BT', 'color': 'purple'},
]

legend_labels = []
for country_meta_data in country_meta_datas:
    country_data = jhu_data[country_meta_data['alpha_2']]
    legend_labels.append(country_data['country_name'])
    timeseries = country_data['timeseries']
    population = country_data['population']

    x = list(map(
        lambda d: datetime.datetime.fromtimestamp(d['unixtime']),
        timeseries,
    ))
    y = list(map(
        lambda d: 100_000 * d['cum_deaths'] / population,
        timeseries,
    ))
    plt.plot(x, y, color=country_meta_data['color'])

plt.title('Total Deaths per 100,000 people in South Asia.')
plt.suptitle(
    'Data Source: https://github.com/CSSEGISandData/COVID-19',
    fontsize=6,
)
plt.legend(
    legend_labels,
    loc='upper left',
)

ax = plt.gca()
ax.get_yaxis().set_major_formatter(
    tkr.FuncFormatter(lambda x, p: format(int(x), ','))
)

fig = plt.gcf()
fig.autofmt_xdate()
fig.set_size_inches(8, 4.5)
fig.savefig('lk/img/death.png', dpi=600)

import datetime
import matplotlib.pyplot as plt
import matplotlib.ticker as tkr

from covid19 import covid_data

#jhu_data = covid_data.load_jhu_data()
country_meta_datas = [
    {'alpha_2': 'IN', 'color': 'orange'},
    {'alpha_2': 'LK', 'color': 'maroon'},
    {'alpha_2': 'PK', 'color': 'lightgreen'},
    {'alpha_2': 'NP', 'color': 'blue'},
    {'alpha_2': 'BD', 'color': 'darkgreen'},
    {'alpha_2': 'AF', 'color': 'lightblue'},
    # {'alpha_2': 'MV', 'color': 'red'},
    {'alpha_2': 'BT', 'color': 'purple'},
]

legend_labels = []
for country_meta_data in country_meta_datas:
    country_data = jhu_data[country_meta_data['alpha_2']]
    legend_labels.append(country_data['country_name'])
    timeseries = country_data['timeseries']
    population = country_data['population']

    x = list(map(
        lambda d: datetime.datetime.fromtimestamp(d['unixtime']),
        timeseries,
    ))
    y = list(map(
        lambda d: 100_000 * d['active'] / population,
        timeseries,
    ))

    plt.plot(x, y, color=country_meta_data['color'])

plt.title(
    'Active COVID19Cases per 100,000 people in South Asia.',
)
plt.suptitle(
    'Data Source: https://github.com/CSSEGISandData/COVID-19',
    fontsize=6,
)
plt.legend(
    legend_labels,
    loc='upper left',
)

ax = plt.gca()
ax.get_yaxis().set_major_formatter(
    tkr.FuncFormatter(lambda x, p: format(int(x), ','))
)

fig = plt.gcf()
fig.autofmt_xdate()
fig.set_size_inches(8, 4.5)
fig.savefig('lk/img/active.png', dpi=600)

country_meta_datas = [
    #{'alpha_2': 'IN', 'color': 'orange'},
    {'alpha_2': 'LK', 'color': 'maroon'},
    #{'alpha_2': 'PK', 'color': 'lightgreen'},
    #{'alpha_2': 'NP', 'color': 'blue'},
    #{'alpha_2': 'BD', 'color': 'darkgreen'},
    #{'alpha_2': 'AF', 'color': 'lightblue'},
    # {'alpha_2': 'MV', 'color': 'red'},
    #{'alpha_2': 'BT', 'color': 'purple'},
]

legend_labels = []
for country_meta_data in country_meta_datas:
    country_data = jhu_data[country_meta_data['alpha_2']]
    legend_labels.append(country_data['country_name'])
    timeseries = country_data['timeseries']
    population = country_data['population']

    x = list(map(
        lambda d: datetime.datetime.fromtimestamp(d['unixtime']),
        timeseries,
    ))
    y = list(map(
        lambda d: 100_000 * d['active'] / population,
        timeseries,
    ))

    plt.plot(x, y, color=country_meta_data['color'])

plt.title(
    'Active COVID19Cases per 100,000 people in South Asia.',
)
plt.suptitle(
    'Data Source: https://github.com/CSSEGISandData/COVID-19',
    fontsize=6,
)
plt.legend(
    legend_labels,
    loc='upper left',
)

ax = plt.gca()
ax.get_yaxis().set_major_formatter(
    tkr.FuncFormatter(lambda x, p: format(int(x), ','))
)

fig = plt.gcf()
fig.autofmt_xdate()
fig.set_size_inches(8, 4.5)
fig.savefig('lk/img/active_SL.png', dpi=600)


country_data = covid_data.load_jhu_data()['LK']
timeseries = country_data['timeseries']

x = list(map(
    lambda d: datetime.datetime.fromtimestamp(d['unixtime']),
    timeseries,
))
y1 = list(map(
    lambda d: d['active'],
    timeseries,
))
y2 = list(map(
    lambda d: d['cum_recovered'],
    timeseries,
))
y3 = list(map(
    lambda d: d['cum_deaths'],
    timeseries,
))

plt.stackplot(x, y1, y2, y3, colors=['blue', 'green', 'red'])

plt.title(
    'Daily COVID19 Active Cases, Total Recovered Cases, '
    + '& Total Deaths in %s.' % (country_data['country_name'])
)
plt.suptitle(
    'Data Source: https://github.com/CSSEGISandData/COVID-19 '
    + '& https://www.hpb.health.gov.lk/api/get-current-statistical',
    fontsize=6,
)
plt.legend(
    ['Active', 'Total Recovered', 'Total Deaths'],
    loc='upper left',
)

ax = plt.gca()
ax.get_yaxis().set_major_formatter(
    tkr.FuncFormatter(lambda x, p: format(int(x), ','))
)

fig = plt.gcf()
fig.autofmt_xdate()
fig.set_size_inches(12, 6.75)
fig.savefig('lk/img/recovered.png', dpi=600)

from covid19 import lk_data

timeseries = lk_data.get_timeseries()

x = list(map(
    lambda d: datetime.datetime.fromtimestamp(d['unixtime']),
    timeseries,
))
y = list(map(
    lambda d: d['new_confirmed'],
    timeseries,
))
plt.plot(x, y, color='red')

y2 = list(map(
    lambda d: d['new_pcr_tests'],
    timeseries,
))
plt.plot(x, y2, color='blue')

plt.title('Daily New COVID19 Cases and PCR Tests in Sri Lanka.')
plt.suptitle(
    'Data Source: https://github.com/CSSEGISandData/COVID-19',
    fontsize=6,
)
plt.legend(['Daily New Cases', 'Daily PCR Tests'])

ax = plt.gca()
ax.get_yaxis().set_major_formatter(
    tkr.FuncFormatter(lambda x, p: format(int(x), ','))
)

fig = plt.gcf()
fig.autofmt_xdate()
fig.set_size_inches(12, 6.75)
fig.savefig('lk/img/casesvstest.png', dpi=600)


import numpy as np

from covid19 import lk_data

timeseries = lk_data.get_timeseries()

x = list(map(
    lambda d: datetime.datetime.fromtimestamp(d['unixtime']),
    timeseries,
))

y = list(map(
    lambda d: d['new_confirmed'] / d['new_pcr_tests'] \
        if d['new_pcr_tests'] > 10 \
        else 0,
    timeseries,
))
plt.plot(x, y, color='pink')
N = 14
y = np.convolve(y, np.ones(N) / N, 'valid')
plt.plot(x[:-(N - 1)], y, color='red')

plt.title('Daily New COVID19 Cases per PCR Tests in Sri Lanka.')
plt.suptitle(
    'Data Source: https://github.com/CSSEGISandData/COVID-19 & https://www.hpb.health.gov.lk/api/get-current-statistical',
    fontsize=6,
)
plt.legend(['Cases per Test', '%d-Day Moving Window' % N])

ax = plt.gca()
ax.get_yaxis().set_major_formatter(
    tkr.FuncFormatter(lambda x, p: format(float(x), '.2%'))
)

fig = plt.gcf()
fig.autofmt_xdate()
fig.set_size_inches(12, 6.75)
fig.savefig('lk/img/pcrpercent.png', dpi=600)



legend_labels = []
country_meta_datas = [
    {'alpha_2': 'IN', 'color': 'orange'},
    {'alpha_2': 'LK', 'color': 'maroon'},
    {'alpha_2': 'PK', 'color': 'lightgreen'},
    {'alpha_2': 'NP', 'color': 'blue'},
    {'alpha_2': 'BD', 'color': 'darkgreen'},
    {'alpha_2': 'AF', 'color': 'lightblue'},
    # {'alpha_2': 'MV', 'color': 'red'},
    {'alpha_2': 'BT', 'color': 'purple'},
]
for country_meta_data in country_meta_datas:
    country_data = jhu_data[country_meta_data['alpha_2']]
    legend_labels.append(country_data['country_name'])
    timeseries = country_data['timeseries']
    population = country_data['population']

    x = list(map(
        lambda d: datetime.datetime.fromtimestamp(d['unixtime']),
        timeseries,
    ))
    y = list(map(
        lambda d: d['cum_people_vaccinated'] / population,
        timeseries,
    ))
    plt.plot(x, y, color=country_meta_data['color'])

plt.title('% People vaccinated in South Asia.')
plt.suptitle(
    'Data Source: https://github.com/CSSEGISandData/COVID-19 '
    + '& https://github.com/owid/covid-19-data',
    fontsize=6,
)
plt.legend(
    legend_labels,
    loc='upper left',
)

ax = plt.gca()
ax.get_yaxis().set_major_formatter(
    tkr.FuncFormatter(lambda x, p: format(float(x), '.2%'))
)

fig = plt.gcf()
fig.autofmt_xdate()
fig.set_size_inches(8, 4.5)
fig.savefig('lk/img/vaccinated.png', dpi=600)



country_alpha_2 = 'LK'
country_data = jhu_data[country_alpha_2]
country_name = country_data['country_name']
timeseries = country_data['timeseries'][-150:]
population = country_data['population']

x = list(map(
    lambda d: datetime.datetime.fromtimestamp(d['unixtime']),
    timeseries,
))
y1 = list(map(
    lambda d: d['cum_people_fully_vaccinated'] / population,
    timeseries,
))
y2 = list(map(
    lambda d:
        (d['cum_people_vaccinated'] - d['cum_people_fully_vaccinated'])
            / population,
    timeseries,
))

plt.stackplot(x, y1, y2, colors=['green', 'lightgreen'])

plt.title(
    '%% People Vaccinated in %s.' % (country_name)
)
plt.suptitle(
    'Data Source: https://github.com/CSSEGISandData/COVID-19'
    + '& https://www.hpb.health.gov.lk/api/get-current-statistical',
    fontsize=6,
)
plt.legend(
    ['Fully', 'Partially'],
    loc='upper left',
)

ax = plt.gca()
ax.get_yaxis().set_major_formatter(
    tkr.FuncFormatter(lambda x, p: format(float(x), '.2%'))
)

fig = plt.gcf()
fig.autofmt_xdate()
fig.set_size_inches(12, 6.75)
fig.savefig('lk/img/vaccinated_%s.png' % (country_alpha_2), dpi=600)


country_alpha_2 = 'LK'
country_data = jhu_data[country_alpha_2]
country_name = country_data['country_name']
timeseries = country_data['timeseries']

delay = 7
mortality_rate = timeseries[-1]['cum_deaths'] \
    / timeseries[-delay]['cum_confirmed']

x = list(map(
    lambda d: datetime.datetime.fromtimestamp(d['unixtime']),
    timeseries,
))
y1 = list(map(
    lambda d: d['new_deaths'],
    timeseries,
))
N = 7
y2 = np.convolve(y1, np.ones(N) / N, 'valid')
plt.plot(x[:-(N - 1)], y2, color='red')

y3 = list(map(
    lambda d: d['new_confirmed'] * mortality_rate,
    [{'new_confirmed': 0 } for _ in range(0, delay)] + timeseries[:-delay],
))
y4 = np.convolve(y3, np.ones(N) / N, 'valid')
plt.plot(x[:-(N - 1)], y4, color='blue')

plt.title(
    'New COVID19 Deaths in %s vs. "Predicted Deaths"' % (country_name)

)
plt.suptitle(
    'Data Source: https://github.com/CSSEGISandData/COVID-19 ',
    fontsize=6,
)
plt.legend([
    'New Deaths (%d Data Window)' % N,
    '"Predicted Deaths" = New Confirmed Cases %d days before *  %4.2f%%' % (delay, mortality_rate * 100.0),
])

ax = plt.gca()
ax.get_yaxis().set_major_formatter(
    tkr.FuncFormatter(lambda x, p: format(int(x), ','))
)

fig = plt.gcf()
fig.autofmt_xdate()
fig.set_size_inches(12, 6.75)
fig.savefig('lk/img/death_%s.png' % country_alpha_2, dpi=600)


country_alpha_2 = 'LK'
country_data = jhu_data[country_alpha_2]
country_name = country_data['country_name']
timeseries = country_data['timeseries'][-150:]
population = country_data['population']

x = list(map(
    lambda d: datetime.datetime.fromtimestamp(d['unixtime']),
    timeseries,
))
y1 = list(map(
    lambda d: d['cum_people_fully_vaccinated'] / population,
    timeseries,
))
y2 = list(map(
    lambda d: d['cum_people_vaccinated'] / population,
    timeseries,
))

legend = [
    'Fully Vaccinated',
    'At least 1st dose',
]
plt.plot(x, y1,  color="green")
plt.plot(x, y2,  color="lightgreen")

windows = [4, 6, 8, 10, 12, 14]
n_windows = len(windows)
for i, weeks in enumerate(windows):
    days_to_second_dose1 = 7 * weeks
    y = [0 for _ in range(0, days_to_second_dose1)] + list(map(
        lambda d: d['cum_people_vaccinated'] / population,
        timeseries[:-days_to_second_dose1],
    ))
    r = 1
    g = 0.8 - 0.8 * i / n_windows
    b = g
    plt.plot(x, y,  color=(r, g, b))
    legend.append('%d weeks since 1st dose' % weeks)

plt.title(
    '%% People Vaccinated in %s.' % (country_name)
)
plt.suptitle(
    'Data Source: https://github.com/CSSEGISandData/COVID-19'
    + '& https://www.hpb.health.gov.lk/api/get-current-statistical',
    fontsize=6,
)
plt.legend(
    legend,
    loc='upper left',
)

ax = plt.gca()
ax.get_yaxis().set_major_formatter(
    tkr.FuncFormatter(lambda x, p: format(float(x), '.2%'))
)

fig = plt.gcf()
fig.autofmt_xdate()
fig.set_size_inches(12, 6.75)
fig.savefig('lk/img/vaccinedelay_%s.png' % (country_alpha_2), dpi=300)




import os
field_key = 'new_deaths'
field_label = 'New Deaths per Day'
country_meta_datas = [
    {'alpha_2': 'IN', 'color': 'orange'},
    {'alpha_2': 'LK', 'color': 'maroon'},
    {'alpha_2': 'PK', 'color': 'lightgreen'},
    {'alpha_2': 'BD', 'color': 'darkgreen'},
    # {'alpha_2': 'NP', 'color': 'blue'},
    # {'alpha_2': 'AF', 'color': 'lightblue'},
    # {'alpha_2': 'MV', 'color': 'red'},
    # {'alpha_2': 'BT', 'color': 'purple'},
]

legend_labels = []
for country_meta_data in country_meta_datas:
    country_data = jhu_data[country_meta_data['alpha_2']]
    legend_labels.append(country_data['country_name'])
    timeseries = country_data['timeseries']
    population = country_data['population']

    x = list(map(
        lambda d: datetime.datetime.fromtimestamp(d['unixtime']),
        timeseries,
    ))
    y = list(map(
        lambda d: 100_000 * d[field_key] / population,
        timeseries,
    ))
    N = 14
    y = np.convolve(y, np.ones(N) / N, 'valid')
    plt.plot(x[:-(N - 1)], y, color=country_meta_data['color'])

plt.title(
    '%s per 100,000 people in South Asia (%d day average).' % (
        field_label,
        N,
    )
)
plt.suptitle(
    'Data Source: https://github.com/CSSEGISandData/COVID-19',
    fontsize=6,
)
plt.legend(
    legend_labels,
    loc='upper left',
)

ax = plt.gca()
ax.get_yaxis().set_major_formatter(
    tkr.FuncFormatter(lambda x, p: format(float(x), '.2'))
)

fig = plt.gcf()
fig.autofmt_xdate()
fig.set_size_inches(8, 4.5)
file_name = 'lk/img/newdeath.png'
fig.savefig(file_name, dpi=300)






