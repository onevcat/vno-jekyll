---
layout: post
title: Some Keyboard Setting of Vim
date: 2019-07-02 19:39:24.000000000 +09:00
---
Keyboard setting is something boring in vim, and tell you the truth, it's a little complex. However, vim setting is essential to us. I use the vim aimed to increase the efficiency of my daily writing, including blog and coding. And the keyboard setting is no doubly the most important.<br>
## The vimrc build
The keyboard setting of vim, is similar to the setting of terminal bashrc. Make a folder named with **`vim`** and create the **`vimrc`** document.
```bash
$mkdir ~/.vim && cd .vim
$touch vimrc
```
And then a vimrc will be created.<br>
> One tricky thing I want to say is how to quickly set your vim. Maybe it's a little early to talk about it, I recommend that you can skip this at first.<br> 

As vim is a very small and easy taken word editor, you may want to set up your vim more easily. And you can upload your vim setting to the github and setup vim on any computer you like. I got a very cool code to auto-detect if there is a vimrc, if your vimrc isn't set, this code will help you set your vim.

```bash
if empty(glob('~/.vim/autoload/plug.vim'))
  silent !curl -fLo ~/.vim/autoload/plug.vim --create-dirs
    \ https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
  autocmd VimEnter * PlugInstall --sync | source $MYVIMRC
endif
```
As all the plugin will be plugged by the [Vim plugin manager](https://github.com/junegunn/vim-plug) and a file named plug.vim will be downloaded in `/autoload`. Copy the this code to your vimrc, and if your computer didn't get your `/autoload/plug.vim` it will auto-install all of the plugins from the github. Cool!

## The Keyboard setting
Next we will enter our topic. Two commands will help you resolve the keyboard setting. 
```vim
noremap 
&
map
```

noremap is an easy command to change the simple key group. For example,
```vim
noremap u i 
```
It will simply help you change i to u.
<br>The other command **`map`** is more powerful and can handle more complex work. For example,
```vim
map <LEADER>rc :e ~/.vim/vimrc<CR>
```
Means to set **`<LEADER> + r + c`** can help you edit vimrc document directly.<br>
As I introduced [before](../2019-06-26-basic-op-vim.markdown), **`operation + motivation`** will help you make a more flexible setting like,
```vim
map <LEADER><LEADER> <Esc>/<++><CR>:nohlsearch<CR>c4l
```
 Means when you tap **`<LEADER> + <LEADER>`**, will at first execute **`Esc`** command, and then search for **`<++>`** (some defined tag working as a place holder), then execute **`:nohlsearch`** to cancel highlight search mode and change the 4 units on the right (**`c4l`**) .


