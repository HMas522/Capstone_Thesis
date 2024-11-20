from pathlib import Path
import pandas as pd
from shiny import reactive
from shiny.express import render, ui

# Load the data from the CSV file
@reactive.calc
def dat():
    infile = Path(__file__).parent / "English_Premier_League_standings.csv"
    return pd.read_csv(infile)

# Define the UI layout
with ui.page_fluid(
    ui.title("Capstone: English Premier League Standings")  # Add the title to the app
):
    with ui.navset_card_underline():

        # Data Frame Tab
        with ui.nav_panel("Data frame"):
            @render.data_frame
            def frame():
                # Render the dataframe (this is the first tab)
                return dat()

        # Table Tab
        with ui.nav_panel("Table"):
            @render.table
            def table():
                # Render the data in a table format (second tab)
                return dat()