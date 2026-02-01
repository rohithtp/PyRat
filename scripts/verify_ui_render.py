import sys
import os

# Add root to path so we can import main
sys.path.append(os.getcwd())

try:
    from main import render, PyRatState
    # We don't strictly need ratatui real classes for duck typing, 
    # but we need to ensure imports in main work.
except ImportError as e:
    print(f"Failed to import main: {e}")
    sys.exit(1)

class MockTerminal:
    def size(self):
        return (80, 24)
    
    def draw_paragraph(self, widget, area):
        # Just check it accepts arguments
        pass
    
    def draw_sparkline(self, widget, area):
        pass
    
    def draw_gauge(self, widget, area):
        pass

def verify():
    print("Verifying UI render logic...")
    state = PyRatState()
    state.update()
    
    term = MockTerminal()
    
    try:
        render(term, state)
        print("Render successful (no exceptions).")
    except Exception as e:
        print(f"Render failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

    # Test small screen
    print("Verifying small screen render...")
    class SmallTerminal(MockTerminal):
        def size(self):
            return (80, 3) 
    
    try:
        render(SmallTerminal(), state)
        print("Small screen render successful.")
    except Exception as e:
        print(f"Small screen render failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    verify()
