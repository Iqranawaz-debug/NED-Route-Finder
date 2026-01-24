import streamlit as st
from backend import graph, a_star, dijkstra, coordinates

# === Streamlit Config ===
st.set_page_config(page_title="Route to NED", layout="centered")

# === Background and Styling ===
def set_background_and_style():
    st.markdown("""
        <style>
        .stApp {
            background-image: url("https://plus.unsplash.com/premium_photo-1661911626941-2bae2185d92c?q=80&w=2070&auto=format&fit=crop");
            background-size: cover;
            background-position: center;
            color: white;
        }

        .stApp::before {
            content: "";
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.55);
            z-index: -1;
        }

        .main-container {
            background-color: rgba(255, 255, 255, 0.07);
            padding: 2rem;
            border-radius: 15px;
            max-width: 700px;
            margin: auto;
        }

        .stButton>button {
            background-color: #ff4444;
            color: white;
            border-radius: 8px;
            padding: 10px 20px;
            font-size: 16px;
        }

        .result-box {
            background-color: rgba(255, 255, 255, 0.1);
            padding: 1rem;
            margin-top: 1.5rem;
            border-radius: 10px;
            font-size: 16px;
        }
        </style>
    """, unsafe_allow_html=True)

set_background_and_style()

# === Page Content ===
with st.container():
    st.markdown('<div class="main-container">', unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: center;'>🚍 Route Finder to NED University</h1>", unsafe_allow_html=True)

    # === Input Fields ===
    start_node = st.selectbox("Choose your starting point:", list(graph.keys()))
    destination = "NED University"
    algo_choice = st.radio("Choose the algorithm:", ["Dijkstra", "A*"], horizontal=True)

    # === Button Logic ===
    if st.button("Find Route"):
        if start_node == destination:
            st.warning("You're already at NED University.")
        else:
            if algo_choice == "Dijkstra":
                distance, path = dijkstra(graph, start_node, destination)
            else:
                distance, path = a_star(graph, start_node, destination, coordinates)

            if distance == float('inf') or not path:
                st.error(f"No path found from {start_node} to {destination}.")
            else:
                st.success(f"Path found from {start_node} to {destination} using {algo_choice}!")
                st.markdown(f"""
                    <div class="result-box">
                        <strong>Path:</strong> {' → '.join(path)}<br>
                        <strong>Total Distance:</strong> {round(distance, 2)} km<br>
                        <strong>Estimated Time:</strong> {round((distance / 40) * 60, 1)} minutes (at 40 km/h)
                    </div>
                """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)