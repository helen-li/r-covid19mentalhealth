"""CSC110 Fall 2021 Final Project

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2021 Asma Jaseem, Helen Li.
"""
import plotly.express as px
import plotly.io as pio
import pandas
import openpyxl


def read_xslx_file(filename: str, term: str) -> dict:
    """
    Returns data for the terms based on data stored in the file given by filename.
    """
    search_term_interest = {}
    data = pandas.read_excel(filename)
    df = pandas.DataFrame(data, columns=[term])
    search_term_interest[term] = list(df[term])
    return search_term_interest


def create_line_plots(term: str) -> px.line():
    """
    Plot a line graph corresponding to each term.
    """
    japan_terms = read_xslx_file('search_terms/search_term_japan.xlsx', term)[term]
    italy_terms = read_xslx_file('search_terms/search_term_italy.xlsx', term)[term]
    canada_terms = read_xslx_file('search_terms/search_term_canada.xlsx', term)[term]
    iran_terms = read_xslx_file('search_terms/search_term_iran.xlsx', term)[term]
    uk_terms = read_xslx_file('search_terms/search_term_uk.xlsx', term)[term]
    us_terms = read_xslx_file('search_terms/search_term_us.xlsx', term)[term]
    world_terms = read_xslx_file('search_terms/search_term_worldwide.xlsx', term)[term]
    week = read_xslx_file('search_terms/search_term_worldwide.xlsx', 'Week')['Week']

    fig = px.line(x=week, y=[
        japan_terms, italy_terms, canada_terms, iran_terms, uk_terms, us_terms, world_terms
    ], labels={'value': 'search term frequency', 'x': 'week', 'variable': 'country'})

    new_names = {
        'wide_variable_0': 'japan', 'wide_variable_1': 'italy',
        'wide_variable_2': 'canada', 'wide_variable_3': 'iran',
        'wide_variable_4': 'uk', 'wide_variable_5': 'us', 'wide_variable_6': 'world'}

    fig.for_each_trace(lambda t: t.update(
        name=new_names[t.name], legendgroup=new_names[t.name],
        hovertemplate=t.hovertemplate.replace(t.name, new_names[t.name])
    ))

    return fig


def plot_line_graphs() -> None:
    """
    Plot interactive line graph.
    Use the button to switch between different sectors.
    """
    depression_trace = list(create_line_plots('depression').select_traces())
    anxiety_trace = list(create_line_plots('anxiety').select_traces())
    ocd_1_trace = list(create_line_plots('obsessive compulsive disorder').select_traces())
    ocd_2_trace = list(create_line_plots('ocd').select_traces())
    insomnia_trace = list(create_line_plots('insomnia').select_traces())
    panic_attack_trace = list(create_line_plots('panic attack').select_traces())
    mental_health_trace = list(create_line_plots('mental health').select_traces())
    counseling_trace = list(create_line_plots('counseling').select_traces())
    psychiatrist_trace = list(create_line_plots('psychiatrist').select_traces())

    data = depression_trace + anxiety_trace + ocd_1_trace + ocd_2_trace + insomnia_trace +\
        panic_attack_trace + mental_health_trace + counseling_trace + psychiatrist_trace

    updatemenus = [
        dict(active=-1,
             buttons=list([
                 dict(label='Depression',
                      method='update',
                      args=[{'visible':
                            [True, True, True, True, True, True, True,
                             False, False, False, False, False, False, False,
                             False, False, False, False, False, False, False,
                             False, False, False, False, False, False, False,
                             False, False, False, False, False, False, False,
                             False, False, False, False, False, False, False,
                             False, False, False, False, False, False, False,
                             False, False, False, False, False, False, False,
                             False, False, False, False, False, False, False]},
                            {'title': "COVID-19 Impact on Public Attention Toward 'Depression'"}]),

                 dict(label='Anxiety',
                      method='update',
                      args=[{'visible':
                            [False, False, False, False, False, False, False,
                             True, True, True, True, True, True, True,
                             False, False, False, False, False, False, False,
                             False, False, False, False, False, False, False,
                             False, False, False, False, False, False, False,
                             False, False, False, False, False, False, False,
                             False, False, False, False, False, False, False,
                             False, False, False, False, False, False, False,
                             False, False, False, False, False, False, False]},
                            {'title': "COVID-19 Impact on Public Attention Toward 'Anxiety'"}]),

                 dict(label='Obsessive Compulsive Disorder',
                      method='update',
                      args=[{'visible':
                            [False, False, False, False, False, False, False,
                             False, False, False, False, False, False, False,
                             True, True, True, True, True, True, True,
                             False, False, False, False, False, False, False,
                             False, False, False, False, False, False, False,
                             False, False, False, False, False, False, False,
                             False, False, False, False, False, False, False,
                             False, False, False, False, False, False, False,
                             False, False, False, False, False, False, False]},
                            {'title': "COVID-19 Impact on Public Attention Toward "
                                      "'Obsessive Compulsive Disorder'"}]),

                 dict(label='OCD',
                      method='update',
                      args=[{'visible':
                            [False, False, False, False, False, False, False,
                             False, False, False, False, False, False, False,
                             False, False, False, False, False, False, False,
                             True, True, True, True, True, True, True,
                             False, False, False, False, False, False, False,
                             False, False, False, False, False, False, False,
                             False, False, False, False, False, False, False,
                             False, False, False, False, False, False, False,
                             False, False, False, False, False, False, False]},
                            {'title': "COVID-19 Impact on Public Attention Toward 'OCD'"}]),

                 dict(label='Insomnia',
                      method='update',
                      args=[{'visible':
                            [False, False, False, False, False, False, False,
                             False, False, False, False, False, False, False,
                             False, False, False, False, False, False, False,
                             False, False, False, False, False, False, False,
                             True, True, True, True, True, True, True,
                             False, False, False, False, False, False, False,
                             False, False, False, False, False, False, False,
                             False, False, False, False, False, False, False,
                             False, False, False, False, False, False, False]},
                            {'title': "COVID-19 Impact on Public Attention Toward 'Insomnia'"}]),

                 dict(label='Panic Attack',
                      method='update',
                      args=[{'visible':
                            [False, False, False, False, False, False, False,
                             False, False, False, False, False, False, False,
                             False, False, False, False, False, False, False,
                             False, False, False, False, False, False, False,
                             False, False, False, False, False, False, False,
                             True, True, True, True, True, True, True,
                             False, False, False, False, False, False, False,
                             False, False, False, False, False, False, False,
                             False, False, False, False, False, False, False]},
                            {'title': "COVID-19 Impact on Public Attention Toward "
                                      "'Panic Attack'"}]),

                 dict(label='Mental Health',
                      method='update',
                      args=[{'visible':
                            [False, False, False, False, False, False, False,
                             False, False, False, False, False, False, False,
                             False, False, False, False, False, False, False,
                             False, False, False, False, False, False, False,
                             False, False, False, False, False, False, False,
                             False, False, False, False, False, False, False,
                             True, True, True, True, True, True, True,
                             False, False, False, False, False, False, False,
                             False, False, False, False, False, False, False]},
                            {'title': "COVID-19 Impact on Public Attention Toward "
                                      "'Mental Health'"}]),

                 dict(label='Counseling',
                      method='update',
                      args=[{'visible':
                            [False, False, False, False, False, False, False,
                             False, False, False, False, False, False, False,
                             False, False, False, False, False, False, False,
                             False, False, False, False, False, False, False,
                             False, False, False, False, False, False, False,
                             False, False, False, False, False, False, False,
                             False, False, False, False, False, False, False,
                             True, True, True, True, True, True, True,
                             False, False, False, False, False, False, False]},
                            {'title': "COVID-19 Impact on Public Attention Toward 'Counseling'"}]),

                 dict(label='Psychiatrist',
                      method='update',
                      args=[{'visible':
                            [False, False, False, False, False, False, False,
                             False, False, False, False, False, False, False,
                             False, False, False, False, False, False, False,
                             False, False, False, False, False, False, False,
                             False, False, False, False, False, False, False,
                             False, False, False, False, False, False, False,
                             False, False, False, False, False, False, False,
                             False, False, False, False, False, False, False,
                             True, True, True, True, True, True, True]},
                            {'title': "COVID-19 Impact on Public Attention Toward "
                                      "'Psychiatrist'"}])
             ]),
             )
    ]

    layout = dict(title='COVID-19 Impact on Public Attention Toward '
                        'Mental Health Related Search Terms',
                  showlegend=True, updatemenus=updatemenus)

    fig = dict(data=data, layout=layout)
    pio.show(fig)


if __name__ == '__main__':
    import python_ta
    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    python_ta.check_all(config={
        # the names (strs) of imported modules
        'extra-imports': ['plotly.express', 'plotly.io', 'pandas',
                          'openpyxl', 'python_ta.contacts', 'python_ta'],
        # the names (strs) of functions that call print/open/input
        'allowed-io': [],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })
