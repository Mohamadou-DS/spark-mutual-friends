# 🔗 PySpark - Détection d’Amis Communs

## 🎯 Objectif

Ce projet utilise Apache Spark pour analyser un graphe social et détecter les amis communs entre deux utilisateurs spécifiés. On applique ici les concepts de **MapReduce**, **RDDs**, et **filtrage distribué**.

---

## 📁 Structure

spark-mutual-friends/
├── data/
│ └── friends.txt # Données d'entrée
├── src/
│ └── mutual_friends.py # Code Spark
├── results/
│ └── output.txt # Résultats


---

## 💾 Données

Le fichier `friends.txt` est structuré comme suit :

<user_id> <Nom> <friend_id1> <friend_id2>,...

Exemple :

1 Sidi 2,3,4
2 Mohamed 1,3,5


---

## ⚙️ Exécution

```bash
# Depuis le dossier du projet
$ pyspark src/mutual_friends.py

1<Sidi>2<Mohamed> : ['Ahmed']



🧪 Jeu de test
Vous pouvez modifier friends.txt pour tester d’autres cas de figure.



👨‍💻 Auteur
Projet réalisé dans le cadre du TP Spark – M1 IA 2025.

Par Ba Mohamadou Adama - C20509

---