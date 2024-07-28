import requests
import plotly.graph_objects as go

api_key = "020088dca7e2ad48aae9c69cf05504a5"

url = f"https://api.stlouisfed.org/fred/series/observations?series_id=RIFLPBCIANM72NM&api_key={api_key}&file_type=json"

response = requests.get(url)
data = response.json()

if 'observations' in data:
    observations = data['observations']
    dates = [obs['date'] for obs in observations]
    values = [obs['value'] for obs in observations]

    # Define Barbie color theme
    barbie_pink = '#FF69B4'
    barbie_background = '#FFE1E6'
    barbie_text = '#740A55'

    # Set Plotly template with Barbie colors
    template = go.layout.Template()
    template.layout = go.Layout(
        title={'text': '<b style="font-size:24px; color:' + barbie_text + ';">Sofia Starinnova\'s Dashboard</b><br><b style="font-size:18px; color:' + barbie_text + ';">Finance Rate on Consumer Installment Loans at Commercial Banks, New Autos 72 Month Loan (RIFLPBCIANM72NM)</b>', 'font': {'color': barbie_text}},
        plot_bgcolor=barbie_background,
        paper_bgcolor=barbie_background,
        xaxis=dict(title='Date', tickfont=dict(color=barbie_text)),
        yaxis=dict(title='Value', tickfont=dict(color=barbie_text)),
    )

    fig = go.Figure()
    fig.add_trace(go.Bar(x=dates, y=values, marker_color=barbie_pink, name='RIFLPBCIANM72NM'))
    fig.update_layout(template=template)
    fig.show()
else:
    print("Error fetching data from FRED API")
