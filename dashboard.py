try:
    import streamlit as st
except Exception:
    # Provide a minimal stub for environments where streamlit isn't installed
    class _StreamlitStub:
        def title(self, *a, **k):
            return None
        def metric(self, *a, **k):
            return None
        def subheader(self, *a, **k):
            return None
        def write(self, *a, **k):
            return None

    st = _StreamlitStub()
import json
import os

st.title("Detection Engineering Dashboard")

count = 0

for file in os.listdir("rules"):

    if file.endswith(".json"):
        count += 1

st.metric("Detection Rules", count)

st.subheader("Loaded Rules")

for file in os.listdir("rules"):

    if file.endswith(".json"):

        with open(os.path.join("rules", file)) as f:

            rule = json.load(f)

            st.write(
                rule["name"],
                rule["mitre"]
            )