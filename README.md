# NASA_LS_Airfoil_Analysis---Research-Paper
This is the official repository of the paper written by Raghav Venkat Iyer titled 'Aerodynamic Performance of NASA LS Airfoils for Fixed-Wing UAV Applications in the Martian Atmosphere'. This repository includes the python code used for the processing of graphs, .dat files of the airfoils, and even processed csv files. 







# Aerodynamic Performance of NASA LS Airfoils for Fixed-Wing UAV Applications in the Martian Atmosphere

## Overview

This repository contains the datasets, airfoil geometries, simulation files, and supplementary material used in the research paper:

> **Aerodynamic Performance of NASA LS Airfoils for Fixed-Wing UAV Applications in the Martian Atmosphere**

The study investigates the influence of **airfoil thickness ratio** on the aerodynamic efficiency of NASA Low-Speed (LS) airfoils operating under Martian atmospheric conditions. Computational analysis was performed using both **XFLR5** and **CFD simulations in SimScale**.

---

## Research Question

> **How does the airfoil thickness ratio of a NASA LS airfoil affect its aerodynamic efficiency (lift-to-drag ratio) in Martian atmospheric conditions for a slow-speed fixed-wing UAV under varying angles of attack?**

---

## Repository Structure

```
├── Airfoils/
│   ├── NASA_LS0413.dat
│   ├── NASA_LS0417.dat
│   ├── NASA_LS0421.dat
│   ├── NASA_LS0413.step
│   ├── NASA_LS0417.step
│   └── NASA_LS0421.step
│
├── XFLR5/
│   ├── Polar Data
│   ├── Lift Curves
│   ├── Drag Curves
│   ├── L_D Curves
│   └── Project Files
│
├── CFD/
│   ├── SimScale Setup
│   ├── Pressure Contours
│   ├── Velocity Contours
│   ├── Streamlines
│   └── Mesh Information
│
├── Figures/
│
├── Data/
│   ├── Raw Data
│   ├── Processed Results
│   └── Graph Data
│
└── Paper/
    └── Final Manuscript
```

---

## Airfoils Investigated

Primary Airfoils

- NASA LS(1)-0413
- NASA LS(1)-0417
- NASA LS(1)-0421

Supplementary Airfoils (Appendix)

- NACA 0012
- Representative C-5 Galaxy Wing Airfoil Section

---

## Simulation Conditions

### XFLR5

- Analysis Method: Viscous Analysis
- Flow Type: Incompressible
- Reynolds Number: *(Insert value used)*
- Mach Number: *(Insert value used)*
- Angle of Attack:
  - -5° to 15°
  - Increment: 1°

---

### CFD

Software

- SimScale

Solver

- Steady-State CFD
- Incompressible Flow
- k-ω SST Turbulence Model

Boundary Conditions

- Velocity Inlet
- Pressure Outlet
- No-Slip Airfoil Wall
- Slip/Symmetry Side Walls

---

## Martian Atmospheric Properties

| Property | Value |
|----------|------:|
| Density | 0.020 kg/m³ |
| Dynamic Viscosity | 1.08 × 10⁻⁵ Pa·s |

---

## Airfoil Geometry

Airfoil coordinates were obtained from the UIUC Airfoil Database and converted into STEP geometry for CFD analysis.

The repository contains:

- Original DAT files
- CAD-generated STEP files
- CFD-ready geometries

---

## Performance Metrics

The following aerodynamic quantities were evaluated:

- Lift Coefficient (CL)
- Drag Coefficient (CD)
- Lift-to-Drag Ratio (CL/CD)
- Pressure Distribution
- Velocity Distribution
- Flow Streamlines

---

## Key Results

| Airfoil | Maximum CL/CD | Angle of Attack |
|----------|--------------:|----------------:|
| NASA LS0413 | 39.16 | 6° |
| NASA LS0417 | 39.94 | 7° |
| NASA LS0421 | 29.69 | 9° |

The NASA LS0417 airfoil demonstrated the highest aerodynamic efficiency under the simulated Martian conditions.

---

## Software Used

- XFLR5
- SimScale
- Onshape
- CadQuery
- Python
- Microsoft Excel

---

## Reproducibility

All raw datasets, processed results, CFD geometries, and simulation settings used throughout the paper are included to facilitate independent verification and reproduction of the study.

---

## Citation

If you use this repository, please cite:

```
Raghav Venkat Iyer.
Aerodynamic Performance of NASA LS Airfoils for Fixed-Wing UAV Applications in the Martian Atmosphere.
2026.
```

---

## License

This repository is released under the MIT License unless otherwise stated.

---

## Contact

For questions regarding the research or repository:

**Raghav Venkat Iyer**

GitHub: *Your GitHub Profile*

LinkedIn: *Your LinkedIn Profile*

---

## Acknowledgements

- NASA Langley Research Center
- UIUC Airfoil Coordinates Database
- SimScale
- XFLR5 Development Team
