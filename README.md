Below is a clean, assignment-ready **README.md** for your Complexity Analyzer Flask API.
You can copy-paste this directly into your project root.

---

```md
# Complexity Analyzer API (Flask)

## Overview

The **Complexity Analyzer API** is a Flask-based REST API that measures the execution time of different algorithms for varying input sizes.  
It helps demonstrate how algorithm performance grows as input size increases, providing both:

- Runtime results in JSON format
- A Base64-encoded performance graph

This project is designed for learning and analyzing **time complexity** concepts such as:

- **O(n)** (Linear)
- **O(n²)** (Quadratic)
- **O(log n)** (Logarithmic)

---

## Features

- Analyze multiple algorithms through a REST endpoint
- Measure execution time using `time.perf_counter()`
- Generate runtime graphs using Matplotlib
- Return results and graph in JSON response
- Supports step-based input size testing

---

## Algorithms Supported

| Algorithm Name  | Complexity |
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
├── app.py # Main Flask API
├── factorial.py # Algorithms implementation
├── requirements.txt # Dependencies
└── README.md # Documentation

````

---

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/complexity-analyzer.git
cd complexity-analyzer
````

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

---

### Home Endpoint

**GET /**

Returns a simple status message.

#### Example Request

```bash
curl http://127.0.0.1:3000/
```

#### Example Response

```text
Complexity Analyzer Running
```

---

### Analyze Algorithm Endpoint

**GET /analyze**

Runs the selected algorithm for increasing input sizes and measures runtime.

#### Query Parameters

| Parameter | Type   | Description         |
| --------- | ------ | ------------------- |
| `algo`    | string | Algorithm name      |
| `n`       | int    | Maximum input size  |
| `steps`   | int    | Number of intervals |

---

#### Example Request

```bash
curl "http://127.0.0.1:3000/analyze?algo=bubble_sort&n=500&steps=5"
```

---

#### Example JSON Response

```json
{
  "algorithm": "bubble_sort",
  "items": 500,
  "time_complexity": "O(n²)",
  "steps": 5,
  "total_analysis_time_seconds": 0.42,
  "results": [
    { "n": 100, "time_seconds": 0.002 },
    { "n": 200, "time_seconds": 0.009 },
    { "n": 300, "time_seconds": 0.021 },
    { "n": 400, "time_seconds": 0.037 },
    { "n": 500, "time_seconds": 0.061 }
  ],
  "graph_base64": "iVBORw0KGgoAAAANSUhEUgAA..."
}
```

---

## Output Graph

The API generates a runtime plot showing how execution time changes as input size increases.

The graph is returned as a **Base64 PNG string**, which can be decoded and displayed in:

- Web applications
- Postman
- Frontend dashboards

---

## Requirements

Main libraries used:

- Flask
- Matplotlib
- Python Standard Libraries (`time`, `io`, `base64`)

Example `requirements.txt`:

```txt
Flask
matplotlib
```

---

## Future Improvements

Possible enhancements:

- Input validation and error handling
- Add more algorithms (merge sort, quick sort)
- Store results in a database
- Add Swagger/OpenAPI documentation
- Frontend dashboard for visualization

---

## Author

Developed as part of an academic assignment on:

**Algorithm Time Complexity Analysis using REST APIs**

---

## License

This project is for educational use only.

```

---

# Next (Optional)

If you want, I can also generate:

- `requirements.txt`
- Full `factorial.py` algorithms file
- Swagger documentation (`swagger.json`)
- A proper report PDF for submission

Just tell me what your assignment requires.
```

Ai usage link - https://chatgpt.com/share/6979efca-d55c-8005-a79c-2073b289de7d
