"""
CSC110 Final Project

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.
"""
import plotly.express as px


def plot_line_graph(search_term_interest: dict) -> None:
    """
    Plot a line graph based on the search_term_interest data.
    """
    week = search_term_interest['week']
    japan = search_term_interest['japan']
    italy = search_term_interest['italy']
    canada = search_term_interest['canada']
    iran = search_term_interest['iran']
    uk = search_term_interest['uk']
    sk = search_term_interest['south_korea']
    us = search_term_interest['us']

    fig = px.line(x=week, y=[japan, italy, canada, iran, uk, sk, us], labels={
        'value': 'search term frequency', 'x': 'week', 'variable': 'country', 'country': 'japan',
        'wide_variable_1': 'italy', 'wide_variable_2': 'canada', 'wide_variable_3': 'iran', 'wide_variable_4': 'uk',
        'wide_variable_5': 'south_korea', 'wide_variable_6': 'us'},
                  title='COVID-19 Impact on Public Attention Toward Mental Health')
    fig.show()
