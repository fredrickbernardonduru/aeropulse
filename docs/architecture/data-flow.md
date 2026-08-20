OpenSky
   │
   ▼
Python Collector
   │
   ▼
Kafka
   │
   ├───────────────┐
   │               │
   ▼               ▼
Flink           Kafka Consumer
   │               │
   ▼               ▼
Validation      Monitoring
   │
   ▼
Enrichment
   │
   ├───────────────┐
   │               │
   ▼               ▼
ClickHouse      Iceberg
   │               │
   │               ▼
   │             Bronze
   │               │
   │               ▼
   │             Silver
   │               │
   │               ▼
   │              Gold
   │
   ▼
Grafana






Bath Data Flow 
Historical Data
      │
      ▼
    Airflow
      │
      ▼
    Python
      │
      ▼
    Spark
      │
      ├── Validate
      ├── Clean
      ├── Deduplicate
      ├── Enrich
      └── Transform
      │
      ▼
 Apache Iceberg
      │
      ▼
    Trino
      │
      ▼
     dbt
      │
      ▼
 Analytics Marts
      │
      ▼
 ClickHouse
      │
      ▼
  Superset