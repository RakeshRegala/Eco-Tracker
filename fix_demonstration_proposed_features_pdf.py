import os
from fpdf import FPDF
from fpdf.enums import XPos, YPos

class DemonstrationProposedFeaturesPDF(FPDF):
    def __init__(self):
        super().__init__(orientation="P", unit="mm", format="A4")
        self.set_margins(15, 12, 15)
        self.set_auto_page_break(auto=True, margin=12)

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
        self.cell(0, 10, "Demonstration of Proposed Features", border=0, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
        self.ln(3)
        
        # 3. Top Info Table
        top_table_data = [
            ("Date", "30 June 2026"),
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
        
        # 4. Section Title & Description
        self.set_font("Helvetica", "B", 11.5)
        self.set_text_color(15, 23, 42)
        self.cell(0, 6, "Demonstration of Proposed Features", border=0, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="L")
        
        self.set_font("Helvetica", "", 9)
        self.set_text_color(71, 85, 105)
        self.multi_cell(0, 4.5, "List each feature proposed in the solution and confirm whether it was demonstrated in the final project, along with supporting evidence and remarks.", border=0, align="L")
        self.ln(4)
        
        # 5. Table Headers
        headers = ["S.No", "Proposed Feature", "Demonstrated", "Screenshot / Evidence", "Remarks"]
        col_widths = [12, 52, 24, 44, 48]
        
        self.set_fill_color(219, 234, 254) # Blue-100 fill
        self.set_font("Helvetica", "B", 9)
        self.set_text_color(15, 23, 42)
        
        header_h = 8.5
        start_x = self.get_x()
        start_y = self.get_y()
        
        for i, h in enumerate(headers):
            w = col_widths[i]
            align_mode = "C" if i in [0, 2] else "L"
            self.rect(start_x, start_y, w, header_h, "DF")
            
            self.set_xy(start_x if align_mode == "C" else start_x + 2, start_y + (header_h - 4) / 2)
            w_text = w if align_mode == "C" else w - 4
            self.multi_cell(w_text, 4, h, border=0, align=align_mode)
            start_x += w
            
        self.set_xy(15, start_y + header_h)
        
        # Rows Data
        rows_data = [
            ("1", "Multi-Category Daily Habit Logger (Travel, Food, Energy)", "Yes", "Vercel Live App (/logger)", "Fully functional multi-step wizard with real-time carbon footprint preview calculations"),
            ("2", "Dynamic Carbon Footprint Gauge & Daily Budget Indicator", "Yes", "Dashboard Gauge Widget", "Renders carbon footprint gauge vs daily budget dynamically on home screen"),
            ("3", "Groq LLaMA 3.3 AI Lifestyle Swap Generator", "Yes", "Suggestions Engine (/suggestions)", "Generates 3 personalized eco-friendly lifestyle swaps with estimated CO2 savings"),
            ("4", "30-Day Historical Emissions Analytics (Chart.js)", "Yes", "History Analytics Charts (/history)", "Renders 30-day line trend vs budget, 14-day stacked bar breakdown, and heatmap calendar"),
            ("5", "Gamification Engine (Logging Streaks & 10 Badges)", "Yes", "Achievements Shelf (/achievements)", "Tracks consecutive logging streaks and automatically unlocks badge achievements"),
            ("6", "Firebase Firestore Cloud Persistence & Auth Sync", "Yes", "Firebase Auth & Firestore DB", "Secure JWT token authentication, cloud daily habit persistence, and Demo Mode fallback")
        ]
        
        self.set_font("Helvetica", "", 8.5)
        self.set_text_color(30, 41, 59)
        
        for idx, row in enumerate(rows_data):
            lines_col1 = len(self.multi_cell(col_widths[1] - 4, 4, row[1], dry_run=True, output="LINES"))
            lines_col3 = len(self.multi_cell(col_widths[3] - 4, 4, row[3], dry_run=True, output="LINES"))
            lines_col4 = len(self.multi_cell(col_widths[4] - 4, 4, row[4], dry_run=True, output="LINES"))
            max_lines = max(lines_col1, lines_col3, lines_col4, 1)
            row_h = max(8, max_lines * 4 + 3.5)
            
            start_x = self.get_x()
            start_y = self.get_y()
            
            bg_color = (255, 255, 255) if idx % 2 == 0 else (248, 250, 252)
            self.set_fill_color(*bg_color)
            self.rect(start_x, start_y, sum(col_widths), row_h, "F")
            
            curr_x = start_x
            for c_idx, val in enumerate(row):
                w = col_widths[c_idx]
                self.rect(curr_x, start_y, w, row_h, "D")
                
                align = "C" if c_idx in [0, 2] else "L"
                lines = 1
                if c_idx == 1: lines = lines_col1
                elif c_idx == 3: lines = lines_col3
                elif c_idx == 4: lines = lines_col4
                
                self.set_xy(curr_x if align == "C" else curr_x + 2, start_y + (row_h - (lines * 4)) / 2)
                w_text = w if align == "C" else w - 4
                
                if c_idx == 2:
                    self.set_font("Helvetica", "B", 8.5)
                    self.set_text_color(16, 185, 129) # Emerald-500 for "Yes"
                else:
                    self.set_font("Helvetica", "", 8.5)
                    self.set_text_color(30, 41, 59)
                    
                self.multi_cell(w_text, 4, val, border=0, align=align)
                curr_x += w
                
            self.set_xy(start_x, start_y + row_h)
            
        self.output(output_path)
        print(f"Successfully generated clean Demonstration of Proposed Features PDF at: {output_path}")

if __name__ == "__main__":
    pdf_gen = DemonstrationProposedFeaturesPDF()
    target_path = r"c:\Users\regal\.gemini\antigravity-ide\scratch\ecotrack\8. Project Demonstration\Demonstration of Proposed Features.pdf"
    pdf_gen.generate(target_path)
