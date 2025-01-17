import numpy as np

tile_size = np.linspace(0.1,0.5, num=7)
match_score = np.linspace(60,100, num=7).astype(int)
Prev_length = np.linspace(30,120, num=7).astype(int)
Prev_type = ["TT","AC"]

sample_size = 36

combinations = {}
for ts in tile_size:
    for ms in match_score:
        for pl in Prev_length:
            for pt in Prev_type:
                combinations[f"Tile.Size:{ts}, Match.Score:{ms}, Prev.Length:{pl}, Prev.Type:{pt}, Sample.Size:{sample_size}"] = [ts,ms,pl,pt,sample_size]

terms = len(combinations)

with open(f"NSTEVENS.csv", "w") as file:
    file.write("Tile.Size,Match.Score,Prev.Length,Prev.Type,Sample.Size\n")
    
    for values in combinations.values():
        file.write(",".join(map(str, values)) + "\n")
