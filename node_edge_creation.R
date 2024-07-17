### GRAPH CREATION

library(skimr)
library(car)
library(arm)
library(rpart.plot)
library(dplyr)
library(readxl)
library(tidyverse)
library(tidyr)

getwd()
setwd("/Users/ali/Desktop/ctti/datasets")
df<-read.csv2("comerç_bcn.csv", sep=",")
names(df)
df
random_indices <- sample(1:nrow(df), 10000)
df <- df[random_indices, ]
df

# Barri- Districte
df[c("Nom_Barri","Nom_Districte")]
Edge_barri_districte <- df %>% distinct(Nom_Barri, Nom_Districte)

getwd()
setwd("/Users/ali/Library/Application Support/Neo4j Desktop/Application/projects/project-b8a8f6ee-b838-4364-a30a-787cadaca67d")
write.csv(Edge_barri_districte, file = "Edge_barri_districte.csv", row.names = FALSE,  quote = FALSE)

Node_districte<- unique(Edge_barri_districte[,2])
write.csv(Node_districte, "Node_districte.csv", row.names = FALSE) 

Node_barri<- unique(Edge_barri_districte[,1])
write.csv(Node_barri, "Node_barri.csv", row.names = FALSE) 

# Sector - Barri
table(df$Nom_Sector_Activitat)
df[c("Nom_Barri","Nom_Sector_Activitat")]

Edge_barri_sector <- df %>% distinct(Nom_Barri, Nom_Sector_Activitat)
write.csv(Edge_barri_sector, file = "Edge_barri_sector.csv", row.names = FALSE,  quote = FALSE)

Node_sector<- unique(Edge_barri_sector[,2])
write.csv(Node_sector, "Node_sector.csv", row.names = FALSE) 

# Sector - Grup

df[c("Nom_Sector_Activitat","Nom_Grup_Activitat")]
Edge_sector_grup <- df %>% distinct(Nom_Sector_Activitat, Nom_Grup_Activitat)
write.csv(Edge_sector_grup, file = "Edge_sector_grup.csv", row.names = FALSE,  quote = FALSE)

Node_grup<- unique(Edge_sector_grup[,2])
write.csv(Node_grup, "Node_grup.csv", row.names = FALSE) 

# Grup - Activitat

df[c("Nom_Grup_Activitat","Nom_Activitat")]
Edge_grup_activitat <- df %>% distinct(Nom_Grup_Activitat, Nom_Activitat)
write.csv(Edge_grup_activitat, file = "Edge_grup_activitat.csv", row.names = FALSE,  quote = FALSE)

Node_activitat<- unique(Edge_grup_activitat[,2])
write.csv(Node_activitat, "Node_activitat.csv", row.names = FALSE) 


# Nom_Via - Barri

df[c("Nom_Barri","Nom_Via")]

Edge_barri_via <- df %>% distinct(Nom_Barri, Nom_Via)
write.csv(Edge_barri_via, file = "Edge_barri_via.csv", row.names = FALSE,  quote = FALSE)

Node_via<- unique(Edge_barri_via[,2])
write.csv(Node_via, "Node_via.csv", row.names = FALSE) 

# Nom_Via - Local  

df[c("Nom_Via","Nom_Local")]
Edge_via_local <- df %>% distinct(Nom_Via, Nom_Local)
random_indices <- sample(1:nrow(Edge_via_local), 5000)
Edge_via_local <- Edge_via_local[random_indices, ]
Edge_via_local
write.csv(Edge_via_local, file = "Edge_via_local.csv", row.names = FALSE,  quote = FALSE)
Node_local<- unique(Edge_via_local[,2])
write.csv(Node_local, "Node_local.csv", row.names = FALSE) 

# Activitat - Local
