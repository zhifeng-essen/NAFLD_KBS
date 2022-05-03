import streamlit.components.v1 as components
import os

parent_dir = os.path.dirname(os.path.abspath(__file__))
build_dir = os.path.join(parent_dir, "build")
ketcher = components.declare_component(
    "ketcher",
    path=build_dir
)