+++
title = "Give your keyboard an extra layer"
slug = "layer"
date = 2023-01-15
draft = true
+++

I remapped the caps-lock key on my keyboard to provide me with an extra layer for text editing.

![layer](/images/layer.png)


| Command     | Shortcut  | Key sequence                | Vim Equivalent |
| ----------- | --------- | --------------------------- | -------------- |
| select word | `fn+w`    | `right; opt+left; shift+opt+right` | `viw`   |
| select line | `fn+l`    | `cmd+left; shift+cmd+right` | `^v$`          |
| arrows      | `fn+jkl;` | `arrow key`                 | `hjkl`         |
| next line   |           | `cmd+right; return`         | `o`            |
| prev line   |           | `cmd+left; return; up`      | `shift+o`      |
| home        | `fn+h`    | `cmd+right`                 | `^`            |
| end         | `fn+'`    | `cmd+left`                  | `$`            |
| tap caps    | `fn`      | `esc`                       | N/A            |


- keyboard macros
- vim-like benefits in any textbox
- macOS substitutions (e.g. shrug, pro, con)

## Features I would like to add

- replace selected text with chatgpt response
- repeated selects extends selection


# Further reading

- https://getreuer.info/posts/keyboards/select-word/index.html
