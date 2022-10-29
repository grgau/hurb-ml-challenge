# Machine Learning Challenge - Platform

## How to run the application
---
### Docker environment (Advisable! 😉)
Run inside the project directory:
```
docker-compose up
```

The prediction service served by Bentoml will be up with an already trained Catboost model. Also, an MLFlow service will be up to register model's metrics

---
### Without Docker environment
Create and activate a virtual env:
```
python3.10 -m venv venv
source venv/bin/activate
```

Install the requirements
```
pip install -r requirements.txt
```

Load the env file
```
source .env
```

Run the application:
```
mlflow server --host 0.0.0.0 & bash docker-entrypoint.sh
```

---
---
## How to use the API to get predictions

After the project is running, the endpoint `http://localhost:3000/classify` will be available to POST requests, the JSON body needs to have the following structure:

```json
{
    "hotel": ["Resort Hotel", "City Hotel"],
    "lead_time": int,
    "arrival_date_year": [2015, 2016, 2017],
    "arrival_date_month": ["July", "August", "September", "October", "November", "December", "January", "February", "March", "April", "May", "June"],
    "arrival_date_week_number": int,
    "arrival_date_day_of_month": int,
    "stays_in_weekend_nights": int,
    "stays_in_week_nights": int,
    "adults": int,
    "children": int,
    "babies": int,
    "meal": ["BB", "FB", "HB", "SC"],
    "country": ["PRT", "GBR", "USA", "ESP", "IRL", "FRA", "ROU", "NOR", "OMN", "ARG", "POL", "DEU", "BEL", "CHE", "CN", "GRC", "ITA", "NLD", "DNK", "RUS", "SWE", "AUS", "EST", "CZE", "BRA", "FIN", "MOZ", "BWA", "LUX", "SVN", "ALB", "IND", "CHN", "MEX", "MAR", "UKR", "SMR", "LVA", "PRI", "SRB", "CHL", "AUT", "BLR", "LTU", "TUR", "ZAF", "AGO", "ISR", "CYM", "ZMB", "CPV", "ZWE", "DZA", "KOR", "CRI", "HUN", "ARE", "TUN", "JAM", "HRV", "HKG", "IRN", "GEO", "AND", "GIB", "URY", "JEY", "CAF", "CYP", "COL", "GGY", "KWT", "NGA", "MDV", "VEN", "SVK", "FJI", "KAZ", "PAK", "IDN", "LBN", "PHL", "SEN", "SYC", "AZE", "BHR", "NZL", "THA", "DOM", "MKD", "MYS", "ARM", "JPN", "LKA", "CUB", "CMR", "BIH", "MUS", "COM", "SUR", "UGA", "BGR", "CIV", "JOR", "SYR", "SGP", "BDI", "SAU", "VNM", "PLW", "QAT", "EGY", "PER", "MLT", "MWI", "ECU", "MDG", "ISL", "UZB", "NPL", "BHS", "MAC", "TGO", "TWN", "DJI", "STP", "KNA", "ETH", "IRQ", "HND", "RWA", "KHM", "MCO", "BGD", "IMN", "TJK", "NIC", "BEN", "VGB", "TZA", "GAB", "GHA", "TMP", "GLP", "KEN", "LIE", "GNB", "MNE", "UMI", "MYT", "FRO", "MMR", "PAN", "BFA", "LBY", "MLI", "NAM", "BOL", "PRY", "BRB", "ABW", "AIA", "SLV", "DMA", "PYF", "GUY", "LCA", "ATA", "GTM", "ASM", "MRT", "NCL", "KIR", "SDN", "ATF", "SLE", "LAO"],
    "market_segment": ["Direct", "Corporate", "Online TA", "Offline TA/TO", "Complementary", "Groups", "Aviation"],
    "distribution_channel": ["Direct", "Corporate", "TA/TO", "GDS"],
    "is_repeated_guest": [0, 1],
    "previous_cancellations": int,
    "previous_bookings_not_canceled": int,
    "reserved_room_type": ["C", "A", "D", "E", "G", "F", "H", "L", "P", "B"],
    "assigned_room_type": ["C", "A", "D", "E", "G", "F", "I", "B", "H", "P", "L", "K"],
    "booking_changes": int,
    "deposit_type": ["No Deposit", "Refundable", "Non Refund"],
    "agent": float,
    "company": float,
    "days_in_waiting_list": int,
    "customer_type": ["Transient", "Contract", "Transient-Party", "Group"],
    "adr": float,
    "required_car_parking_spaces": int,
    "total_of_special_requests": int,
    "reservation_status": ["Check-Out", "Canceled", "No-Show"],
    "reservation_status_date": ["YYYY-MM-DD"]
}
```

For example:
```json
{
    "hotel": "Resort Hotel",
    "lead_time": 342,
    "arrival_date_year": 2015,
    "arrival_date_month": "July",
    "arrival_date_week_number": 27,
    "arrival_date_day_of_month": 1,
    "stays_in_weekend_nights": 0,
    "stays_in_week_nights": 0,
    "adults": 2,
    "children": 0, 
    "babies": 0,
    "meal": "BB",
    "country": "PRT",
    "market_segment": "Direct",
    "distribution_channel": "Direct",
    "is_repeated_guest": 0,
    "previous_cancellations": 0,
    "previous_bookings_not_canceled": 0,
    "reserved_room_type": "D",
    "assigned_room_type": "C",
    "booking_changes": 3,
    "deposit_type": "No Deposit",
    "agent": 304.0,
    "company": 64.0, 
    "days_in_waiting_list": 0,
    "customer_type": "Transient",
    "adr": 0.0,
    "required_car_parking_spaces": 0,
    "total_of_special_requests": 0,
    "reservation_status": "Check-Out",
    "reservation_status_date": "2015-07-01"
}
```

The model response through the API will be like:
```json
{
	"will_cancel": false
}
```