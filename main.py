import pandas as pd
import matplotlib.pyplot as plt


def create_and_save_plot(output_path="plot.png"):
    df = pd.DataFrame({"x": [0, 1, 2, 3, 4, 5], "y": [0, 1, 4, 9, 16, 25]})
    plt.figure()
    plt.plot(df["x"], df["y"], marker="o")
    plt.title("x vs y")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.savefig(output_path, dpi=150)
    plt.close()
    print(f"Saved plot to {output_path}")


def main():
    create_and_save_plot()


if __name__ == "__main__":
    main()
