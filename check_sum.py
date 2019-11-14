import glob
import re
import json

repo_dir = '/home/yonekura/Documents/pca-coinlabel/'
matricula_pattern = re.compile(repo_dir + '(\d{10})')
filename_pattern = re.compile('/(\d*)_\d*')
matriculas = [matricula_pattern.match(i).group(1) for i in glob.glob(repo_dir+'/*') if matricula_pattern.match(i) is not None]

matriculas.sort()


fingers = 0

for matricula in matriculas:
    json_pattern = re.compile(repo_dir + matricula + '(.*\.json)')
    files = [json_pattern.match(i).group(1) for i in glob.glob(repo_dir+matricula+'/*') if json_pattern.match(i) is not None]
    files.sort()
    print(matricula,'qtd:',len(files),end='')
    sum_error = 0
    for f in files:
        with open(repo_dir+matricula+'/'+f) as json_file:
            data = json.load(json_file)
            s = 0
            finger = False
            for d in data['shapes']:
                if d['label'] == 'finger':
                    finger = True
                    continue
                else:
                    s += int(d['label'])
            if finger:
                fingers+=1
            f_class = filename_pattern.search(f)
            if f_class is not None and int(f_class.group(1)) != s:
                sum_error+=1
    print(' erros:',sum_error,end='')
    print()

