# VIM 

> Better, Stronger, Faster.

* vim 的精髓就在于命令键的组合，全键盘的操作，可以使你收不离开键盘输入区域即可完成
所有的操作。
* 其它编辑器一般是通过键盘和鼠标的组合来完成指定功能。

## Ubuntu 下的安装

```
sudo apt -y install vim vim-gtk
```
## 学习资源

1. [简明 VIM 练级攻略](https://coolshell.cn/articles/5426.html)
1. `vimtutor`

## 基本概念

### 模式
最常用的四个模式：

1. 普通模式(Normal mode)
1. 插入模式(Insert mode)
1. 可视模式(Visual mode)
1. 命令行模式(Command mode)

## VIM 内置常用功能

### Surrounding

```
ci[ 删除一对 [] 中的所有字符，并进入插入模式
ci( 删除一对 () 中的所有字符，并进入插入模式
ci< 删除一对 <> 中的所有字符，并进入插入模式
ci{ 删除一对 {} 中的所有字符, 并进入插入模式
ci" 删除一对 ""  中的所有字符，并进入插入模式
ci' 删除一对 '' 中的所有字符，并进入插入模式
ci` 删除一对 `` 中的所有字符，并进入插入模式
cit 删除一对 HTML/XML 标签内部的所有字符, 并进入插入模式
```

```
ci: 例如，ci(，或者ci)，将会修改()之间的文本
di: 剪切配对符号之间文本
yi: 复制
ca: 同ci，但修改内容包括配对符号本身
da: 同di，但剪切内容包括配对符号本身
ya: 同yi，但复制内容包括配对符号本身
dib: 同 di(
diB: 同 di{
```

## VIM 插件

### UltiSnips: https://github.com/SirVer/ultisnips ###

片段 (snippet) 是一段常用的文本片段，可能包含很多冗余的部分，如果每次都完整输入
，效率很低。UltiSnips 可以极大减少这种文本输入的击键次数，提高这类文本的输入效率。

#### Snippet 基本方法 ####

定义 Snippet 的语法如下：

```bash
snippet trigger_word ["description" [options] ] 
endsnippet
```

options 
1. i: 任何位置
1. r: 正则表达式
1. w:
1. A: 自动展开
1. b: 仅仅在一行的开头展开
1. !: 覆盖前面定义的同名片段 


* 插入当前的日期
```
snippet date
`!v strftime("%Y-%m-%d")`
endsnippet
```

**优先级**




### vim-surrounding: 

下面给出不同模式下的操作命令：

```
Normal mode
-----------
ds  - delete a surrounding
cs  - change a surrounding
ys  - add a surrounding
yS  - add a surrounding and place the surrounded text on a new line + indent it
yss - add a surrounding to the whole line
ySs - add a surrounding to the whole line, place it on a new line + indent it
ySS - same as ySs

Visual mode
-----------
s   - in visual mode, add a surrounding
S   - in visual mode, add a surrounding but place text on new line + indent it

Insert mode
-----------
<CTRL-s> - in insert mode, add a surrounding
<CTRL-s><CTRL-s> - in insert mode, add a new line + surrounding + indent
<CTRL-g>s - same as <CTRL-s>
<CTRL-g>S - same as <CTRL-s><CTRL-s>
```

下面给出一些示例，其中原始字符串中的 `*` 表示光标所在位置 

```
 Old text                  Command     New text ~
 "Hello *world!"           ds"         Hello world!
 [123+4*56]/2              cs])        (123+456)/2
 "Look ma, I'm *HTML!"     cs"<q>      <q>Look ma, I'm HTML!</q>
 if *x>3 {                 ysW(        if ( x>3 ) {
 my $str = *whee!;         vlllls'     my $str = 'whee!';
 <div>Yo!*</div>           dst         Yo!
 <div>Yo!*</div>           cst<p>      <p>Yo!</p>
```

## VIM 技巧

press `q` exit the record mode.

```
<>norm 4dw
```

```
%s/.*\n/\0\\\\\\hline\r/g
```
