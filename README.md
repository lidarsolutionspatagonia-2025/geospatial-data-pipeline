# Geospatial Data Processing Pipeline

Simple geospatial data processing pipeline built with Python and GeoPandas.

## Overview

This project demonstrates a reproducible workflow for processing vector geospatial data, including coordinate system transformation, geometry processing, and output generation for downstream applications.

## Pipeline Steps

- Shapefile ingestion
- CRS transformation to WGS84 (EPSG:4326)
- Geometry processing
- Area calculation
- Export to GeoJSON

## Tech Stack

- Python (GeoPandas)
- Docker
- GitHub

## Output

The pipeline generates a GeoJSON file ready for web mapping and geospatial analytics applications.

## How to Run

```bash
pip install -r requirements.txt
cd scripts
python process_data.py

---

# 🧠 Cómo saber si quedó bien

En GitHub:

- Vas a ver los comandos dentro de un **bloque gris**
- Con formato tipo código

Si ves todo como texto plano → está mal cerrado

---

# 🔴 Error típico

Esto rompe todo:
comandos
