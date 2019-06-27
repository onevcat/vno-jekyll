---
layout: post
title: Some Basic Operations of Vim
date: 2019-06-26 19:11:24.000000000 +09:00
---

#### Where I got to know vim

When I am searching videos at Bilibili, I found an upper, 'TheCW', showed a very nice video to introduce how to use the vim [the link](http://www.bilibili.com/video/av55498503?from=search&seid=9399177761934796555).

#### The advantage of vim

> Actually, I ever learned vim from some basic introduction aticle, and I ever thought it was a very unique editor, but not a good one. I can imagine at some very old age without a mouse, there must be a keyboard leading editor make some words out, but why still pre-installed in kinds of Unix based os today? I found myself too young (not young enough actually :() too simple. Vim is a very powerful txt editor in Unix. How powerful? 

First all, all operations could be apart from the mouse. Some people may feel strange, why this can be called an advantage, because the mouse provide us a convenient way to solve some problems. But in fact, when I have tried the vim to process data totally via the keyboard, something interesting has happened to me. This is a feeling of fluent, a kind of feeling that make you feel that you can control everything here. Every moves will give you a response, and every response will make you know what you're doing now. 

Secondly, unexpected high level freedom for the plug-in setting. In my opinion, the greatest quality of linux is you can make linux you like. Vim inherits this spirit. A open, free, and big community forum exits, and you can download the plug-ins very easily.

Thirdly, a built-in keyboard macro can help work change to be extremly high efficiency. Some operations may be complex will be an easy thing to be done. You can imagine the boring repetition in your daily work will be elegantly avoided. What a happiness :).

#### Some basic operations on vim

| i  | enter insert mode                   |
|----|-------------------------------------|
| a  | insert after the cursor             |
| A  | insert at the last of the line      |
| I  | insert at the beginning of the line |
| o  | insert at the next line             |
| O  | insert at the beginning of the line |
| x  | delete character at the cursor      |
| d  | cut the character at the cursor     |
| dd | cut the whole line                  |

| N/A | normal mode                                          |
|-----|------------------------------------------------------|
| c   | delete character at the cursor and enter insert mode |
| w   | move the cursor to the next word                     |
| b   | move the cursor back to the previous word            |
| y   | copy                                                 |
| p   | paste                                                |

All the operations above can be made in to a mode like this:

> operation + motivation

For example:

d --> means cut the next character

cw --> means cut the next word and enter the insert mode

ciw --> means cut the present word and enter the insert mode 

> PS(Only show myself this message, the visitor, you, don't need care about it): Because I have made the i -> u, so in mine: ciw = cuw

#### Finally

Today I only introduced some very very basal operations. In fact, the most interesting part of vim, I think, is the configuration of vimrc as well as the plug in system. I will show you in the next post.

If you are not a freshbird like me, I share a configuration of mine, and you can configurate yourself immediately.

> [zququ-configuration](https://github.com/zququ/vim-configuration)
