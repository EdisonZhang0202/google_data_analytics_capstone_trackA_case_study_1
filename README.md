# Cyclistic Bike-Share Analysis

## Business Task

The objective of this analysis is to examine how **casual riders** and **annual members** use Cyclistic bikes differently. These insights are intended to support the development of marketing strategies aimed at converting casual riders into annual members.

---

## Dataset

* Source: Cyclistic historical trip data (public dataset)
* Timeframe: 12 months
* Key variables:

  * `member_casual` (user type)
  * `ride_length` (ride duration in seconds)
  * `day_of_week`

---

## Data Processing

The data was processed and prepared using Python (Pandas) to ensure consistency, accuracy, and suitability for analysis.

### Data Loading and Integration

* Twelve monthly datasets (April 2025 – March 2026) were imported as separate DataFrames.
* Column structures were verified to ensure consistency across all files.
* All datasets were concatenated into a single unified DataFrame.
* The combined dataset was exported and reloaded to validate successful integration.

### Data Inspection

* Initial exploratory checks were performed, including:

  * Reviewing column names and data types
  * Inspecting sample rows (head/tail)
  * Generating summary statistics
* Categorical variables such as `member_casual` and `rideable_type` were validated for consistency.
* Missing values were identified and assessed.

### Data Transformation

* Timestamp fields (`started_at`, `ended_at`) were converted to datetime format.
* Additional temporal features were derived:

  * Date (start and end)
  * Month, day, and year
  * Day of the week
* A new variable, `ride_length`, was calculated as the total ride duration in seconds.

### Data Cleaning

* Records associated with system maintenance or testing (e.g., station labeled "HQ QR") were removed.
* Entries with invalid ride durations (negative values) were excluded.
* A cleaned dataset (`v2`) was created to preserve data integrity and ensure reproducibility.

### Data Structuring

* The `day_of_week` variable was converted to an ordered categorical format to maintain correct chronological ordering (Sunday through Saturday).
* The dataset was grouped by:

  * Membership type (`member_casual`)
  * Day of the week

### Aggregation and Summary Metrics

* Key metrics were calculated:

  * Total number of rides
  * Average ride duration
* Summary statistics were generated using group-by operations to support comparative analysis between user types.

### Data Export

* The final aggregated dataset was exported as:

  * `summary_stats_by_member_and_day.csv`
* This file was used for visualization and downstream analysis.

---

## Key Findings

### 1. Ride Duration

Casual riders consistently exhibit longer ride durations than annual members across all days of the week.

| Day       | Casual | Member |
|-----------|--------|--------|
| Sunday    | 1565.91 | 821.46 |
| Monday    | 1360.01 | 726.28 |
| Tuesday   | 1175.15 | 718.03 |
| Wednesday | 1134.74 | 715.21 |
| Thursday  | 1190.27 | 717.80 |
| Friday    | 1340.68 | 741.91 |
| Saturday  | 1514.53 | 818.65 |

This suggests that casual riders primarily use the service for leisure activities, while members tend to take shorter, more purpose-driven trips.

---

### 2. Ride Frequency

Annual members take significantly more rides overall:

* Members: 3,605,025 rides
* Casual riders: 2,015,490 rides 


Members account for approximately 79% more rides, indicating a higher level of engagement and regular usage.

---

### 3. Weekly Usage Patterns

Number of Rides by Day

| Day       | Casual | Member |
|-----------|--------|--------|
| Sunday    | 338,260 | 387,426 |
| Monday    | 234,307 | 511,371 |
| Tuesday   | 227,855 | 580,928 |
| Wednesday | 224,333 | 562,336 |
| Thursday  | 259,660 | 581,378 |
| Friday    | 315,030 | 529,778 |
| Saturday  | 416,045 | 451,808 |

Distinct patterns emerge when comparing weekday and weekend usage:

* Members show peak activity during weekdays, particularly from Tuesday through Thursday
* Casual riders show peak activity on weekends, especially Saturday and Sunday

These trends indicate that members are more likely to use the service for commuting, while casual riders are more likely to use it for recreational purposes.

---

### 4. Consistency of Usage

Members maintain a relatively stable level of usage throughout the week, whereas casual rider activity fluctuates more significantly, increasing on weekends and decreasing during weekdays.

---

## Visualizations

The analysis is supported by the following visualizations:

* Average ride duration by day of the week (segmented by user type)
* Number of rides per day of the week (segmented by user type)

---

## Insights

* Members prioritize frequency and consistency of rides, suggesting routine usage such as commuting
* Casual riders prioritize longer ride durations, indicating leisure-oriented behavior
* There is a clear behavioral segmentation between weekday and weekend usage patterns

---

## Recommendations

### 1. Target Weekend Casual Riders

Our goal is to increase the number of members, by selling membership to casual riders. A good method would be to develop targeted marketing marketing campaigns aimed at weekend users, when casual rider activity is highest. Promotional messaging can focus on the benefits of membership for frequent riders.

### 2. Emphasize Cost Efficiency

Highlight the financial advantages of membership for users who ride frequently, particularly those who may transition from occasional to regular usage. One example would be to let casual members know after a certain number of rides, a membership would be cheaper.

### 3. Leverage Digital Marketing Channels

Deploy targeted digital campaigns during peak casual usage periods (e.g., weekends), using messaging that encourages conversion based on observed usage behavior.

### 4. Weekend Specific Memberships

Create a membership specifically for weekend users. For example, half the price of a membership but only can used on Friday to Sunday. It can also be used as a gateway from casual  to weekend only membership to the standard membership, especially for riders that sometimes ride during the weekdays.

---

## Conclusion

The analysis demonstrates clear behavioral differences between casual riders and annual members. Members use the service more frequently and consistently, likely for commuting, while casual riders engage in longer, leisure-based trips primarily on weekends. Effective conversion strategies should align with these existing behaviors to maximize the likelihood of increasing annual memberships. Effective strategies should align with existing behaviors, such as catering to them with specific memberships or deploy advertisements during peak casual periods, such as the weekends.

---

## Tools Used

* Python (Pandas for data processing)
* Data visualization libraries for analysis and reporting
