import sys
import psutil
import time
from ratatui import App, Terminal, Paragraph, Gauge, Sparkline, split_h, split_v, Color, Style, Mod

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
    try:
        w, h = term.size()
        main_rect = (0, 0, w, h)
        
        # Manual Layout Splitting
        # Header: 3 lines, Footer: 1 line, Content: Rest
        header_h = 3
        footer_h = 1
        content_h = max(0, h - header_h - footer_h)
        
        # Check if screen is too small
        if h < (header_h + footer_h):
            # Fallback: Give everything to content or header? 
            # If very small, just show content
            header_r = (0, 0, w, 0)
            footer_r = (0, 0, w, 0)
            content_r = (0, 0, w, h)
        else:
            header_r = (0, 0, w, header_h)
            content_r = (0, header_h, w, content_h)
            footer_r = (0, header_h + content_h, w, footer_h)
        
        # --- Header ---
        title_text = "🏴‍☠️  PyRat: The High-Seas System Monitor  🏴‍☠️"
        title = Paragraph.from_text(title_text)
        title.set_block_title("Manifest", True)
        title.set_style(Style(fg=Color.Cyan, mods=Mod.BOLD))
        term.draw_paragraph(title, header_r)

        # --- Content ---
        cpu_col, ram_col = split_v(content_r, 0.5, 0.5)

        # CPU Section (Sparkline)
        cpu_spark = Sparkline()
        data = state.cpu_history
        current_cpu = data[-1] if data else 0
        cpu_spark.set_block_title(f"CPU Load: {current_cpu}% | Peak: {state.max_cpu}%", True)
        cpu_spark.set_values(data)
        cpu_spark.set_max(100)
        cpu_spark.set_style(Style(fg=Color.Green))
        term.draw_sparkline(cpu_spark, cpu_col)

        # RAM Section (Gauge)
        ram_gauge = Gauge()
        ram_gauge.set_block_title(f"RAM Usage: {state.ram_val}%", True)
        ram_gauge.ratio(state.ram_val / 100.0)
        
        ram_gauge.set_styles(
            style=Style(fg=Color.White),
            label_style=Style(fg=Color.White),
            gauge_style=Style(fg=Color.Magenta)
        )
        term.draw_gauge(ram_gauge, ram_col)

        # --- Footer ---
        foot_text = "Press 'q' to abandon ship. | Built with ratatui + uv"
        foot = Paragraph.from_text(foot_text)
        term.draw_paragraph(foot, footer_r)
    except Exception as e:
        raise e

def on_tick(term: Terminal, state: PyRatState):
    state.update()

def on_event(term: Terminal, evt: dict, state: PyRatState) -> bool:
    if evt.get("kind") == "key":
        ch = evt.get("ch")
        if ch in (ord('q'), ord('Q')):
            return False
        if ch == 3: # Ctrl+C
            return False
    return True

def on_start(term: Terminal, state: PyRatState):
    term.enter_alt()
    term.enable_raw()
    term.clear()

def on_stop(exc: Exception, term: Terminal, state: PyRatState):
    term.disable_raw()
    term.leave_alt()
    term.show_cursor()

def main():
    state = PyRatState()
    state.update()
    
    try:
        App(
            render=render, 
            on_event=on_event, 
            on_tick=on_tick,
            on_start=on_start,
            on_stop=on_stop,
            tick_ms=1000
        ).run(state)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
