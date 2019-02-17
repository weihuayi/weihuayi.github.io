git checkout master
git add .
git commit -m $1
git push 
cp -r _book/* ../weihuayi.github.io/
cd ../weihuayi.github.io/
git add .
git commit -m $1
git push 
git checkout master
