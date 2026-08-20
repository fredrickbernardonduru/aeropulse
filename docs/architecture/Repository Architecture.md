aeropulse/
│
├── README.md
├── LICENSE
├── .gitignore
├── .env.example
├── Makefile
├── docker-compose.yml
├── docker-compose.prod.yml
│
├── docs/
│   ├── architecture/
│   │   ├── system-architecture.md
│   │   ├── data-flow.md
│   │   ├── streaming-architecture.md
│   │   ├── lakehouse-architecture.md
│   │   ├── aws-architecture.md
│   │   └── ml-architecture.md
│   │
│   ├── data-dictionary/
│   │   ├── flights.md
│   │   ├── aircraft.md
│   │   ├── airports.md
│   │   └── weather.md
│   │
│   └── decisions/
│       ├── ADR-001-kafka.md
│       ├── ADR-002-flink.md
│       ├── ADR-003-iceberg.md
│       └── ADR-004-clickhouse.md
│
├── ingestion/
│   │
│   ├── opensky/
│   │   ├── __init__.py
│   │   ├── client.py
│   │   ├── config.py
│   │   ├── parser.py
│   │   └── producer.py
│   │
│   ├── weather/
│   │   ├── __init__.py
│   │   ├── client.py
│   │   ├── parser.py
│   │   └── producer.py
│   │
│   ├── historical/
│   │   ├── downloader.py
│   │   ├── validator.py
│   │   └── loader.py
│   │
│   └── common/
│       ├── schemas.py
│       ├── validation.py
│       └── logging.py
│
├── kafka/
│   ├── topics/
│   │   ├── flight-positions.json
│   │   ├── flight-status.json
│   │   ├── weather-events.json
│   │   └── airport-events.json
│   │
│   ├── producers/
│   ├── consumers/
│   ├── schemas/
│   └── create_topics.py
│
├── streaming/
│   │
│   └── flink/
│       ├── src/
│       │   ├── main/
│       │   │   └── python/
│       │   │       ├── jobs/
│       │   │       │   ├── flight_processing.py
│       │   │       │   ├── weather_processing.py
│       │   │       │   └── airport_processing.py
│       │   │       │
│       │   │       ├── operators/
│       │   │       ├── windows/
│       │   │       ├── aggregations/
│       │       └── anomaly_detection/
│       │
│       ├── tests/
│       ├── Dockerfile
│       └── requirements.txt
│
├── spark/
│   ├── jobs/
│   │   ├── historical_processing.py
│   │   ├── weather_enrichment.py
│   │   └── feature_generation.py
│   │
│   ├── transformations/
│   ├── schemas/
│   ├── tests/
│   └── Dockerfile
│
├── lakehouse/
│   │
│   ├── iceberg/
│   │   ├── bronze/
│   │   ├── silver/
│   │   └── gold/
│   │
│   ├── schemas/
│   │   ├── flight_schema.py
│   │   ├── weather_schema.py
│   │   └── airport_schema.py
│   │
│   └── catalog/
│       └── nessie/
│
├── dbt/
│   │
│   └── aeropulse/
│       ├── dbt_project.yml
│       ├── profiles.yml
│       │
│       ├── models/
│       │   │
│       │   ├── staging/
│       │   │   ├── stg_flights.sql
│       │   │   ├── stg_weather.sql
│       │   │   ├── stg_airports.sql
│       │   │   └── sources.yml
│       │   │
│       │   ├── intermediate/
│       │   │   ├── int_flight_weather.sql
│       │   │   ├── int_airport_operations.sql
│       │   │   └── int_flight_delays.sql
│       │   │
│       │   ├── marts/
│       │   │   ├── dim_airport.sql
│       │   │   ├── dim_aircraft.sql
│       │   │   ├── dim_airline.sql
│       │   │   ├── dim_route.sql
│       │   │   ├── fact_flights.sql
│       │   │   ├── fact_delays.sql
│       │   │   ├── fact_weather_impact.sql
│       │   │   └── fact_airport_operations.sql
│       │   │
│       │   └── analytics/
│       │       ├── mart_airline_performance.sql
│       │       ├── mart_airport_performance.sql
│       │       ├── mart_route_performance.sql
│       │       └── mart_delay_analysis.sql
│       │
│       ├── macros/
│       ├── tests/
│       ├── seeds/
│       └── snapshots/
│
├── airflow/
│   │
│   ├── dags/
│   │   ├── ingest_flight_data.py
│   │   ├── ingest_weather_data.py
│   │   ├── historical_flight_pipeline.py
│   │   ├── lakehouse_maintenance.py
│   │   ├── dbt_pipeline.py
│   │   └── ml_training_pipeline.py
│   │
│   ├── plugins/
│   ├── config/
│   └── tests/
│
├── ml/
│   │
│   ├── data/
│   │   ├── feature_engineering.py
│   │   └── dataset_builder.py
│   │
│   ├── models/
│   │   ├── delay_prediction.py
│   │   └── anomaly_detection.py
│   │
│   ├── training/
│   │   ├── train.py
│   │   ├── evaluate.py
│   │   └── hyperparameter_tuning.py
│   │
│   ├── inference/
│   │   └── predictor.py
│   │
│   └── mlflow/
│       └── config.py
│
├── api/
│   │
│   ├── app/
│   │   ├── main.py
│   │   ├── config.py
│   │   ├── routes/
│   │   │   ├── flights.py
│   │   │   ├── airports.py
│   │   │   ├── analytics.py
│   │   │   └── predictions.py
│   │   ├── services/
│   │   └── models/
│   │
│   ├── tests/
│   └── Dockerfile
│
├── dashboards/
│   │
│   ├── grafana/
│   │   ├── dashboards/
│   │   │   ├── flight-operations.json
│   │   │   ├── airport-congestion.json
│   │   │   └── system-health.json
│   │   └── provisioning/
│   │
│   └── superset/
│       ├── dashboards/
│       └── datasets/
│
├── data-quality/
│   ├── great_expectations/
│   ├── dbt_tests/
│   └── checks/
│
├── observability/
│   ├── prometheus/
│   ├── grafana/
│   ├── alerts/
│   └── logging/
│
├── infrastructure/
│   │
│   ├── terraform/
│   │   ├── modules/
│   │   │   ├── networking/
│   │   │   ├── kafka/
│   │   │   ├── s3/
│   │   │   ├── iam/
│   │   │   ├── ecs/
│   │   │   └── monitoring/
│   │   │
│   │   ├── environments/
│   │   │   ├── dev/
│   │   │   └── prod/
│   │   │
│   │   └── main.tf
│   │
│   └── kubernetes/
│       ├── namespaces/
│       ├── kafka/
│       ├── flink/
│       ├── spark/
│       ├── airflow/
│       ├── api/
│       └── monitoring/
│
├── scripts/
│   ├── setup.sh
│   ├── init.sh
│   ├── create_topics.sh
│   ├── health_check.sh
│   └── teardown.sh
│
├── tests/
│   ├── unit/
│   ├── integration/
│   ├── data/
│   └── end_to_end/
│
└── .github/
    └── workflows/
        ├── ci.yml
        ├── tests.yml
        ├── dbt.yml
        ├── docker.yml
        └── deploy.yml