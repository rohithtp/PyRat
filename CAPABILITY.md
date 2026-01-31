# 🏴‍☠️ PyRat Capabilities

This document outlines the current functional capabilities of the PyRat system monitor and the roadmap for future enhancements.

## ✅ Current Capabilities

### System Overview
- **Header**: Displays the application title ("PyRat: The High-Seas System Monitor") with a bold Cyan style.
- **Footer**: Provides exit instructions ("Press 'q' to abandon ship") and credits.
- **Layout**: Uses a stacked layout to separate header, content, and footer. The content section is divided into two columns (side-by-side) for CPU and RAM monitoring.

### CPU Monitoring
- **Real-Time Visualization**: Displays a Sparkline graph (Green) showing the history of CPU usage over the last 100 ticks.
- **Current Load**: Shows the instantaneous CPU usage percentage.
- **Peak Load**: Tracks and displays the **maximum (peak)** CPU usage recorded during the session.

### RAM Monitoring
- **Usage Gauge**: Displays a visual gauge representing current Memory (RAM) usage.
- **Percentage Readout**: Shows the exact percentage of RAM currently in use.
- **Styling**: Uses color-coded components (Magenta gauge, White label) for clear visibility.

## 🗺️ Planned Capabilities

### 1. Expanded Hardware Metrics
- **Per-Core Breakdown**: Visualize CPU usage for individual cores instead of just the system average.
- **Disk I/O**: Monitor read/write speeds for primary storage devices.
- **Network Traffic**: Display real-time Upload and Download speeds in a dual-line chart.
- **Battery Health**: (Laptop only) Show battery percentage and charging status.

### 2. Process Management
- **Top Processes**: List the top 5-10 processes consuming CPU or RAM.
- **Kill Process**: Ability to terminate a process directly from the UI (e.g., by selecting it and pressing 'k').

### 3. Advanced UI/UX
- **Theming**: Support for user-selectable color themes (e.g., "Matrix Green", "Red Alert", "Ocean Blue").
- **Responsive Layout**: Better handling of terminal resize events and small screens.
- **Tabs**: multiple views for different metric categories (Overview, Network, Processes).

### 4. Logging & Alerts
- **High Resource Alert**: Visual flash or log entry when CPU/RAM exceeds a threshold (e.g., 90%).
- **Session Export**: Save the session's performance history to a CSV or JSON file on exit.
