from pathlib import Path
import pandas as pd
from shiny.express import input, render, ui
from shinyswatch import theme

ui.page_opts(title="Hmass Dashboard", fillable=True)
# theme.minty()
# theme.cerulean()

with ui.sidebar(open="desktop"):
    ui.h2("Sidebar")
    ui.tags.hr()
    ui.h3("Interaction")
    ui.input_text("name_input", "Enter your name", placeholder="Your Name")

    ui.tags.hr()
    ui.h3("Links")
    ui.a("PyShiny", href="https://shiny.posit.co/py/", target="_blank")
    ui.a("Examples", href="https://shinylive.io/py/examples/", target="_blank")
    ui.a("Themes", href="https://posit-dev.github.io/py-shinyswatch/", target="_blank")
    ui.a("Deploy", href="https://docs.posit.co/shinyapps.io/getting-started.html#working-with-shiny-for-python", target="_blank")
   
   
with ui.layout_columns(fill=False):       
    ui.h2("Captsone: English Premier League Standings ")
 
  
@render.text
def welcome_output():
    user = input.name_input();
    welcome_string = f'Greetings {user}!';
    return welcome_string


@render.data_frame
def csv_output():
        # Read CSV reactively (you can change the path to your actual CSV file)
        infile = Path(__file__).parent / "English_Premier_League_standings.csv"
        df = pd.read_csv(infile)
        return df  # Render CSV data as a DataFrame