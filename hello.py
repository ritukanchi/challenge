from preswald import text, plotly, connect, get_df, table, query
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff

text("# Welcome to Preswald!")
text("This is your first app. 🎉")

connect()  
df = get_df('sample_csv')

#* Top 10 Games by Global Sale Numbers
sql = "SELECT Name, Global_Sales FROM sample_csv ORDER BY Global_Sales DESC LIMIT 10"
df_top_games = query(sql, "sample_csv")

text("# Top 10 Best-Selling Games Globally")
fig_bar = px.bar(df_top_games, x='Name', y='Global_Sales', title='Top 10 Games By Global Sales')
plotly(fig_bar)

#* Regional Sales by Platform
text("# Regional Sales by Platform")
df_platform_sales = df.groupby('Platform')[['NA_Sales', 'EU_Sales', 'JP_Sales']].sum().reset_index()
fig_platform = px.bar(df_platform_sales, x='Platform', y=['NA_Sales', 'EU_Sales', 'JP_Sales'],
                      title='Regional Sales by Platform', barmode='group')
plotly(fig_platform)

#* Global Sales by Genre
text("# Global Sales by Genre")
df_genre_sales = df.groupby('Genre')['Global_Sales'].sum().reset_index().sort_values(by='Global_Sales', ascending=False)
fig_genre = px.bar(df_genre_sales, x='Genre', y='Global_Sales', title='Global Sales by Genre')
plotly(fig_genre)

#* Game Release Trend by Year
text("# Game Releases Over the Years")
df_yearly = df.groupby('Year')['Name'].count().reset_index(name='Game_Count')
fig_yearly = px.line(df_yearly, x='Year', y='Game_Count', title='Number of Games Released Per Year')
plotly(fig_yearly)

#* Correlation Heatmap
text("# Correlation Between Sales Regions")
corr = df[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']].corr()
fig_corr = ff.create_annotated_heatmap(z=corr.values,
                                       x=corr.columns.tolist(),
                                       y=corr.columns.tolist(),
                                       colorscale='Blues',
                                       showscale=True)
plotly(fig_corr)

#* Scatter plot: NA_Sales vs Global_Sales
text("# NA Sales vs Global Sales")
fig_scatter = px.scatter(df, x='NA_Sales', y='Global_Sales', text='Global_Sales',
                         title='NA Sales vs Global Sales',
                         labels={'NA_Sales': 'NA Sales', 'Global_Sales': 'Global Sales'})
fig_scatter.update_traces(textposition='top center', marker=dict(size=12, color='lightblue'))
fig_scatter.update_layout(template='plotly_white')
plotly(fig_scatter)

#* Display the whole table
text("# Full Dataset")
table(df)
