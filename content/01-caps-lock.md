+++
title = "Making caps-lock more useful"
slug = "caps-lock"
date = 2023-01-15
+++

I remapped the `caps-lock` key on my keyboard to `fn` and bound several useful shortcuts around it.

![layer](/images/layer.png)

Here's a description of what they do

| Command     | Shortcut          | Key sequence                       | Vim       |
| ----------- | ----------------- | ---------------------------------- | --------- |
| select word | `fn+d`            | `right; opt+left; shift+opt+right` | `viw`     |
| extend word | `(fn)+d`          | `shift+opt+right`                  | `e`       |
| select line | `fn+f`            | `cmd+left; shift+cmd+right`        | `^v$`     |
| extend line | `(fn)+d`          | `shift+down; shift+cmd+right`      | `j$`      |
| arrows      | `fn+jkl;`         | `arrow key`                        | `hjkl`    |
| line below  | `fn+return`       | `cmd+right; return`                | `o`       |
| line above  | `fn+shift+return` | `cmd+left; return; up`             | `shift+o` |
| home        | `fn+h`            | `cmd+right`                        | `^`       |
| end         | `fn+'`            | `cmd+left`                         | `$`       |
| tap caps    | `fn`              | `esc`                              | N/A       |
| caps-lock   | `fn+escape`       | `caps-lock`                        | N/A       |


## How I did it

I used Karabiner-elements, a keyboard customization program for macOS. Bindings are configured tediously with a json file. Here's the config for select/extend word:

```json
{
    "description": "a = select word",
    "type": "basic",
    "from": {"key_code": "a", "modifiers": {"mandatory": ["fn"]}},
    "to": [
        {"key_code": "right_arrow"},
        {"key_code": "left_arrow", "modifiers": ["option"]},
        {"key_code": "right_arrow", "modifiers": ["shift", "option"]},
        {"set_variable": {"name": "word_pressed", "value": 1}}
    ],
    "conditions": [
        {"type": "variable_if", "name": "word_pressed", "value": 0}
    ]
},
{
    "description": "multi-tap a = extend word selection",
    "type": "basic",
    "from": {"key_code": "a", "modifiers": {"mandatory": ["fn"]}},
    "to": [
        {"key_code": "right_arrow", "modifiers": ["shift", "option"]}
    ],
    "conditions": [
        {"type": "variable_if", "name": "word_pressed", "value": 1}
    ]
},
```


## How you can do it yourself

1. Install karabiner-elements (`brew install karabiner-elements`)
2. Copy the config into complex modifications folder of karabiner-elements `~/.config/karabiner/assets/complex_modifications/`


# Further reading

- https://getreuer.info/posts/keyboards/select-word/index.html
- http://capslock.vonng.com/
- [Karabiner-elements key codes](https://github.com/pqrs-org/Karabiner-Elements/blob/main/src/apps/SettingsWindow/Resources/simple_modifications.json)