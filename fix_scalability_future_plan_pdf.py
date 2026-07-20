import os
from fpdf import FPDF
from fpdf.enums import XPos, YPos

class ScalabilityFuturePlanPDF(FPDF):
    def __init__(self):
        super().__init__(orientation="P", unit="mm", format="A4")
        self.set_margins(15, 15, 15)
        self.set_auto_page_break(auto=True, margin=15)

    def generate(self, output_path):
        self.add_page()
        
        # 1. Header Logos
        logo_left = r"c:\Users\regal\.gemini\antigravity-ide\scratch\ecotrack\docs_assets\perfect_smartbridge_logo.png"
        logo_right = r"c:\Users\regal\.gemini\antigravity-ide\scratch\ecotrack\docs_assets\perfect_skillwallet_logo.png"
        
        if os.path.exists(logo_left):
            self.image(logo_left, x=15, y=10, h=14)
        if os.path.exists(logo_right):
            self.image(logo_right, x=145, y=10, h=14)
            
        self.set_y(32)
        
        # 2. Main Title
        self.set_font("Helvetica", "B", 16)
        self.set_text_color(15, 23, 42)
        self.cell(0, 10, "Scalability & Future Plan Template", border=0, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
        self.ln(3)
        
        # 3. Top Info Table
        top_table_data = [
            ("Date", "29 June 2026"),
            ("Team ID", ""),
            ("Project Name", "EcoTrack - Personal Carbon AI Footprint Tracker"),
            ("Maximum Marks", "1 Mark")
        ]
        
        self.set_draw_color(51, 65, 85)
        self.set_line_width(0.3)
        
        for key, val in top_table_data:
            self.set_fill_color(241, 245, 249)
            self.set_font("Helvetica", "B", 10)
            self.set_text_color(15, 23, 42)
            self.cell(45, 8.5, key, border=1, fill=True, align="L")
            
            self.set_font("Helvetica", "", 10)
            self.set_text_color(30, 41, 59)
            self.cell(135, 8.5, f"  {val}", border=1, fill=False, align="L", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            
        self.ln(5)
        
        # 4. Section Title & Overview
        self.set_font("Helvetica", "B", 11.5)
        self.set_text_color(15, 23, 42)
        self.cell(0, 6, "Scalability & Future Plan", border=0, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="L")
        
        self.set_font("Helvetica", "", 9)
        self.set_text_color(71, 85, 105)
        self.multi_cell(0, 4.5, "Describe how the current solution can scale to handle increased load or users, and outline the features or enhancements planned for future releases.", border=0, align="L")
        self.ln(3)
        
        # 5. Scalability Subsection
        self.set_font("Helvetica", "B", 11)
        self.set_text_color(15, 23, 42)
        self.cell(0, 6, "Scalability", border=0, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="L")
        
        # Scalability Table Headers
        sc_headers = ["Aspect", "Details"]
        sc_widths = [48, 132]
        
        self.set_fill_color(219, 234, 254) # Blue-100 fill
        self.set_font("Helvetica", "B", 9.5)
        self.set_text_color(15, 23, 42)
        
        for i, h in enumerate(sc_headers):
            self.cell(sc_widths[i], 8, h, border=1, align="L", fill=True)
        self.ln()
        
        # Scalability Data Rows
        sc_rows = [
            ("Current Architecture", "Decoupled React.js SPA frontend served via Vite/Vercel with a lightweight Flask Python REST API backend and Firebase Firestore NOSQL cloud database."),
            ("Scalability Approach", "Stateless Flask API deployment on serverless containers, asynchronous Groq LLM proxy requests, automatic Firestore horizontal partitioning, and client-side Chart.js caching."),
            ("Expected Growth / Load", "Designed to scale seamlessly from current prototype capacity up to 10,000+ daily active users (DAU) with sub-200ms API latency and scalable cloud throughput.")
        ]
        
        self.set_font("Helvetica", "", 9)
        self.set_text_color(30, 41, 59)
        
        for idx, (aspect, details) in enumerate(sc_rows):
            # Calculate height needed
            lines_aspect = len(self.multi_cell(sc_widths[0] - 4, 4.5, aspect, dry_run=True, output="LINES"))
            lines_details = len(self.multi_cell(sc_widths[1] - 4, 4.5, details, dry_run=True, output="LINES"))
            max_lines = max(lines_aspect, lines_details)
            row_h = max(8, max_lines * 4.5 + 4)
            
            start_x = self.get_x()
            start_y = self.get_y()
            
            bg_color = (255, 255, 255) if idx % 2 == 0 else (248, 250, 252)
            self.set_fill_color(*bg_color)
            self.rect(start_x, start_y, sum(sc_widths), row_h, "F")
            
            # Aspect cell
            self.rect(start_x, start_y, sc_widths[0], row_h, "D")
            self.set_xy(start_x + 2, start_y + (row_h - (lines_aspect * 4.5)) / 2)
            self.set_font("Helvetica", "B", 9)
            self.multi_cell(sc_widths[0] - 4, 4.5, aspect, border=0, align="L")
            
            # Details cell
            self.rect(start_x + sc_widths[0], start_y, sc_widths[1], row_h, "D")
            self.set_xy(start_x + sc_widths[0] + 2, start_y + (row_h - (lines_details * 4.5)) / 2)
            self.set_font("Helvetica", "", 9)
            self.multi_cell(sc_widths[1] - 4, 4.5, details, border=0, align="L")
            
            self.set_xy(start_x, start_y + row_h)
            
        self.ln(5)
        
        # 6. Future Plan Subsection
        self.set_font("Helvetica", "B", 11)
        self.set_text_color(15, 23, 42)
        self.cell(0, 6, "Future Plan", border=0, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="L")
        
        fp_headers = ["S.No", "Planned Feature / Enhancement", "Target Timeline", "Priority"]
        fp_widths = [14, 94, 42, 30]
        
        self.set_fill_color(254, 243, 199) # Amber-100 fill matching header styling in original
        self.set_font("Helvetica", "B", 9.5)
        self.set_text_color(15, 23, 42)
        
        for i, h in enumerate(fp_headers):
            align_mode = "C" if i in [0, 2, 3] else "L"
            self.cell(fp_widths[i], 8, h, border=1, align=align_mode, fill=True)
        self.ln()
        
        fp_rows = [
            ("1", "Mobile Native Companion Application (React Native / Expo)", "Q3 2026", "High"),
            ("2", "Automated Smart Utility Meter IoT API Integration", "Q4 2026", "High"),
            ("3", "Receipt OCR AI Recognition Scanner for Meal Invoices", "Q4 2026", "Medium"),
            ("4", "Social Leaderboards & Community Carbon Offset Challenges", "Q1 2027", "Medium")
        ]
        
        self.set_font("Helvetica", "", 9)
        self.set_text_color(30, 41, 59)
        
        for idx, row in enumerate(fp_rows):
            lines_title = len(self.multi_cell(fp_widths[1] - 4, 4.5, row[1], dry_run=True, output="LINES"))
            row_h = max(8, lines_title * 4.5 + 4)
            
            start_x = self.get_x()
            start_y = self.get_y()
            
            bg_color = (255, 255, 255) if idx % 2 == 0 else (248, 250, 252)
            self.set_fill_color(*bg_color)
            self.rect(start_x, start_y, sum(fp_widths), row_h, "F")
            
            curr_x = start_x
            for c_idx, val in enumerate(row):
                w = fp_widths[c_idx]
                self.rect(curr_x, start_y, w, row_h, "D")
                
                align = "C" if c_idx in [0, 2, 3] else "L"
                lines = lines_title if c_idx == 1 else 1
                self.set_xy(curr_x if align == "C" else curr_x + 2, start_y + (row_h - (lines * 4.5)) / 2)
                
                w_text = w if align == "C" else w - 4
                self.multi_cell(w_text, 4.5, val, border=0, align=align)
                curr_x += w
                
            self.set_xy(start_x, start_y + row_h)
            
        self.output(output_path)
        print(f"Successfully generated clean Scalability & Future Plan PDF at: {output_path}")

if __name__ == "__main__":
    pdf_gen = ScalabilityFuturePlanPDF()
    target_path = r"c:\Users\regal\.gemini\antigravity-ide\scratch\ecotrack\8. Project Demonstration\Scalability & Future Plan.pdf"
    pdf_gen.generate(target_path)
