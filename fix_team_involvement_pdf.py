import os
from fpdf import FPDF
from fpdf.enums import XPos, YPos

class TeamInvolvementPDF(FPDF):
    def __init__(self):
        super().__init__(orientation="P", unit="mm", format="A4")
        self.set_margins(15, 15, 15)
        self.set_auto_page_break(auto=True, margin=15)

    def generate(self, output_path):
        self.add_page()
        
        # 1. Header Logos
        logo_left = r"c:\Users\regal\.gemini\antigravity-ide\scratch\ecotrack\docs_assets\perfect_smartbridge_logo.png" # SmartBridge
        logo_right = r"c:\Users\regal\.gemini\antigravity-ide\scratch\ecotrack\docs_assets\perfect_skillwallet_logo.png" # SkillWallet
        
        if os.path.exists(logo_left):
            self.image(logo_left, x=15, y=10, h=14)
        if os.path.exists(logo_right):
            self.image(logo_right, x=145, y=10, h=14)
            
        self.set_y(33)
        
        # 2. Main Title
        self.set_font("Helvetica", "B", 16)
        self.set_text_color(15, 23, 42) # Slate-900
        self.cell(0, 10, "Team Involvement in Demonstration Template", border=0, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
        self.ln(4)
        
        # 3. Top Info Table
        top_table_data = [
            ("Date", "30 June 2026"),
            ("Team ID", ""),
            ("Project Name", "EcoTrack - Personal Carbon AI Footprint Tracker"),
            ("Maximum Marks", "1 Mark")
        ]
        
        self.set_draw_color(51, 65, 85) # Dark slate border
        self.set_line_width(0.3)
        
        for key, val in top_table_data:
            start_y = self.get_y()
            # Key Column
            self.set_fill_color(241, 245, 249) # Slate-100 background
            self.set_font("Helvetica", "B", 10)
            self.set_text_color(15, 23, 42)
            self.cell(45, 9, key, border=1, fill=True, align="L")
            
            # Value Column
            self.set_font("Helvetica", "", 10)
            self.set_text_color(30, 41, 59)
            self.cell(135, 9, f"  {val}", border=1, fill=False, align="L", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            
        self.ln(8)
        
        # 4. Section Title & Description
        self.set_font("Helvetica", "B", 12)
        self.set_text_color(15, 23, 42)
        self.cell(0, 7, "Team Involvement in Demonstration", border=0, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="L")
        
        self.set_font("Helvetica", "", 9.5)
        self.set_text_color(71, 85, 105)
        self.multi_cell(0, 5, "List every team member who took part in the final project demonstration, the module/feature they presented, and their role in the team.", border=0, align="L")
        self.ln(4)
        
        # 5. Main Table Headers
        headers = ["S.No", "Team Member Name", "Role in Team", "Module / Feature Demonstrated", "Remarks"]
        col_widths = [14, 44, 43, 55, 24]
        
        self.set_fill_color(219, 234, 254) # Blue-100 fill
        self.set_font("Helvetica", "B", 9.5)
        self.set_text_color(15, 23, 42)
        
        for i, h in enumerate(headers):
            align_mode = "C" if i in [0, 4] else "L"
            self.cell(col_widths[i], 9, h if align_mode == "L" else h, border=1, align=align_mode, fill=True)
        self.ln()
        
        # 6. Main Table Rows
        rows_data = [
            ("1", "Regala Rakesh", "Team Lead & Full Stack Engineer", "Daily Habit Logger & Multi-Step Wizard", "Completed"),
            ("2", "Sri Dhruthi Mallela", "AI & Logic Engineer", "Groq LLaMA 3.3 AI Lifestyle Swap Generator", "Completed"),
            ("3", "P L P D Sravanthi Murukuri", "Data & Analytics Lead", "30-Day Historical Analytics & Chart.js Rendering", "Completed"),
            ("4", "Manikanta Cherukuri", "Gamification & Frontend Engineer", "Streaks Engine & Gamification Badges Catalog", "Completed"),
            ("5", "Thokala Charan", "Systems & API Integration Engineer", "Backend REST API & Carbon Interface Gateway", "Completed")
        ]
        
        self.set_font("Helvetica", "", 9)
        self.set_text_color(30, 41, 59)
        
        for idx, row in enumerate(rows_data):
            # Calculate required height for this row based on text length
            # Col 1: 14mm, Col 2: 44mm, Col 3: 43mm, Col 4: 55mm, Col 5: 24mm
            # Check maximum lines required
            line_counts = [
                1,
                len(self.multi_cell(col_widths[1] - 2, 4.5, row[1], dry_run=True, output="LINES")),
                len(self.multi_cell(col_widths[2] - 2, 4.5, row[2], dry_run=True, output="LINES")),
                len(self.multi_cell(col_widths[3] - 2, 4.5, row[3], dry_run=True, output="LINES")),
                1
            ]
            max_lines = max(line_counts)
            row_height = max(10, max_lines * 5 + 4)
            
            start_x = self.get_x()
            start_y = self.get_y()
            
            # Draw row background if alternating
            bg_color = (255, 255, 255) if idx % 2 == 0 else (248, 250, 252)
            self.set_fill_color(*bg_color)
            
            # Background rectangle for whole row
            self.rect(start_x, start_y, sum(col_widths), row_height, "F")
            
            # Render Cells
            curr_x = start_x
            for c_idx, val in enumerate(row):
                w = col_widths[c_idx]
                self.rect(curr_x, start_y, w, row_height, "D") # cell border
                
                # Render cell text
                self.set_xy(curr_x, start_y + (row_height - (line_counts[c_idx] * 4.5)) / 2)
                align = "C" if c_idx in [0, 4] else "L"
                if align == "L":
                    self.set_x(curr_x + 2)
                    w_text = w - 4
                else:
                    w_text = w
                    
                self.multi_cell(w_text, 4.5, val, border=0, align=align)
                curr_x += w
                
            self.set_xy(start_x, start_y + row_height)

        # Output file
        self.output(output_path)
        print(f"Successfully generated clean PDF at: {output_path}")

if __name__ == "__main__":
    pdf_gen = TeamInvolvementPDF()
    target_path = r"c:\Users\regal\.gemini\antigravity-ide\scratch\ecotrack\8. Project Demonstration\Team Involvement in Demonstration.pdf"
    pdf_gen.generate(target_path)
