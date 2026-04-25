# Cyclistic Bike-Share Analysis

## Business Task

The objective of this analysis is to examine how **casual riders** and **annual members** use Cyclistic bikes differently. These insights are intended to support the development of marketing strategies aimed at converting casual riders into annual members.

---

## Dataset

* Source: Cyclistic historical trip data (public dataset)
* Timeframe: 12 months
* Key variables:

  * `member_casual` (user type)
  * `ride_length` (ride duration)
  * `day_of_week`

---

## Data Processing

The dataset was cleaned and prepared to ensure accuracy and consistency:

* Removed invalid or negative ride durations
* Created derived fields:

  * `ride_length` (calculated from timestamps)
  * `day_of_week`
* Aggregated data by user type and day of the week for analysis

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

Develop targeted marketing campaigns aimed at weekend users, when casual rider activity is highest. Promotional messaging can focus on the benefits of membership for frequent riders.

### 2. Emphasize Cost Efficiency

Highlight the financial advantages of membership for users who ride frequently, particularly those who may transition from occasional to regular usage.

### 3. Leverage Digital Marketing Channels

Deploy targeted digital campaigns during peak casual usage periods (e.g., weekends), using messaging that encourages conversion based on observed usage behavior.

---

## Conclusion

The analysis demonstrates clear behavioral differences between casual riders and annual members. Members use the service more frequently and consistently, likely for commuting, while casual riders engage in longer, leisure-based trips primarily on weekends. Effective conversion strategies should align with these existing behaviors to maximize the likelihood of increasing annual memberships.

---

## Tools Used

* Python (Pandas for data processing)
* Data visualization libraries for analysis and reporting
