import subprocess, json

def get_metadata():
    result = subprocess.run(['find', '-name', '*.json'], stdout=subprocess.PIPE)
    filenames = result.stdout.decode('utf-8').split()
    
    metadata_list = []
    for filename in filenames:
        with open(filename) as f:
            metadata_list.append(json.loads(f.read()))
    
    return metadata_list
    
metadata_list = get_metadata()

label_hist = {}

for metadata in metadata_list:
    for shape in metadata['shapes']:
        label = shape['label']
        if label in label_hist:
            label_hist[label] += 1
        else:
            label_hist[label] = 1

for key, value in label_hist.items():
    print(f'{key}: {value}')
