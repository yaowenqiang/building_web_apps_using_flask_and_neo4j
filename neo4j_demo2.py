from neo4j import GraphDatabase, RoutingControl
import neo4j
URI = "neo4j://localhost:7687"
AUTH = ("neo4j", "Ywq123456")

# https://neo4j.com/docs/api/python-driver/current/api.html#neo4j.graph.Relationship

with GraphDatabase.driver(URI, auth=AUTH) as driver:
    with driver.session(database="neo4j") as session:
        pandas_df = driver.execute_query(
            "UNWIND range(1, 10) AS n RETURN n, n+1 AS m",
            database_="neo4j",
            result_transformer_=neo4j.Result.to_df
        )

print(type(pandas_df))  # <class 'pandas.core.frame.DataFrame'>
