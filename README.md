# 🎬 Netflix Recommendation System

### Discover your next favorite movie! 🍿

A Python-based movie recommendation system that helps users discover highly rated movies based on genre preferences, IMDb ratings, and popularity.

Built using **Python, Pandas, NumPy, and Streamlit**, the project combines data processing, a weighted rating algorithm, and a Netflix-inspired interactive web interface.

---

## 📸 Preview

A modern, dark-themed interface inspired by Netflix.

**Application features:**

- Movie genre selection
- Interactive popularity threshold slider
- Customizable number of recommendations
- Movie rankings displayed in a table
<img width="1022" height="892" alt="image" src="https://github.com/user-attachments/assets/885332fb-3687-40b3-be1e-4a85b732a9c9" />
<img width="961" height="651" alt="image" src="https://github.com/user-attachments/assets/3a195a84-ee1a-4095-8b4b-39fe3f2790ae" />


---

## 📖 About the Project

The Netflix Recommendation System is a movie ranking application built using an IMDb movie dataset.

Instead of simply recommending movies with the highest average ratings, the application considers both the **IMDb rating** and the **number of user votes**.

This helps reduce the influence of movies with very high ratings but relatively few reviews.

The project was initially developed during a Python programming course and later extended with a custom Streamlit interface.

Its main purpose is to demonstrate practical Python skills, data analysis, object-oriented programming, and basic web application development.

---

## ✨ Features

- 🎭 **Genre Filtering** — Select your preferred movie genre.
- ⭐ **Weighted Rating Algorithm** — Calculate movie scores using ratings and vote counts.
- 📊 **Popularity Threshold** — Filter movies based on a selected vote-count quantile.
- 🎯 **Customizable Results** — Display the top 5, 10, or 20 recommendations.
- 🎨 **Netflix-Inspired UI** — Dark-themed interface with red accents.
- 🧹 **Data Cleaning** — Remove duplicates and prepare the dataset for analysis.
- 🐍 **Object-Oriented Design** — Recommendation logic organized into a reusable Python class.

---

## 🛠️ Tech Stack

| Technology   | Purpose                                  |
| ------------ | ---------------------------------------- |
| Python       | Main programming language                |
| Pandas       | Dataset cleaning and manipulation        |
| NumPy        | Statistical calculations                 |
| Streamlit    | Interactive web application              |
| IMDb Dataset | Movie ratings and popularity information |

---

## 🧠 How the Recommendation Algorithm Works

The recommendation system uses a **weighted rating formula** to calculate a score for every eligible movie.

[
WR = \frac{v}{v+m}R + \frac{m}{v+m}C
]

Where:

- **WR** — Weighted rating
- **R** — Average IMDb rating of the movie
- **v** — Number of votes received by the movie
- **m** — Minimum vote threshold calculated using the selected quantile
- **C** — Mean rating of the filtered movies

### Recommendation Process

1. Load the IMDb dataset.
2. Clean the dataset and remove duplicate movies.
3. Filter movies by the selected genre.
4. Calculate the minimum number of votes using a quantile.
5. Remove movies below the popularity threshold.
6. Calculate weighted ratings.
7. Sort movies by their weighted scores.
8. Display the top recommendations.

This approach balances movie ratings with popularity, producing a more reliable ranking than sorting by IMDb rating alone.

---

## 📁 Project Structure

```text
Netflix-Recommendation-System/
│
├── app.py
├── recommender.py
├── imdb.csv
├── requirements.txt
└── README.md
```

**File descriptions:**

- `app.py` — Streamlit user interface
- `recommender.py` — Movie recommendation algorithm and Python class
- `imdb.csv` — IMDb movie dataset
- `requirements.txt` — Required Python packages
- `README.md` — Project documentation

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/kuleszamikolaj7-cell/Netflix-Recommendation-System.git
```

### 2. Navigate to the project folder

```bash
cd Netflix-Recommendation-System
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the application

```bash
python -m streamlit run app.py
```

The application should open automatically in your web browser.

If it doesn't, open:

`http://localhost:8501`

**Note:** Make sure the `imdb.csv` dataset is available in the project's main directory.

---

## 💻 Usage

1. Launch the Streamlit application.
2. Select your preferred movie genre.
3. Adjust the popularity threshold.
4. Choose the number of recommendations.
5. Click **Get Recommendations**.
6. Explore the generated movie ranking.

### Example

**Input:**

```text
Genre: Comedy
Popularity Threshold: 80%
Number of Recommendations: 5
```

**Output:**

A table containing the top 5 qualifying comedy movies, sorted by weighted rating.

The actual recommendations depend on the IMDb dataset.

---

## 🧩 Object-Oriented Programming

The recommendation algorithm is organized into the `NetflixRecomennderSystem` class.

The class includes methods responsible for individual steps of the recommendation process:

```python
read_file()
cleanData()
filter_genre()
Thresh_votes()
avg_score()
sort_score()
run()
```

This structure separates the recommendation logic from the user interface and makes the project easier to maintain and extend.

---

## 🗺️ Roadmap

Future improvements planned for the project:

- [ ] Add movie posters and descriptions
- [ ] Introduce additional filtering options
- [ ] Create interactive rating charts
- [ ] Add a search function for specific movies
- [ ] Implement content-based recommendations
- [ ] Add automated tests
- [ ] Deploy the application online

---

## 📚 What I Learned

During this project, I gained practical experience in:

- Working with real-world CSV datasets
- Cleaning and processing data using Pandas
- Performing statistical calculations with NumPy
- Implementing weighted ranking algorithms
- Applying object-oriented programming concepts
- Building interactive web interfaces using Streamlit
- Connecting Python backend logic with a frontend application
- Organizing a programming project for GitHub

---

## ⚠️ Known Limitations

- Recommendations are based on IMDb ratings and vote counts, rather than individual viewing history.
- The system does not currently use machine learning.
- Results depend on the quality and completeness of the dataset.
- The application requires the IMDb CSV dataset to be available locally.
- Movie posters and descriptions are not yet included.

---

## 👨‍💻 Author

**Mikołaj Kulesza**

GitHub: [kuleszamikolaj7-cell](https://github.com/kuleszamikolaj7-cell)

Developed as a Python learning project and extended for my programming portfolio.

---

⭐ If you find this project interesting, feel free to explore the code!
