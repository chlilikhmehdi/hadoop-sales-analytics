# Hadoop Sales Analytics

**Projet Big Data – Analyse distribuée des ventes avec Apache Hadoop, HDFS, YARN et Python**

## Présentation du projet

Hadoop Sales Analytics est un projet de traitement et d'analyse de données volumineuses basé sur l'écosystème Apache Hadoop.

L'objectif est de mettre en place un pipeline Big Data permettant de stocker, traiter et analyser des données commerciales à travers plusieurs traitements distribués développés en Python avec Hadoop Streaming.

Le projet exploite HDFS pour le stockage distribué et MapReduce pour effectuer des analyses telles que le calcul du chiffre d'affaires, l'identification des meilleurs clients et l'analyse des ventes par produit, ville et période.

## Objectifs

- Découvrir et mettre en pratique l'écosystème Hadoop.
- Stocker des fichiers CSV dans HDFS.
- Développer des traitements distribués avec Python.
- Exécuter des Jobs MapReduce avec Hadoop Streaming.
- Comprendre la gestion des ressources avec YARN.
- Optimiser les traitements avec Combiner et plusieurs Reducers.
- Vérifier et comparer les résultats obtenus.

## Technologies utilisées

| Technologie | Utilisation |
|---|---|
| Apache Hadoop 3.3.6 | Framework Big Data |
| HDFS | Stockage distribué |
| MapReduce | Traitement distribué |
| Hadoop Streaming | Exécution des scripts Python |
| Python 3 | Développement des Mappers et Reducers |
| YARN | Gestion des ressources et des Jobs |
| Java 11 | Environnement d'exécution Hadoop |
| macOS | Environnement de développement |

## Architecture du projet

```text
             Fichiers CSV
                  |
                  v
             Apache HDFS
                  |
                  v
          Hadoop Streaming
                  |
          +-------+-------+
          |               |
          v               v
        Mapper          Python
          |               |
          +-------+-------+
                  |
                  v
              Combiner
             (si pertinent)
                  |
                  v
               Shuffle
              & Sort
                  |
                  v
               Reducer
                  |
                  v
             Résultats HDFS
                  |
                  v
              Analyse
             et validation
```

YARN intervient dans l'exécution des applications et la gestion des ressources du cluster.

## Analyses réalisées

Le projet comprend neuf traitements MapReduce :

| # | Analyse | Description |
|---|---|---|
| 1 | Revenue by Seller | Calcul du chiffre d'affaires par vendeur |
| 2 | Revenue by City | Calcul du chiffre d'affaires par ville |
| 3 | Revenue by Product | Calcul du chiffre d'affaires par produit |
| 4 | Monthly Analysis | Analyse des ventes par mois |
| 5 | Transactions by Client | Nombre de transactions par client |
| 6 | Top Clients | Identification des 10 meilleurs clients |
| 7 | Best Selling Products | Identification des produits les plus vendus |
| 8 | Sales by Category | Analyse des ventes par catégorie |
| 9 | Transactions by Status | Répartition des transactions par statut |

Certaines analyses nécessitent des fichiers de référence, notamment les données clients et produits.

## Structure du projet

```text
hadoop-sales-analytics/
│
├── data/
│   ├── transactions/
│   ├── clients/
│   ├── produits/
│   └── vendeurs/
│
├── src/
│   ├── revenue_by_seller/
│   │   ├── mapper.py
│   │   └── reducer.py
│   │
│   ├── revenue_by_city/
│   ├── revenue_by_product/
│   ├── monthly_analysis/
│   ├── transactions_by_client/
│   ├── top_clients/
│   ├── best_selling_products/
│   ├── sales_by_category/
│   └── transactions_by_status/
│
├── scripts/
│
├── results/
│
├── README.md
└── .gitignore
```

Chaque dossier d'analyse contient un Mapper et un Reducer indépendants.

## Prérequis

Avant de lancer le projet, installer :

- Java JDK 11
- Apache Hadoop 3.3.6
- Python 3
- Hadoop Streaming

Vérifier les installations :

```bash
java -version
python3 --version
hadoop version
```

Définir les variables d'environnement Hadoop :

```bash
export HADOOP_HOME="$HOME/hadoop/hadoop-3.3.6"
export PATH="$HADOOP_HOME/bin:$HADOOP_HOME/sbin:$PATH"
```

Localiser Hadoop Streaming :

```bash
export STREAMING_JAR=$(find "$HADOOP_HOME/share/hadoop/tools/lib" \
-name "hadoop-streaming*.jar" | head -n 1)
```

## Installation et démarrage

### 1. Cloner le repository

```bash
git clone https://github.com/VOTRE_USERNAME/hadoop-sales-analytics.git

cd hadoop-sales-analytics
```

### 2. Démarrer HDFS

```bash
start-dfs.sh
```

### 3. Démarrer YARN

```bash
start-yarn.sh
```

### 4. Vérifier les services

```bash
jps
```

Les principaux processus attendus sont :

- NameNode
- DataNode
- SecondaryNameNode
- ResourceManager
- NodeManager

### 5. Préparer les répertoires HDFS

```bash
hdfs dfs -mkdir -p /sales-analytics/input/transactions
hdfs dfs -mkdir -p /sales-analytics/input/clients
hdfs dfs -mkdir -p /sales-analytics/input/produits
hdfs dfs -mkdir -p /sales-analytics/input/vendeurs
```

Les fichiers CSV doivent être placés dans les répertoires HDFS correspondants avant l'exécution des traitements.

### 6. Vérifier les données

```bash
hdfs dfs -ls -R /sales-analytics/input
```

## Exécution d'un Job MapReduce

Exemple : calcul du chiffre d'affaires par vendeur.

```bash
hadoop jar "$STREAMING_JAR" \
-files src/revenue_by_seller/mapper.py,src/revenue_by_seller/reducer.py \
-mapper "python3 mapper.py" \
-reducer "python3 reducer.py" \
-input /sales-analytics/input/transactions \
-output /sales-analytics/output/revenue_by_seller
```

### Consulter les résultats

```bash
hdfs dfs -cat "/sales-analytics/output/revenue_by_seller/part-*"
```

Chaque analyse possède son propre répertoire de sortie dans HDFS.

## Exploitation de YARN

Afficher les applications :

```bash
yarn application -list -appStates ALL
```

Consulter le statut d'une application :

```bash
yarn application -status APPLICATION_ID
```

Consulter les logs :

```bash
yarn logs -applicationId APPLICATION_ID
```

Interface Web YARN :

http://localhost:8088

Interface Web HDFS :

http://localhost:9870

## Optimisation des traitements

Plusieurs techniques d'optimisation sont étudiées dans ce projet :

- **Combiner :** effectuer une agrégation locale avant l'envoi des données aux Reducers, lorsque l'opération le permet.
- **Multiple Reducers :** répartir le traitement entre plusieurs Reducers.
- **Partitioning :** distribuer les clés entre les Reducers.
- **Performance Analysis :** comparer les durées d'exécution des traitements.
- **Data Processing Optimization :** éviter les opérations et lectures inutiles.

## Vérification des résultats

Les résultats Hadoop peuvent être récupérés localement :

```bash
hdfs dfs -getmerge \
/sales-analytics/output/revenue_by_seller \
results/revenue_by_seller.txt
```

Une comparaison avec un calcul de référence local permet de vérifier la cohérence des résultats :

```bash
diff -u results/revenue_by_seller_local.txt \
results/revenue_by_seller.txt
```

## Compétences développées

- Big Data Fundamentals
- Distributed Data Processing
- Apache Hadoop Ecosystem
- HDFS Administration
- MapReduce Programming
- Python Data Processing
- Hadoop Streaming
- YARN Resource Management
- Data Aggregation
- Performance Optimization

## Auteur

**El Mehdi Chlilikh**

Étudiant ingénieur en Génie Informatique – Data Science et Intelligence Artificielle.


---

*Projet pédagogique réalisé dans le cadre de l'apprentissage du Big Data et du Data Engineering.*
