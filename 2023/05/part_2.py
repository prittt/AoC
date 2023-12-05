
import sys

def do(data):
    
    seeds = data[0].split(":")[1].split()
    
    if True:
        seed_to_soil_map = []
        for i in range (3, 5):
        # for i in range (3, 5):
            seed_to_soil_map.append(data[i].split())
        
        soil_to_fertilizer_map = []
        for i in range (7, 10):
            soil_to_fertilizer_map.append(data[i].split())
        

        fertilizer_to_water_map = []
        for i in range (12, 16):
            fertilizer_to_water_map.append(data[i].split())
        
        water_to_ligh_map = []
        for i in range (18, 20):
            water_to_ligh_map.append(data[i].split())
        
        light_to_temp_map = []
        for i in range (22, 25):
            light_to_temp_map.append(data[i].split())
    
        temperature_to_humidity_map = []
        for i in range (27, 29):
            temperature_to_humidity_map.append(data[i].split())

        humidity_to_location_map = []
        for i in range (31, 33):
            humidity_to_location_map.append(data[i].split())
    else:
        seed_to_soil_map = []
        for i in range (3, 47):
        # for i in range (3, 5):
            seed_to_soil_map.append(data[i].split())
        
        soil_to_fertilizer_map = []
        for i in range (49, 71):
            soil_to_fertilizer_map.append(data[i].split())
        

        fertilizer_to_water_map = []
        for i in range (73, 113):
            fertilizer_to_water_map.append(data[i].split())
        
        water_to_ligh_map = []
        for i in range (115, 158):
            water_to_ligh_map.append(data[i].split())
        
        light_to_temp_map = []
        for i in range (160, 194):
            light_to_temp_map.append(data[i].split())
    
        temperature_to_humidity_map = []
        for i in range (196, 241):
            temperature_to_humidity_map.append(data[i].split())

        humidity_to_location_map = []
        for i in range (243, 277):
            humidity_to_location_map.append(data[i].split())


    min_pos = sys.maxsize
    i = 0
    while i < len(seeds):
        
        start = int(seeds[i])
        end = int(seeds[i]) + int(seeds[i + 1])
        
        ranges = [(start, end)]

        # seed = int(seed)
        mappings = [seed_to_soil_map, soil_to_fertilizer_map, fertilizer_to_water_map, water_to_ligh_map, light_to_temp_map, temperature_to_humidity_map, humidity_to_location_map]
        for m in mappings:
            print(m)
            for x in m:
                new_ranges = []
                source_start = int(x[1])
                source_end = int(x[2]) + int(x[1])

                destination_start = int(x[0])
                destination_end = int(x[0]) + int(x[1])
                for start, end in ranges:
                    if end < source_start or start > source_end:
                        # just keep the same range 
                        #new_ranges.append((start, end))
                        pass
                    elif start < source_start:
                        new_ranges.append((start, source_start - 1))  # il primo pezzo rimane così come era
                        if end > source_end:
                            # converto fino a destination end
                            new_ranges.append((destination_start, destination_end))
                            # e lascio il resto così com'era
                            new_ranges.append((source_end, end))
                        else:
                            # converto fino a end
                            new_ranges.append((destination_start, end - source_start + destination_start))
                    else:
                        if end > source_end:
                            # converto fino a destination end
                            new_ranges.append((destination_start + start -source_start, destination_end))
                            # e lascio il resto così com'era
                            new_ranges.append((source_end, end))
                        else:
                            # sono tutto dentro
                            new_ranges.append((destination_start + start -source_start, end - source_start + destination_start))
                if len(new_ranges) == 0:
                    new_ranges.append((start, end))    
                ranges = new_ranges
                        # for seed in range(start if start > int(x[1]) else int(x[1]), end if end < int(x[2]) + int(x[1]) else int(x[2]) + int(x[1])):
                        #     if seed >= int(x[1]) and seed < int(x[2]) + int(x[1]):
                        #         seed = seed - int(x[1]) + int(x[0])
                        #     break
       
        for r in ranges:
            if r[0] < min_pos:
                min_pos = r[0]
        i += 2
        print(i)
    
    return min_pos


with open('2023/05/input.txt') as f:
    data = f.read().splitlines()
    data = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4""".split("\n")
    res = do(data)  
    print("Result should be (🤞):", res)
