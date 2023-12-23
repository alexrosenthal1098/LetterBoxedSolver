#!/bin/bash

cd /Users/alexrosenthal/LetterBoxedSolver

python3 src/collect_lb_words.py

git add docs/lb_words.txt
git commit -m "auto commit new words"
git push origin main