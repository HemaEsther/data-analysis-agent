def generate_report(df, summary, missing, insights_text, plot_paths):

    images_html = ""
    for path in plot_paths:
        images_html += f'<img src="{path}" class="plot"><br>'

    html = f"""
    <html>
    <head>
        <title>Data Analysis Dashboard</title>
        
        <style>
            body {{
                font-family: 'Segoe UI', sans-serif;
                background-color: #f4f6f8;
                margin: 0;
                padding: 0;
            }}

            .container {{
                padding: 20px;
            }}

            h1 {{
                text-align: center;
                color: #2c3e50;
            }}

            .card {{
                background: white;
                padding: 20px;
                margin: 20px 0;
                border-radius: 12px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }}

            .section-title {{
                font-size: 20px;
                margin-bottom: 10px;
                color: #34495e;
            }}

            table {{
                border-collapse: collapse;
                width: 100%;
                font-size: 14px;
            }}

            th, td {{
                border: 1px solid #ddd;
                padding: 8px;
                text-align: center;
            }}

            th {{
                background-color: #2c3e50;
                color: white;
            }}

            .plot {{
                width: 600px;
                margin: 10px 0;
                border-radius: 10px;
            }}

            .highlight {{
                font-size: 18px;
                color: #16a085;
            }}

            pre {{
                background: #ecf0f1;
                padding: 15px;
                border-radius: 10px;
                overflow-x: auto;
            }}
        </style>
    </head>

    <body>
        <div class="container">

            <h1>📊 Data Analysis Dashboard</h1>

            <div class="card">
                <div class="section-title">📌 Dataset Overview</div>
                <p class="highlight">Shape: {df.shape}</p>
            </div>

            <div class="card">
                <div class="section-title">🧾 Missing Values</div>
                {missing.to_frame(name="Missing").to_html()}
            </div>

            <div class="card">
                <div class="section-title">📊 Statistical Summary</div>
                {summary.to_html()}
            </div>

            <div class="card">
                <div class="section-title">📈 Visualizations</div>
                {images_html}
            </div>

            <div class="card">
                <div class="section-title">🧠 Insights & Recommendations</div>
                <pre>{insights_text}</pre>
            </div>

        </div>
    </body>
    </html>
    """

    import os
    os.makedirs("reports", exist_ok=True)

    with open("reports/report.html", "w", encoding="utf-8") as f:
        f.write(html)

    print("📄 Professional dashboard report generated!")