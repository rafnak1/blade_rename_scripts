import subprocess, json

defect_labels = ['leading edge;erosion;coating or LEP only', 'leading edge;erosion;continuous or deep', 'leading edge;erosion;spotty or laminate', 'leading edge;erosion;eroded tip', 'trailing edge;crack;superficial', 'surface;coating damage;superficial', 'trailing edge;crack;deep', 'surface;crack or laminate defect;superficial', 'surface;burn damage;superficial', 'surface;burn damage;deep']

def get_labels(meta_filename: str):
    with open(meta_filename) as f:
        meta = json.loads(f.read())
    return list(map(lambda shape: shape['label'], meta['shapes']))

def insert_prefix_to_filename(prefix, filename):
    path = filename[:filename.rfind('/')]
    file = filename[filename.rfind('/') + 1:]
    subprocess.run(['mv', filename, path + '/' + prefix + '_' + file])


output_images = subprocess.run(['find', '-name', '*.jpg'], stdout=subprocess.PIPE)
filenames_images = output_images.stdout.decode('utf-8').split()

output_meta = subprocess.run(['find', '-name', '*.json'], stdout=subprocess.PIPE)
filenames_meta = output_meta.stdout.decode('utf-8').split()

for filename in filenames_images:
    if filename.replace('jpg', 'json') in filenames_meta:
        labels = get_labels(filename.replace('jpg', 'json'))
        if set(defect_labels).intersection(labels):
            insert_prefix_to_filename('defect_' + '_'.join(sorted(labels)), filename)
        else:
            insert_prefix_to_filename('labeled_' + '_'.join(sorted(labels)), filename)
    else:
        insert_prefix_to_filename('unlabeled', filename)


