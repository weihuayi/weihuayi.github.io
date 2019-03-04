<div id="container"></div>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/theme-next/theme-next-gitment@1/default.css"/>
<script src="https://cdn.jsdelivr.net/gh/theme-next/theme-next-gitment@1/gitment.browser.js"></script>

<script>
var gitment = new Gitment({
  id: 'window.location.pathname', // 可选。默认为 location.href
  owner: 'weihuayi',
  repo: 'weihuayi.github.io',
  oauth: {
    client_id: '7dd9c9fc3ac45352b55b',
    client_secret: '4e6f74b82a7ac18671c7e9e0d17a1ceb9359a5ad',
  },
})
gitment.render('container')
</script>
