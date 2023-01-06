import os
import os.path
import shutil

def main():
    rootDir = os.path.abspath(".")
    rootDirLen = len(rootDir.split(os.sep))
    destRootDir = '/usr/local/eliozoapp'
    for root, dirs, files in os.walk(rootDir):
        path = root.split(os.sep)
        if len(path) < rootDirLen:
            continue
        if len(path) > rootDirLen and path[rootDirLen] in ['tests', 'venv', 'instance']:
            continue
        if len(path) > rootDirLen+1 and path[rootDirLen+1] == '__pycache__':
            continue
        for file in files:
            extension = os.path.splitext(file)[1].lower()
            if extension in ['.cfg', '.in', '.ini', '.py', '.html'] or (len(path) > rootDirLen+2 and path[rootDirLen+2] in ['reveal.js.40', 'algorithms-slides']):
                srcpath = list(path)
                srcpath.append(file)
                #destpath = ['c:', 'Users', 'kapsitis', 'tmp']
                destpath = destRootDir.split(os.sep)
                destpath = destpath + srcpath[rootDirLen:]
                print('Copying ' + '/'.join(srcpath))
                print('  to file ' + '/'.join(destpath))
                os.makedirs(os.path.dirname('/'.join(destpath)), exist_ok=True)
                shutil.copyfile('/'.join(srcpath), '/'.join(destpath))

if __name__ == '__main__':
    main()