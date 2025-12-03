import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
import google.generativeai as genai


class ADTechPipeline:

    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.df = None
        self.styles = getSampleStyleSheet()

    # -------------------------------------------------------------
    # STEP 1 — Load Data
    # -------------------------------------------------------------
    def load_data(self):
        print("📥 Loading dataset...")

        self.df = pd.read_csv(self.csv_path)

        # Fix: parse date safely for your dataset
        self.df["date"] = pd.to_datetime(
            self.df["date"],
            dayfirst=True,
            errors="coerce"
        )

        print("✔ Loaded", len(self.df), "rows")

    # -------------------------------------------------------------
    # STEP 2 — Compute AD-Tech Metrics
    # -------------------------------------------------------------
    def compute_insights(self):
        print("📊 Computing insights...")

        insights = {
            "Total Impressions": int(self.df["total_impressions"].sum()),
            "Total Revenue": float(self.df["total_revenue"].sum()),
            "Average Revenue Share %": float(self.df["revenue_share_percent"].mean()),
            "Total Viewable Impressions": int(self.df["viewable_impressions"].sum()),
            "Total Measurable Impressions": int(self.df["measurable_impressions"].sum()),
            "Viewability Rate (%)": (
                self.df["viewable_impressions"].sum()
                / max(self.df["measurable_impressions"].sum(), 1)
            ) * 100
        }

        return insights

    # -------------------------------------------------------------
    # STEP 3 — AI Narrative Generation (LATEST GEMINI API)
    # -------------------------------------------------------------
    # -------------------------------------------------------------
    # STEP 3 — AI Narrative Generation (with Bold Formatting)
    # -------------------------------------------------------------
    def generate_ai_summary(self, insights):
        print("🤖 Generating AI insights...")

        prompt = f"""
        You are an expert AdTech analyst. Write a highly professional executive summary.

        Use this formatting:
        - For bold text, ALWAYS wrap with double asterisks like **this**.
        - Do NOT use HTML tags.

        Base the summary on these metrics:

        - Total Impressions: {insights["Total Impressions"]}
        - Total Revenue: {insights["Total Revenue"]:.2f}
        - Average Revenue Share %: {insights["Average Revenue Share %"]:.2f}%
        - Viewability Rate (%): {insights["Viewability Rate (%)"]:.2f}%
        - Viewable Impressions: {insights["Total Viewable Impressions"]}
        - Measurable Impressions: {insights["Total Measurable Impressions"]}

        Provide key trends, insights, and actionable recommendations.
        """

        genai.configure(api_key="AIzaSyCzUeHUqDc8UE1QfnpqOUqD_E8hfJ7GLdo")

        model = genai.GenerativeModel("models/gemini-2.0-flash")

        response = model.generate_content([prompt])
        text = response.text

        # Convert **bold** markdown → <b>bold</b>
        import re
        text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)

        return text


    # -------------------------------------------------------------
    # STEP 4 — Generate Charts
    # -------------------------------------------------------------
    def generate_figures(self):
        print("📈 Creating charts...")

        # Impressions over time
        plt.figure(figsize=(8, 4))
        sns.lineplot(data=self.df, x="date", y="total_impressions")
        plt.title("Total Impressions Over Time")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig("impressions_over_time.png")
        plt.close()

        # Revenue by Geo
        plt.figure(figsize=(8, 4))
        sns.barplot(
            data=self.df.groupby("geo_id")["total_revenue"].sum().reset_index(),
            x="geo_id", y="total_revenue"
        )
        plt.title("Revenue by Geo")
        plt.tight_layout()
        plt.savefig("revenue_by_geo.png")
        plt.close()

        return ["impressions_over_time.png", "revenue_by_geo.png"]

    # -------------------------------------------------------------
    # STEP 5 — Generate PDF Report
    # -------------------------------------------------------------
    def generate_pdf(self, insights, narrative, figures):
        print("📄 Generating PDF report...")

        pdf = SimpleDocTemplate("ADTech_Report.pdf", pagesize=letter)
        content = []

        content.append(Paragraph("📊 AD-Tech Performance Report", self.styles["Title"]))
        content.append(Spacer(1, 12))

        content.append(Paragraph("Executive Summary", self.styles["Heading1"]))
        content.append(Paragraph(narrative, self.styles["BodyText"]))
        content.append(Spacer(1, 12))

        content.append(Paragraph("Key Metrics", self.styles["Heading1"]))
        for key, value in insights.items():
            content.append(Paragraph(f"<b>{key}:</b> {value}", self.styles["BodyText"]))
        content.append(Spacer(1, 12))

        content.append(Paragraph("Visual Insights", self.styles["Heading1"]))
        for fig in figures:
            content.append(Image(fig, width=400, height=240))
            content.append(Spacer(1, 12))

        pdf.build(content)
        print("✔ PDF generated!")

    # -------------------------------------------------------------
    # END-TO-END RUNNER
    # -------------------------------------------------------------
    def run(self):
        self.load_data()
        insights = self.compute_insights()
        narrative = self.generate_ai_summary(insights)
        figures = self.generate_figures()
        self.generate_pdf(insights, narrative, figures)
        return "ADTech_Report.pdf"
