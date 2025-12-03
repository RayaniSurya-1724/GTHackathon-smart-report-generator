# GTHackathon-smart-report-generator



📊 ADTech Automated Insights & PDF Report Generator
Turn raw AdTech CSV logs into professional reports with AI-generated summaries, charts, and automated insights.

This project takes a raw advertising dataset and transforms it into a PDF performance report containing:

Data-driven KPIs

Visual charts

An AI-written executive summary

Actionable insights

Powered by Pandas, Matplotlib, Seaborn, ReportLab, and Google Gemini.

🚀 Features
✅ Data Processing

Load and clean large AdTech datasets

Compute essential KPIs such as:

Total impressions

Total revenue

Viewability rate

Revenue share

Viewable vs. measurable impressions

🎨 Data Visualization

Generates high-quality charts:

Impressions Over Time

Revenue by Geo

Saved as .png and embedded into the final report.

🤖 AI-Generated Insights

Uses Gemini 2.0 Flash to create:

Executive summary

Performance insights

Optimization recommendations

📄 Automated PDF Report

Builds a complete PDF using ReportLab, containing:

Title page

Executive summary

KPI table

Charts

AI recommendations

📁 Dataset Format

Your CSV must contain the following columns:

date
site_id
ad_type_id
geo_id
device_category_id
advertiser_id
order_id
line_item_type_id
os_id
integration_type_id
monetization_channel_id
ad_unit_id
total_impressions
total_revenue
viewable_impressions
measurable_impressions
revenue_share_percent

🛠 Installation

Install all dependencies:

pip install pandas matplotlib seaborn reportlab google-generativeai

⚙ Setup Gemini API Key

Get your API key:
👉 https://aistudio.google.com/app/apikey

In adtech_pipeline.py, configure it:

genai.configure(api_key="YOUR_API_KEY_HERE")

▶ How to Run

Run the main script:

python app.py


This will:

Load the dataset

Compute insights

Generate AI executive summary

Create charts

Produce a professional PDF report

The final output will be saved as:

ADTech_Report.pdf

📄 Output Contents

Your generated report includes:

Title Page

AI-Generated Executive Summary

Key Metrics Table

Charts (PNG embedded)

AI Recommendations & Observations

🧩 Project Structure

/project-folder
│
├── app.py  
# Main entry point
├── adtech_pipeline.py    
# Full data → insights → charts → PDF workflow
├── dataset.csv       
# Input dataset
├── impressions_over_time.png

├── revenue_by_geo.png

└── ADTech_Report.pdf      # Final report (auto-generated)

🤝 Contributions

Contributions are welcome!
You can improve:

KPIs

Visualizations

Report design

Multi-report automation

AI prompt quality
