# # Game Theory

A collection of Python implementations of core Game Theory algorithms and models, covering antagonistic matrix games in pure and mixed strategies, linear programming reductions, and cooperative game analysis.

## Repository Structure

```text
Game_theory/
├── lab1_matrix_games/
│   ├── main1.py
│   └── Readme1.md
├── lab2_brown_robinson/
│   ├── main2.py
│   └── Readme2.md
├── lab3_graph_analytic/
│   ├── main3.py
│   └── Readme3.md
├── lab4_cooperative_games/
│   ├── main4.py
│   └── Readme4.md
├── lab5_linear_programming/
│   ├── main5.py
│   └── Readme5.md
├── .gitignore
└── README.md
```

## Labs Overview

| Lab | Topic | Key Methods & Concepts | Dependencies |
| :--- | :--- | :--- | :--- |
| **[Lab 1](./lab1_matrix_games/Readme1.md)** | Matrix Games | Minimax & maximin criteria, saddle point detection, pure strategy solutions | `numpy` |
| **[Lab 2](./lab2_brown_robinson/Readme2.md)** | Brown–Robinson Method | Iterative fictitious play, empirical mixed strategies, convergence plotting | `numpy`, `matplotlib` |
| **[Lab 3](./lab3_graph_analytic/Readme3.md)** | Graph-Analytical Method | Graphical solution of $(2 \times n)$ and $(m \times 2)$ games, lower/upper envelopes | `numpy`, `matplotlib` |
| **[Lab 4](./lab4_cooperative_games/Readme4.md)** | Cooperative Games | Characteristic function, superadditivity, 0–1 normalization, C-core, Shapley value | Standard Library |
| **[Lab 5](./lab5_linear_programming/Readme5.md)** | Linear Programming | Reduction of matrix games to dual LP problems, exact mixed strategies via `linprog` | `numpy`, `scipy` |

## Getting Started

### Prerequisites

- Python 3.8+

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Game_theory
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # Windows (Git Bash)
   source venv/Scripts/activate
   # Linux / macOS
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install numpy matplotlib scipy
   ```

### Usage

Run any lab script directly from the root directory:

```bash
python lab1_matrix_games/main1.py
python lab2_brown_robinson/main2.py
python lab3_graph_analytic/main3.py
python lab4_cooperative_games/main4.py
python lab5_linear_programming/main5.py
```