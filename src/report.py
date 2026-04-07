def generate_report(df, summary, missing, insights_text):
    
    html = f"""
    <html>
    <head>
        <title>Data Analysis Report</title>
        <style>
            body {{ font-family: Arial; padding: 20px; }}
            h1 {{ color: #2c3e50; }}
            h2 {{ color: #34495e; }}
            table {{ border-collapse: collapse; width: 100%; }}
            th, td {{ border: 1px solid #ddd; padding: 8px; }}
        </style>
    </head>
    
    <body>
        <h1>📊 Data Analysis Report</h1>

        <h2>Dataset Shape</h2>
        <p>{df.shape}</p>

        <h2>Missing Values</h2>
        {missing.to_frame(name="Missing Count").to_html()}

        <h2>Statistical Summary</h2>
        {summary.to_html()}

        <h2>Insights</h2>
        <pre>{insights_text}</pre>

    </body>
    </html>
    """

    with open("report.html", "w", encoding="utf-8") as f:
        f.write(html)

    print("\n📄 Report generated: report.html")