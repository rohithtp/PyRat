import sys
import psutil
from ratatui import App, Terminal, Paragraph, Gauge, Sparkline, split_h, split_v, Color, Style

class PyRatState:
    def __init__(self):
        self.cpu_history = [0] * 100
        self.max_history = 100
        self.ram_val = 0.0
        self.max_cpu = 0.0
        self.cpu_count = psutil.cpu_count()

    def update(self):
        # psutil.cpu_percent(interval=None) is non-blocking
        cpu = psutil.cpu_percent(interval=None)
        self.cpu_history.append(int(cpu))
        if len(self.cpu_history) > self.max_history:
            self.cpu_history.pop(0)
        
        # Update peak CPU
        if cpu > self.max_cpu:
            self.max_cpu = cpu
        
        self.ram_val = psutil.virtual_memory().percent

def render(term: Terminal, state: PyRatState):
    w, h = term.size()
    main_rect = (0, 0, w, h)
    
    # Layout: Header (3 lines), Content (Rest), Footer (1 line)
    # Using fractions might be tricky for exact lines, but let's try approximate or use specific logic if available.
    # split_h takes fractions. 3 lines out of 24 is ~0.125.
    # Let's use simple fractions for now: Top 15%, Middle 80%, Bottom 5%.
    header_r, content_r, footer_r = split_h(main_rect, 0.15, 0.80, 0.05)
    
    # --- Header ---
    title_text = "🏴‍☠️  PyRat: The High-Seas System Monitor  🏴‍☠️"
    title = Paragraph.from_text(title_text)
    title.set_block_title("Manifest", True)
    title.set_style(Style(fg=Color.Cyan, mods=1)) # 1 is likely Bold in termios/ratatui
    # Center text if possible, but Paragraph doesn't have alignment in this binding easily accessible?
    # Note: Paragraph.set_alignment might exist, but I'll stick to default.
    term.draw_paragraph(title, header_r)

    # --- Content ---
    # Split Content Vertically: CPU (Left) and RAM (Right)
    cpu_col, ram_col = split_v(content_r, 0.5, 0.5)

    # CPU Section (Sparkline)
    cpu_spark = Sparkline()
    current_cpu = state.cpu_history[-1] if state.cpu_history else 0
    cpu_spark.set_block_title(f"CPU Load: {current_cpu}% | Peak: {state.max_cpu}%", True)
    cpu_spark.set_values(state.cpu_history)
    cpu_spark.set_max(100)
    cpu_spark.set_style(Style(fg=Color.Green))
    term.draw_sparkline(cpu_spark, cpu_col)

    # RAM Section (Gauge)
    ram_gauge = Gauge()
    ram_gauge.set_block_title(f"RAM Usage: {state.ram_val}%", True)
    ram_gauge.ratio(state.ram_val / 100.0)
    
    # Styles
    # Note: Style constructor args might be strictly keyword or positional. 
    # help(Style) showed: Style(fg=..., bg=..., mods=...)
    ram_gauge.set_styles(
        style=Style(fg=Color.White),
        label_style=Style(fg=Color.White, mods=1), # Bold label
        gauge_style=Style(fg=Color.Magenta)
    )
    term.draw_gauge(ram_gauge, ram_col)

    # --- Footer ---
    foot_text = "Press 'q' to abandon ship. | Built with ratatui + uv"
    foot = Paragraph.from_text(foot_text)
    term.draw_paragraph(foot, footer_r)

def on_tick(term: Terminal, state: PyRatState):
    state.update()

def on_event(term: Terminal, evt: dict, state: PyRatState) -> bool:
    if evt.get("kind") == "key":
        ch = evt.get("ch")
        # 'q' is 113, 'Q' is 81. Or simple check.
        if ch in (ord('q'), ord('Q')):
            return False
        # Ctrl+C is 3
        if ch == 3:
            return False
    return True

def main():
    state = PyRatState()
    # Initial update
    state.update()
    
    # Run App
    # tick_ms=1000 means 1 second updates.
    try:
        App(
            render=render, 
            on_event=on_event, 
            on_tick=on_tick, 
            tick_ms=1000
        ).run(state)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
