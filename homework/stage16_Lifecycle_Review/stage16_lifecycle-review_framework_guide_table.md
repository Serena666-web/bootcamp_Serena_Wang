# Applied Financial Engineering — Framework Guide Template

This Framework Guide is a structured reflection tool.  
Fill it in as you progress through the course or at the end of your project.  
It will help you connect each stage of the **Applied Financial Engineering Lifecycle** to your own project, and create a portfolio-ready artifact.

---

## How to Use
- Each row corresponds to one stage in the lifecycle.  
- Use the prompts to guide your answers.  
- Be concise but specific — 2–4 sentences per cell is often enough.  
- This is **not a test prep sheet**. It’s a way to *document, reflect, and demonstrate* your process.

---

## Framework Guide Table

| Lifecycle Stage | What You Did | Challenges | Solutions / Decisions | Future Improvements |
|-----------------|--------------|------------|-----------------------|---------------------|
| Lifecycle Stage | What You Did | Challenges | Solutions / Decisions | Future Improvements |
|-----------------|--------------|------------|-----------------------|---------------------|
| **1. Problem Framing & Scoping** | Defined the problem: predicting short-term returns for Nvidia stock.| Balancing model complexity with interpretability was tricky. | Narrowed scope to regression-based forecasting with clear metrics (eg.RMSE). | Next time, involve stakeholders earlier to refine goals and risk constraints. |
| **2. Tooling Setup** | Configured Python environment with pandas, numpy, scikit-learn, matplotlib, and yfinance. | Faced dependency conflicts across versions. | Used virtual environments and saved requirements in `requirements.txt`. | Try Docker to ensure reproducibility. |
| **3. Python Fundamentals** | Applied loops, functions, and class structures; used numpy arrays for efficiency. | Needed to recall vectorized operations or enumeration to avoid slow loops. | Practiced with small benchmarks and used in larger data set. | Practice more to ensure efficient coding. |
| **4. Data Acquisition / Ingestion** | Pulled price data via yfinance and saved raw data as CSV. | Occasionally API failed or returned missing days. | Added retry logic after each pull. | Try other data vendor |
| **5. Data Storage** | Organized into `data/raw`, `data/processed`, `artifacts/`. Used CSV for raw, parquet for processed. | Schema drift when new columns appeared. | Standardized column naming and schema validation. | Automate schema checks and use databases for larger scale. |
| **6. Data Preprocessing** | Cleaned missing values, adjusted for splits. | Some variables had unexpected gaps. | Applied forward fill and median imputation. | Explore more domain-aware preprocessing like volatility adjustment. |
| **7. Outlier Analysis** | Used IQR and z-score methods to flag extreme returns. | Distinguishing true events (some shock) from errors was hard. | Kept known events, capped erroneous spikes. | Add event calendars to separate structural vs data errors. |
| **8. Exploratory Data Analysis (EDA)** | Plotted return distributions, autocorrelations, and rolling volatility. | Initial histograms were skewed and hard to interpret. | Applied log transformations and compared across windows. | Add polynomial function. |
| **9. Feature Engineering** | Built lagged returns, moving averages, and momentum ratios. | Choosing look-back windows was arbitrary. | Validated windows by cross-validation on past returns. | Explore volume shocks or sentiment. |
| **10. Modeling (Regression / Time Series / Classification)** | Trained linear regression. | Overfitting. | Used grid search. | Try tree-based ensembles. |
| **11. Evaluation & Risk Communication** | Evaluated with RMSE.| Hard to convey uncertainty to non-technical peers. | Used confidence intervals and scenario analysis. | Add backtesting. |
| **12. Results Reporting, Delivery Design & Stakeholder Communication** | Delivered Jupyter notebook and short slide deck with visuals. | Some statistical terms might be to hard to stakeholders to understand. | Simplified plots, added plain-language explanations. | Develop dashboards with interactive drill-downs. |
| **13. Productization** | Packaged pipeline into modular Python scripts. | Maintaining reproducibility across machines. | Used relative paths and requirements txt. | Implement CI/CD with GitHub Actions. |
| **14. Deployment & Monitoring** | Ran scheduled retrains locally. | Monitoring drift manually was not easy. | Logged metrics after each run and compared trends. | Add automated alerts. |
| **15. Orchestration & System Design** | Defined workflow as DAG (ingest → clean → features → train → evaluate → report). | Dependencies across tasks created brittle runs. | Added checkpointing. | Use Prefect to manage orchestration. |
| **16. Lifecycle Review & Reflection** | Review pipeline design across all stages. |Forgot some details. | Review on repo. | Try other text format. |

---

## Reflection Prompts

- Which stage was the most **difficult** for you, and why?  
- Which stage was the most **rewarding**?  
- How do the stages **connect** — where did one stage’s decisions constrain or enable later stages?  
- If you repeated this project, what would you **do differently across the lifecycle**?  
- Which skills do you most want to **strengthen** before your next financial engineering project?  

Initial tooling setup was the most difficult stage for me since it was the first time for me to use GitHub repo and sometimes it was struggling to follow the instructions without knowing where's the direction. Feature Engineering is the most rewarding one as the process of translating financial domain knowledge into lagged returns, ratios, and moving averages directly improved model accuracy and gave a sense of creative contribution. Early preprocessing and storage choices shaped everything downstream; for example, inconsistent schema during ingestion created problems in training and evaluation at later stages. I would want to strengthening my coding fundamentals more before moving on to the next stage as it took me much longer to ingest the data provided in the lecture than my peers.

