📘 Unit Converter – Python Package
A simple and clean Python unit-conversion package built as part of my Python learning roadmap.
This project demonstrates how to structure a real Python package with multiple modules, clean imports, and organized code.
🚀 About the Project
This project contains a custom package named unit_converter, which includes functions to convert:
Length units (km → m, m → cm, etc.)
Weight units (kg → g, g → kg)
Temperature units (Celsius ↔ Fahrenheit)
It also teaches:
How to build a Python package from scratch
How to use __init__.py
How to split code into multiple modules
How to design a clean project structure
How to import functions in a scalable way
📁 Project Structure
unit_converter_project/
│── main.py
│── README.md
│
└── unit_converter/
    │── __init__.py
    │── length.py
    │── weight.py
    │── temperature.py
🔧 Modules
1️⃣ length.py
Functions for length conversions:
km_to_m(km)
m_to_cm(m)
2️⃣ weight.py
Functions for mass conversions:
kg_to_g(kg)
g_to_kg(g)
3️⃣ temperature.py
Functions for temperature conversions:
c_to_f(c)
f_to_c(f)
