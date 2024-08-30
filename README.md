# Restaurant-Waste-Reduction

### Project Scope

The restaurant industry operates with notoriously thin operating margins, typically dropping around 5% of total revenue to their bottom lines. For every $1.00 in sales, approximately $0.30 - $0.35 will likely go to cost of goods (e.g. raw ingredients, dry goods, alcohol) while an additional $0.30 - $0.35 will go to labor, leaving roughly $0.30 - $0.40 to cover overhead (rent, insurance, utilities, equipment rentals, waste management, accounting, marketing) and provide a return on capital, to the extent there is any excess after covering all the costs.

An accurate sales forecast provides several avenues of cost saving + revenue expansion to restaurants:

* **Labor Optimization** | Minimize labor hours on slow nights while maintaining appropriate staffing levels on busier nights.
* **Minimize Food Waste** | More precise daily prep levels to help limit food waste.
* **Lean Inventory** | Inventory is a drag on cash flow and high levels of inventory of fresh goods can lead to spoilage and food waste.
* **Marketing Initiatives** | Maximize marketing dollars by targeting slow nights and weeks.

Using real sales data from a M Test Kitchen located in Cary, NC, this is a pilot project exploring what an end-to-end restaurant sales forecasting tool utilizing machine learning would entail.

### Data Sources
* **Restaurant Sales Data** | Restaurant sales and guest counts ("covers") were downloaded directly from the restuarant's Point of Sale ("POS") on a check-by-check basis from 6/1/2023 through 06/1/2024, then aggregated into nightly totals covering the dinner period only.

* **Reservations & Covers Data** | Reservations and covers data was downloaded directly from the restaurant's OpenTable platform. Opentable data was considered the ground truth for covers data, however only aggregate data was available. Total covers is equal to total OpenTable cover counts.
* TODO: Figure out how to differentiate indoor vs outdoor covers 

* **Weather Data** | Weather data was accessed via the Open-Meteo API, as of 7:30 PM each day. The source code for the API call can be found [here](https://github.com/byywork1/Restaurant-Waste-Reduction/blob/main/Weather/Weather_Daily.py). The latitude and longitude for the restuarant, required to access the weather data, is accessed via the Google.

### Repository Guide
* [Open-Meteo API Call](https://github.com/byywork1/Restaurant-Waste-Reduction/blob/main/Weather/Weather_Daily.py)
* TODO: Fill with links later 


### Restaurant Background

The subject is a contemporary american restaurant located in Cary, NC. It has a patio that almost doubles the total number of seats. 


