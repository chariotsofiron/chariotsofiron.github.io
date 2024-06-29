install:
    brew install zola

run:
    zola serve

format:
    mdformat content
    fd -e md | xargs sd '\\\\\\\\' '\\'
