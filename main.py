import plotly.express as px
import chart_studio.tools as tls
import plotly.io as pio

gapminder = px.data.gapminder()
fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
           hover_name="country", log_x=True, size_max=60)
pio.write_html(fig, file='index.html', auto_open=True)

fig.show()