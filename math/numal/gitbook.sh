cd ../weihuayi.github.io/
git pull

cd ../numal/
git add .
git commit -m "update" 
git push 
gitbook build
cp -r _book/* ../weihuayi.github.io/math/numal/
cd ../weihuayi.github.io/
git add .
git commit -m "update" 
git push 
