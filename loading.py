
from neo4j_classes import Neo4jConnection
from neo4jconfig import NEO4J_URI, NEO4J_USERNAME, NEO4J_PASSWORD, BASE_URL

# Neo4j connection parameters
uri = NEO4J_URI  
username = NEO4J_USERNAME        
password = NEO4J_PASSWORD
base_url = BASE_URL

def main():
    # Connect to Neo4j
    connection = Neo4jConnection(uri, username, password)
     
    # Queries to execute, formatted for readability
    queries = [

        f"""
        MATCH (n)
        DETACH DELETE n
        """,

        f"""
        LOAD CSV WITH HEADERS FROM '{base_url}/Node_barri.csv' AS row
        MERGE (a:Barri {{name: row.x}})
        """,

        f"""
        LOAD CSV WITH HEADERS FROM '{base_url}/Node_districte.csv' AS row
        MERGE (b:Districte {{name: row.x}})
        """,

        f"""
        LOAD CSV WITH HEADERS FROM '{base_url}/Node_sector.csv' AS row
        MERGE (c:Sector {{name: row.x}})
        """,

        f"""
        LOAD CSV WITH HEADERS FROM '{base_url}/Node_grup.csv' AS row
        MERGE (d:Grup {{name: row.x}})
        """,

        f"""
        LOAD CSV WITH HEADERS FROM '{base_url}/Node_activitat.csv' AS row
        MERGE (e:Activitat {{name: row.x}})
        """,

        f"""
        LOAD CSV WITH HEADERS FROM '{base_url}/Node_via.csv' AS row
        MERGE (f:Via {{name: row.x}})
        """,

        f"""
        LOAD CSV WITH HEADERS FROM '{base_url}/Node_local.csv' AS row
        MERGE (g:Local {{name: row.x}})
        """,


        f"""
        LOAD CSV WITH HEADERS FROM '{base_url}/Edge_barri_districte.csv' AS row
        MATCH (a:Barri {{name: row.Nom_Barri}})
        MATCH (b:Districte {{name: row.Nom_Districte}})
        MERGE (a)-[r:PERTANY]->(b);
        """,


        f"""
        LOAD CSV WITH HEADERS FROM '{base_url}/Edge_sector_grup.csv' AS row
        MATCH (c:Sector {{name: row.Nom_Sector_Activitat}})
        MATCH (d:Grup {{name: row.Nom_Grup_Activitat}})
        MERGE (c)-[r:GRUP]->(d);
        """,

        f"""
        LOAD CSV WITH HEADERS FROM '{base_url}/Edge_grup_activitat.csv' AS row
        MATCH (d:Grup {{name: row.Nom_Grup_Activitat}})
        MATCH (e:Activitat {{name: row.Nom_Activitat}})
        MERGE (d)-[r:ACTIVITAT]->(e);
        """,

        f"""
        LOAD CSV WITH HEADERS FROM '{base_url}/Edge_barri_via.csv' AS row
        MATCH (a:Barri {{name: row.Nom_Barri}})
        MATCH (f:Via {{name: row.Nom_Via}})
        MERGE (a)-[r:VIA]->(f);
        """,

        f"""
        LOAD CSV WITH HEADERS FROM '{base_url}/Edge_via_local.csv' AS row
        MATCH (f:Via {{name: row.Nom_Via}})
        MATCH (g:Local {{name: row.Nom_Local}})
        MERGE (f)-[r:LOCAL]->(g);
        """

    ]

    # Execute each query, respecting the readable formatting
    for i, query in enumerate(queries, start=1):
        print(f"Executing Query {i}...")
        connection.load_csv_data(query)

    connection.close()

if __name__ == '__main__':
    main()



#### queries

# MATCH (s:Sector )-[r:GRUP]-(G:Grup)
# RETURN s,r,G

## MATCH (b:Barri )-[p:PERTANY]-(d:Districte)
# RETURN b,p,d


#MATCH (b:Via )-[p:LOCAL]-(d:Local)
#RETURN b,p,d