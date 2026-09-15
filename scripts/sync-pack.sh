#!/bin/bash
# Mirror Desktop pack <-> git pack/
set -euo pipefail
DESK="/mnt/c/Users/jbies/OneDrive/Desktop/Atlas of the Build Loop — Study Pack"
REPO="/home/jbies/Atlas-Learning-Forge/pack"
DIR="${1:-}"
if [[ "$DIR" == "to-git" ]]; then
  mkdir -p "$REPO"
  rsync -a --delete "$DESK/" "$REPO/"
  echo "synced Desktop -> $REPO"
elif [[ "$DIR" == "to-desktop" ]]; then
  mkdir -p "$DESK"
  rsync -a --delete "$REPO/" "$DESK/"
  echo "synced $REPO -> Desktop"
else
  echo "usage: $0 to-git | to-desktop" >&2
  exit 2
fi
