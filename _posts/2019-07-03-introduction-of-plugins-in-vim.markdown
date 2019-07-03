---
layout: post
title: Introduction of Plugins In Vim
date: 2019-07-03 13:52:24.000000000 +09:00
---
There are many very nice plugins in vim, which make vim a very charming one. As I introduced at first, why people like vim, the most reliable reason is the powerful plugins in Vim.

## Vim-plug

Every great success begins with a dream, and why vim becomes great, I think it is because of vim-plug.
Vim-plug is very powerful vim plugin manager, very easy install and control. You can find a detail description [here](https://github.com/junegunn/vim-plug).
Here I cite some advantages introductions from vim-plug README <br>:
![image](https://raw.githubusercontent.com/junegunn/i/master/vim-plug/installer.gif)
- Easier to setup: Single file. No boilerplate code required.
- Easier to use: Concise, intuitive syntax
- [Super-fast][40/4] parallel installation/update
  (with any of `+job`, `+python`, `+python3`, `+ruby`, or [Neovim][nv])
- Creates shallow clones to minimize disk space usage and download time
- On-demand loading for [faster startup time][startup-time]
- Can review and rollback updates
- Branch/tag/commit support
- Post-update hooks
- Support for externally managed plugins

The use of vim-plug:<br>
Add these lines in your vimrc:
```vim
Plug 'your plugins here'
" for example, install the vim-airline (a vim theme)
Plug 'vim-airline/vim-airline'
```

## MarkdownPreview

MarkdownPrefview can help you edit and show your markdown file at the same time. After the installation, you can just input:
```vim
:MarkdownPreview
```
and enter. To set the rapid key, you can set like this:
```vim
map <LEADER>t :MarkdownPreview<CR>
```
In this way you can enter the explorer to see the output of your markdown file.
> There is something we need to know about the markdown.
1. Markdown only supports vim >= 8.1 ver.
   markdown
2. There are some default settings of MarkdownPreview:

```vim
let g:mkdp_auto_start = 0
let g:mkdp_auto_close = 1
let g:mkdp_refresh_slow = 0
let g:mkdp_command_for_global = 0
let g:mkdp_open_to_the_world = 0
let g:mkdp_open_ip = ''
let g:mkdp_browser = ''
let g:mkdp_echo_preview_url = 0
let g:mkdp_browserfunc = ''
let g:mkdp_preview_options = {
    \ 'mkit': {},
    \ 'katex': {},
    \ 'uml': {},
    \ 'maid': {},
    \ 'disable_sync_scroll': 0,
    \ 'sync_scroll_type': 'middle',
    \ 'hide_yaml_meta': 1
    \ }
let g:mkdp_markdown_css = ''
let g:mkdp_highlight_css = ''
let g:mkdp_port = ''
let g:mkdp_page_title = '「${name}」'
```
I just copied them here, you can also just copy them to your vimrc to set the MarkdownPreview plugin.<br>
Look at this line:
```vim
let g:mkdp_browserfunc = ''
```
You can set your expolorer here, and you can just leave this place blank, escape from some other troubles.
And now, you can enjoy your happy input and explore your post at the same time.

