from pyspark import SparkContext

def parse_line(line):
    parts = line.strip().split()
    user_id = parts[0]
    name = parts[1]
    friends = parts[2].split(',') if len(parts) > 2 else []
    return user_id, name, friends

def generate_pairs(user_id, friends):
    pairs = []
    for friend_id in friends:
        key = tuple(sorted([user_id, friend_id]))
        pairs.append((key, set(friends)))
    return pairs

if __name__ == "__main__":
    sc = SparkContext("local", "MutualFriends")

    # Charger les données
    data = sc.textFile("data/friends.txt")
    
    # Associer ID et Nom
    user_names = data.map(lambda line: (line.split()[0], line.split()[1])).collectAsMap()
    
    # Parser chaque ligne : (user_id, friends)
    parsed = data.map(lambda line: parse_line(line))  # (user_id, name, friends_list)

    # Générer tous les couples triés
    pairs = parsed.flatMap(lambda x: generate_pairs(x[0], x[2]))

    # Grouper les paires et faire intersection
    mutuals = pairs.reduceByKey(lambda x, y: x.intersection(y))

    # Filtrer pour Mohamed (2) et Sidi (1)
    target_pair = tuple(sorted(['1', '2']))  # => ('1', '2')
    result = mutuals.filter(lambda x: x[0] == target_pair).collect()

    # Afficher la sortie
    for pair, friends in result:
        uid1, uid2 = pair
        name1 = user_names[uid1]
        name2 = user_names[uid2]
        common_names = [user_names[fid] for fid in friends if fid in user_names]
        print(f"{uid1}<{name1}>{uid2}<{name2}> : {common_names}")

    sc.stop()
