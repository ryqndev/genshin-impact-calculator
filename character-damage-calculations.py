import json

"""
c - character stats variable
"""
def calculate_damage(path: str):
    c = read_stats_from(path)
    base_atk = stat('atk', c) + stat('atk', c['weapon'])
    percent_atk = stat('atk_percentage', c) + stat('atk_percentage', c['weapon'])

    print("Base Attack:", base_atk)

    artifact_atk = artifact_percent_atk = 0
    for artifact in c['artifacts']:
        artifact_atk += stat('atk', artifact)
        artifact_percent_atk += stat('atk_percentage', artifact)

    print("Artifacts Base Attack:", artifact_atk)
    print("Artifacts Attack Percentage:", artifact_percent_atk, "%")

    artifact_percent_atk_bonus = base_atk * (artifact_percent_atk / 100)

    print("Bonus Attack from Percentage Stats:", artifact_percent_atk_bonus)

    final_atk = base_atk + artifact_percent_atk_bonus + artifact_atk

    print("Final Damage Score:", final_atk)

def read_stats_from(path: str):
    with open(path) as json_file:
        data = json.load(json_file)
        return data

def stat(stat_name: str, stats: dict, default_value: int=0):
    return stats['stats'].get(stat_name, default_value)

def write_stats_to(path: str):
    with open(path, 'w') as outfile:
        json.dump(data, outfile)

if __name__ == "__main__":
    calculate_damage('./assets/fischl.json')