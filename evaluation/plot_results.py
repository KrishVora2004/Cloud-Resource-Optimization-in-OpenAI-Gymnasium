# evaluation/plot_results.py

import matplotlib.pyplot as plt


def plot_instances_vs_workload(results_dict):

    for name, results in results_dict.items():
        plt.plot(results["workload"], label=f"{name} workload", linestyle='--')
        plt.plot(results["instances"], label=f"{name} instances")

    plt.legend()
    plt.title("Workload vs Instances")
    plt.xlabel("Time Steps")
    plt.ylabel("Value")
    plt.show()