import os
from fpdf import FPDF
from fpdf.enums import XPos, YPos

class ProjectDemoPlanningPDF(FPDF):
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
            self.image(logo_left, x=15, y=8, h=13)
        if os.path.exists(logo_right):
            self.image(logo_right, x=145, y=8, h=13)
            
        self.set_y(28)
        
        # 2. Main Title
        self.set_font("Helvetica", "B", 15)
        self.set_text_color(15, 23, 42)
        self.cell(0, 8, "Project Demo Planning Template", border=0, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
        self.ln(2)
        
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
            self.set_font("Helvetica", "B", 9.5)
            self.set_text_color(15, 23, 42)
            self.cell(42, 7.5, key, border=1, fill=True, align="L")
            
            self.set_font("Helvetica", "", 9.5)
            self.set_text_color(30, 41, 59)
            self.cell(138, 7.5, f"  {val}", border=1, fill=False, align="L", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            
        self.ln(4)
        
        # 4. Section Title & Description
        self.set_font("Helvetica", "B", 11)
        self.set_text_color(15, 23, 42)
        self.cell(0, 5, "Project Demo Planning", border=0, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="L")
        
        self.set_font("Helvetica", "", 8.5)
        self.set_text_color(71, 85, 105)
        self.multi_cell(0, 4, "Plan the flow of the final project demo - list out the modules/features to be shown, what will be demonstrated for each, who will present it, and the time allotted, so the demo runs smoothly within the available time.", border=0, align="L")
        self.ln(3)
        
        # 5. Main Planning Table Headers
        headers = ["S.No", "Module / Feature\nto be Demonstrated", "What will be Shown", "Demonstrated\nBy", "Time\nAllotted"]
        col_widths = [11, 48, 56, 40, 25]
        
        self.set_fill_color(219, 234, 254) # Blue-100 fill
        self.set_font("Helvetica", "B", 8.5)
        self.set_text_color(15, 23, 42)
        
        header_h = 9
        start_x = self.get_x()
        start_y = self.get_y()
        
        for i, h in enumerate(headers):
            w = col_widths[i]
            align_mode = "C" if i in [0, 4] else "L"
            
            # Draw header cell background and border
            self.rect(start_x, start_y, w, header_h, "DF")
            
            lines = h.split("\n")
            line_count = len(lines)
            self.set_xy(start_x if align_mode == "C" else start_x + 1.5, start_y + (header_h - (line_count * 3.8)) / 2)
            w_text = w if align_mode == "C" else w - 3
            self.multi_cell(w_text, 3.8, h, border=0, align=align_mode)
            start_x += w
            
        self.set_xy(15, start_y + header_h)
        
        # Main Planning Rows Data
        rows_data = [
            ("1", "Daily Habit Logger & Multi-Step Wizard", "Multi-step habit entry form (Travel, Food, Energy) with real-time footprint preview calculations", "Regala Rakesh", "15 Mins"),
            ("2", "Groq LLaMA 3.3 AI Lifestyle Swap Generator", "Personalized eco swap recommendations generation using Groq API and robust JSON parser", "Sri Dhruthi Mallela", "15 Mins"),
            ("3", "30-Day Historical Analytics & Chart.js Rendering", "30-day line trend vs budget, 14-day stacked bar breakdown, and 30-day activity heatmap calendar", "P L P D Sravanthi Murukuri", "15 Mins"),
            ("4", "Streaks Engine & Gamification Badges Catalog", "Daily streak counter, achievements evaluation matrix, and unlockable badge modals", "Manikanta Cherukuri", "15 Mins"),
            ("5", "Backend REST API & Carbon Interface Gateway", "Flask API endpoints, Firebase Auth middleware verification, and Carbon Interface API proxy", "Thokala Charan", "15 Mins")
        ]
        
        self.set_font("Helvetica", "", 8.5)
        self.set_text_color(30, 41, 59)
        
        for idx, row in enumerate(rows_data):
            # Calculate height needed
            lines_col1 = len(self.multi_cell(col_widths[1] - 3, 4, row[1], dry_run=True, output="LINES"))
            lines_col2 = len(self.multi_cell(col_widths[2] - 3, 4, row[2], dry_run=True, output="LINES"))
            lines_col3 = len(self.multi_cell(col_widths[3] - 3, 4, row[3], dry_run=True, output="LINES"))
            max_lines = max(lines_col1, lines_col2, lines_col3, 1)
            row_h = max(7.5, max_lines * 4 + 3.5)
            
            start_x = self.get_x()
            start_y = self.get_y()
            
            bg_color = (255, 255, 255) if idx % 2 == 0 else (248, 250, 252)
            self.set_fill_color(*bg_color)
            self.rect(start_x, start_y, sum(col_widths), row_h, "F")
            
            curr_x = start_x
            for c_idx, val in enumerate(row):
                w = col_widths[c_idx]
                self.rect(curr_x, start_y, w, row_h, "D")
                
                align = "C" if c_idx in [0, 4] else "L"
                lines = 1
                if c_idx == 1: lines = lines_col1
                elif c_idx == 2: lines = lines_col2
                elif c_idx == 3: lines = lines_col3
                
                self.set_xy(curr_x if align == "C" else curr_x + 1.5, start_y + (row_h - (lines * 4)) / 2)
                w_text = w if align == "C" else w - 3
                self.multi_cell(w_text, 4, val, border=0, align=align)
                curr_x += w
                
            self.set_xy(start_x, start_y + row_h)
            
        # Total Duration Row
        self.set_fill_color(241, 245, 249)
        self.set_font("Helvetica", "B", 9)
        self.set_text_color(15, 23, 42)
        total_w = sum(col_widths[:4])
        self.cell(total_w, 7.5, "Total Demo Duration", border=1, align="R", fill=True)
        self.cell(col_widths[4], 7.5, "75 Mins", border=1, align="C", fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        
        self.ln(4)
        
        # 6. Demo Logistics Section
        self.set_font("Helvetica", "B", 11)
        self.set_text_color(15, 23, 42)
        self.cell(0, 5, "Demo Logistics", border=0, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="L")
        self.ln(1)
        
        logistics_data = [
            ("Demo Platform / Tool", "Vercel Live App (https://eco-tracker-tan.vercel.app/) & Google Drive Video"),
            ("Demo Date & Time", "29 June 2026, 10:00 AM IST"),
            ("Recording / Demo Video Link", "https://drive.google.com/file/d/1CufYmVf8ybdpfGAxnU9Mqqxqe81F3eAK/view?usp=drivesdk"),
            ("Backup Plan (in case of technical issues)", "Pre-recorded HD video demo on Google Drive, local Flask + Vite fallback environment, and in-memory Demo Mode.")
        ]
        
        for idx, (label, val_text) in enumerate(logistics_data):
            lines_val = len(self.multi_cell(132 - 3, 4, val_text, dry_run=True, output="LINES"))
            row_h = max(7.5, lines_val * 4 + 3)
            
            start_x = self.get_x()
            start_y = self.get_y()
            
            bg_color = (255, 255, 255) if idx % 2 == 0 else (248, 250, 252)
            self.set_fill_color(*bg_color)
            self.rect(start_x, start_y, 180, row_h, "F")
            
            # Label Cell
            self.rect(start_x, start_y, 48, row_h, "D")
            self.set_xy(start_x + 2, start_y + (row_h - 4) / 2)
            self.set_font("Helvetica", "B", 8.5)
            self.set_text_color(15, 23, 42)
            self.multi_cell(44, 4, label, border=0, align="L")
            
            # Value Cell
            self.rect(start_x + 48, start_y, 132, row_h, "D")
            self.set_xy(start_x + 50, start_y + (row_h - (lines_val * 4)) / 2)
            self.set_font("Helvetica", "", 8.5)
            self.set_text_color(30, 41, 59)
            
            # Render with link formatting if text is URL or contains URL
            if val_text.startswith("http"):
                self.set_text_color(37, 99, 235) # Blue-600 link color
                self.cell(128, 4, val_text, border=0, link=val_text)
            else:
                self.multi_cell(128, 4, val_text, border=0, align="L")
                
            self.set_xy(start_x, start_y + row_h)
            
        self.output(output_path)
        print(f"Successfully generated clean Project Demo Planning PDF at: {output_path}")

if __name__ == "__main__":
    pdf_gen = ProjectDemoPlanningPDF()
    target_path = r"c:\Users\regal\.gemini\antigravity-ide\scratch\ecotrack\8. Project Demonstration\Project Demo Planning Template.pdf"
    pdf_gen.generate(target_path)
