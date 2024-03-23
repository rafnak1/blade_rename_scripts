import subprocess

output_images = subprocess.run(['find', '-name', '*.jpg'], stdout=subprocess.PIPE)
filenames_images = output_images.stdout.decode('utf-8').split()

output_meta = subprocess.run(['find', '-name', '*.json'], stdout=subprocess.PIPE)
filenames_meta = output_meta.stdout.decode('utf-8').split()

for filename in filenames_images:
    if filename.replace('jpg', 'json') in filenames_meta:
        
        subprocess.run(['mv', filename, './' + 'labeled_' + filename[2:]])
    else:
        subprocess.run(['mv', filename, './' + 'unlabeled_' + filename[2:]])


