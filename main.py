from flask import Flask, jsonify, request
import time
import base64
import io
from factorial import linear_search, bubble_sort, nested_loops, binary_search

#matplotlib initilization stuff 
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

app = Flask(__name__)


@app.route("/")
def home():
    return "Complexity Analyzer Running"



@app.route("/analyze", methods=["GET"])
def analyze():

    overall_start = time.perf_counter()

    algo_name = request.args.get("algo")
    n = request.args.get("n")
    steps = request.args.get("steps")

    n = int(n)
    steps = int(steps)

    step_sizes = [int((i + 1) * n / steps) for i in range(steps)]

    results = []
    times = []

    #the algorithms available
    algorithms = {
        "linear_search": linear_search,
        "bubble_sort": bubble_sort,
        "binary_search": binary_search,
        "nested_loops": nested_loops
    }

    algo_func = algorithms[algo_name]

    for size in step_sizes:
        start = time.perf_counter()
        algo_func(size)
        end = time.perf_counter()
        # to get the total time the function run for 
        runtime = end - start
        results.append({
            "n": size,
            "time_seconds": runtime
        })
        times.append(runtime)

    #getting the graph
    plt.figure()
    plt.plot(step_sizes, times, marker="o")
    plt.title(f"Time Complexity Analysis: {algo_name}")
    plt.xlabel("Input Size (n)")
    plt.ylabel("Execution Time (seconds)")

    # Convert plot into Base64
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)

    graph_base64 = base64.b64encode(buf.read()).decode("utf-8")
    plt.close()
    #TODO - put the base64 image on a url 


    overall_end = time.perf_counter()

    if algo_name == "linear_search" :
        time_complexity = "O(n)"
    elif algo_name == "bubble_sort" :
        time_complexity = "O(n2)"
    elif algo_name == "binary_search" :
        time_complexity = "O(log n)"
    elif algo_name == "nested_loops" :
        time_complexity = "O(n2)"             

    response = {
        "algorithm": algo_name,
        "items": n,
        "time_complexity": time_complexity,
        "steps": steps,
        "start_time":start,
        "end_time":end,
        "total_analysis_time_seconds": overall_end - overall_start,
        "results": results,
        "graph_base64": graph_base64
    }

    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True, port=3000)
