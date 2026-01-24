
# 🚍 Route Finder to NED University

An interactive web application built with **Streamlit** that calculates the most efficient travel routes to NED University from various locations in Karachi using classical AI pathfinding algorithms.

## 🌟 Overview
This project demonstrates the practical application of **Graph Theory** and **Search Algorithms**. It allows users to compare how different algorithms perform in a real-world navigation scenario.

## 🛠️ Technical Features
- **Dijkstra’s Algorithm:** Implemented to find the absolute shortest path by exploring all nodes in the graph.
- **A* Search Algorithm:** Optimized pathfinding using a **Heuristic function** (Euclidean distance) based on geographic coordinates.
- **Dynamic UI:** A custom-styled Streamlit interface with real-time distance and time estimation.
- **Modular Architecture:** Clean separation between the frontend logic (`app.py`) and the algorithmic backend (`backend.py`).



## 📁 Project Structure
- `app.py`: The Streamlit dashboard and UI styling.
- `backend.py`: Contains the Graph data, coordinate system, and algorithm implementations.
- `requirements.txt`: List of dependencies.

## Sample Output
- Path: Displayed as a sequence of landmarks (e.g., Safoora Goth → University Road → NED).
- Total Distance: Calculated in kilometers.
- Estimated Time: Calculated based on an average city speed of 40 km/h.
