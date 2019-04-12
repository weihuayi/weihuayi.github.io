# update the site first
cd ../weihuayi.github.io/
git pull


cd ../whysite/
git add .
git commit -m "update" 
git pull
git push 
gitbook build
cp -r _book/* ../weihuayi.github.io/
cd ../weihuayi.github.io/
git add .
git commit -m "update" 
git push 
