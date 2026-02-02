# Complexity Analyzer API (Flask)

## Overview

The **Complexity Analyzer API** is a Flask-based REST API that measures the execution time of different algorithms for varying input sizes. It helps demonstrate how algorithm performance grows as input size increases, providing:

- Runtime results in JSON format
- Performance graphs saved as PNG files
- Persistent storage of analysis results using SQLite

This project is designed for learning and analyzing **time complexity** concepts such as:

- **O(n)** — Linear
- **O(n²)** — Quadratic
- **O(log n)** — Logarithmic

---

## Features

- Analyze multiple algorithms through REST endpoints
- Measure execution time using `time.perf_counter()`
- Generate and save runtime graphs using Matplotlib
- Persist analysis results to SQLite database
- Retrieve past analysis records by ID
- Supports step-based input size testing

---

## Algorithms Supported

| Algorithm       | Complexity |
| --------------- | ---------- |
| `linear_search` | O(n)       |
| `bubble_sort`   | O(n²)      |
| `binary_search` | O(log n)   |
| `nested_loops`  | O(n²)      |

---

## Project Structure

```
complexity-analyzer/
│
├── app.py              # Main Flask API
├── factorial.py        # Algorithm implementations
├── requirements.txt    # Dependencies
├── README.md           # Documentation
├── instance/
│   └── algorithms.db   # SQLite database (auto-generated)
└── images/
    └── static/         # Generated graph images
```

---

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/complexity-analyzer.git
cd complexity-analyzer
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create Required Directories

```bash
mkdir -p images/static
```

---

## Running the API Server

Start the Flask application:

```bash
python app.py
```

The server will run on:

```
http://127.0.0.1:3000
```

---

## API Endpoints

### 1. Home

**GET /**

Returns a simple status message.

```bash
curl http://127.0.0.1:3000/
```

**Response:**

```
Complexity Analyzer Running
```

---

### 2. Analyze Algorithm

**GET /analyze**

Runs the selected algorithm for increasing input sizes and measures runtime.

**Query Parameters:**

| Parameter | Type   | Description                     |
| --------- | ------ | ------------------------------- |
| `algo`    | string | Algorithm name                  |
| `n`       | int    | Maximum input size              |
| `steps`   | int    | Number of measurement intervals |

**Example Request:**

```bash
curl "http://127.0.0.1:3000/analyze?algo=bubble_sort&n=500&steps=5"
```

**Example Response:**

```json
{
  "algorithm": "bubble_sort",
  "items": 500,
  "time_complexity": "O(n2)",
  "steps": 5,
  "start_time": 1234567890.123,
  "end_time": 1234567890.456,
  "total_analysis_time_seconds": 0.42,
  "path_to_graph": "/images/static/bubble_sort.png"
}
```

---

### 3. Save Analysis

**POST /save_analysis**

Persists an analysis result to the SQLite database.

**Request Body (JSON):**

```json
{
  "algorithm": "bubble_sort",
  "items": 500,
  "steps": 5,
  "start_time": 1234567890.123,
  "end_time": 1234567890.456,
  "total_time_ms": 420.5,
  "time_complexity": "O(n2)",
  "path_to_graph": "/images/static/bubble_sort.png"
}
```

**Example Request:**

```bash
curl -X POST http://127.0.0.1:3000/save_analysis \
  -H "Content-Type: application/json" \
  -d '{
    "algorithm": "bubble_sort",
    "items": 500,
    "steps": 5,
    "start_time": 1234567890.123,
    "end_time": 1234567890.456,
    "total_time_ms": 420.5,
    "time_complexity": "O(n2)",
    "path_to_graph": "/images/static/bubble_sort.png"
  }'
```

**Success Response (201):**

```json
{
  "message": "saved!",
  "id": 1
}
```

**Error Response (500):**

```json
{
  "error": "error message"
}
```

---

### 4. Retrieve Analysis

**GET /retrieve_analysis/<id>**

Retrieves a saved analysis record by its ID.

**Example Request:**

```bash
curl http://127.0.0.1:3000/retrieve_analysis/1
```

**Success Response (200):**

```json
{
  "id": 1,
  "algo_name": "bubble_sort",
  "items": 500,
  "steps": 5,
  "start_time": 1234567890.123,
  "end_time": 1234567890.456,
  "time_complexity": "O(n2)",
  "path_to_graph": "/images/static/bubble_sort.png"
}
```

**Not Found Response (404):**

```json
{
  "error": "Not found"
}
```

---

## Database Schema

The API uses SQLite with Flask-SQLAlchemy. The `algorithm_info` table stores:

| Column            | Type    | Description                   |
| ----------------- | ------- | ----------------------------- |
| `id`              | Integer | Primary key (auto-increment)  |
| `algo_name`       | String  | Name of the algorithm         |
| `items`           | Integer | Maximum input size (n)        |
| `steps`           | Integer | Number of measurement steps   |
| `start_time`      | Float   | Analysis start timestamp      |
| `end_time`        | Float   | Analysis end timestamp        |
| `total_time_ms`   | Float   | Total analysis duration       |
| `time_complexity` | String  | Big-O notation                |
| `path_to_graph`   | String  | Path to the saved graph image |

---

## Requirements

```txt
Flask
Flask-SQLAlchemy
matplotlib
```

---

## Future Improvements

- Input validation and error handling
- Add more algorithms (merge sort, quick sort)
- List all saved analyses endpoint
- Delete analysis endpoint
- Swagger/OpenAPI documentation
- Frontend dashboard for visualization

---
