                              AEROPULSE
                 REAL-TIME AVIATION INTELLIGENCE
                                 │
     ┌───────────────────────────┴────────────────────────────┐
     │                                                        │
     ▼                                                        ▼
 DATA SOURCES                                           HISTORICAL DATA
     │                                                        │
     ├── OpenSky                                               │
     ├── Weather API                                           │
     └── Airport APIs                                          │
     │                                                        │
     ▼                                                        ▼
 PYTHON INGESTION                                          AIRFLOW
     │                                                        │
     ▼                                                        ▼
   KAFKA                                                     SPARK
     │                                                        │
     │                                                        │
     ▼                                                        ▼
   FLINK ───────────────────────────────────────────────► ICEBERG
     │                                                      │
     ├── Validation                                         │
     ├── Enrichment                                         │
     ├── Windows                                            │
     ├── Aggregations                                       │
     └── Anomalies                                          │
     │                                                      │
     │                                              ┌───────┴───────┐
     │                                              │               │
     ▼                                              ▼               ▼
 CLICKHOUSE                                       BRONZE         CATALOG
     │                                              │            Nessie
     │                                              ▼
     │                                            SILVER
     │                                              │
     │                                              ▼
     │                                             GOLD
     │                                              │
     │                                              ▼
     │                                            TRINO
     │                                              │
     │                                              ▼
     │                                             DBT
     │                                              │
     │                              ┌───────────────┼───────────────┐
     │                              │               │               │
     │                              ▼               ▼               ▼
     │                            FACTS         DIMENSIONS        MARTS
     │                              │               │               │
     └──────────────────────────────┴───────────────┼───────────────┘
                                                    │
                                                    ▼
                                               ANALYTICS
                                                    │
                                  ┌─────────────────┼─────────────────┐
                                  │                 │                 │
                                  ▼                 ▼                 ▼
                               GRAFANA           SUPERSET          FASTAPI
                                  │                 │                 │
                                  │                 │                 ▼
                                  │                 │               REDIS
                                  │                 │                 │
                                  │                 │                 ▼
                                  │                 │              USERS
                                  │                 │
                                  └─────────────────┘


                         MACHINE LEARNING LAYER
                                  │
                              ICEBERG/GOLD
                                  │
                                  ▼
                         FEATURE ENGINEERING
                                  │
                                  ▼
                              XGBOOST
                                  │
                                  ▼
                              MLFLOW
                                  │
                           MODEL REGISTRY
                                  │
                                  ▼
                              FASTAPI
                                  │
                                  ▼
                         DELAY PREDICTIONS


                         OBSERVABILITY
                                  │
             ┌────────────────────┼────────────────────┐
             ▼                    ▼                    ▼
          PROMETHEUS           GRAFANA             ALERTING
             │                    │
             └────────────────────┘


                         INFRASTRUCTURE
                                  │
                     ┌────────────┴────────────┐
                     ▼                         ▼
                LOCAL DEV                    CLOUD
              Docker Compose                 AWS
                     │                         │
                     │                    Terraform
                     │                         │
                     │                      EKS/ECS
                     │                         │
                     └────────────┬────────────┘
                                  ▼
                             PRODUCTION