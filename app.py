from pathlib import Path
import pandas as pd
from shiny import reactive
import shinyswatch
from shiny.express import render, ui

# Load the data
@reactive.calc
def dat():
    infile = Path(__file__).parent / "English_Premier_League_standings.csv"
    return pd.read_csv(infile)

# UI for the app
with ui.navset_card_underline():

    # Title and theme
    ui.title("Capstone: English Premier League Standings")
    ui.theme("journal")  # You can choose other themes like "cosmo", "darkly", "sandstone", etc.

    # First Tab: Data frame
    with ui.nav_panel("Data frame"):
        @render.data_frame
        def frame():
            # Display the dataframe using dat()
            return dat()

    # Second Tab: Table
    with ui.nav_panel("Table"):
        @render.table
        def table():
            # Display the raw data as a table
            return dat()

    # Third Tab: Summary
    with ui.nav_panel("Summary"):
        @render.table
        def summary_table():
            # Generate and display a summary of the dataset (e.g., basic statistics)
            return dat().describe()