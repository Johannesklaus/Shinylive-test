from shiny import *

app_ui = ui.page_fluid(
    ui.tags.h1("Hello World!"),
    ui.input_numeric("n1", "First Number", value=0),
    ui.input_numeric("n2", "Second Number", value=0),
    ui.output_text("result"),
)

def server(input, output, session):
    @output
    @render.text
    def result():
        # Check if either input is None and handle appropriately
        if input.n1() is None or input.n2() is None:
            return "Please enter both numbers."
        return f"The sum is: {input.n1() + input.n2()}"

app = App(app_ui, server)
