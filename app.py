from pathlib import Path
import pandas as pd
from shiny import App, render, ui, reactive
import shinyswatch

# Load the data
@reactive.calc
def dat():
    infile = Path(__file__).parent / "English_Premier_League_standings.csv"
    return pd.read_csv(infile)

# Create the UI
app_ui = ui.page_fluid(
    # Add a title
    ui.h1("English Premier League Standings"),

    # Add navigation (tabs)
    ui.navset_tab(
        ui.nav("Data frame", render.render_data_frame(dat)),  # Data frame tab
        ui.nav("Table", render.render_table(dat)),  # Table tab
        ui.nav("Summary", render.render_table(dat().describe())),  # Summary tab
    ),
    
)

# Define the server logic
def server(input, output, session):
    pass  # No additional server logic is needed for this example

# Create the Shiny app
app = App(app_ui, server)

# Run the app
if __name__ == "__main__":
    app.run()