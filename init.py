#!/usr/bin/env python3

import argparse
import subprocess
import sys
from argparse import Namespace
from os import path
from typing import List
from urllib.parse import urlparse


install_dir = path.abspath(path.join(path.dirname(__file__), "plugins"))

plugins: List[str] = [
    "https://github.com/alexanderjeurissen/ranger_devicons.git"
]


def p_name(uri: str) -> str:
  url = urlparse(uri)
  name = path.basename(url.path)
  target, _ = path.splitext(name)
  return target


def install_plugin(uri: str) -> None:
  install_target = path.join(install_dir, p_name(uri))
  print(f"安装: {uri}")
  if path.isdir(install_target):
    subprocess.run(
        ["git", "pull"],
        cwd=install_target.encode(),
        stdout=sys.stdout,
        stderr=sys.stderr)
  else:
    subprocess.run(
        ["git", "clone", "--depth=1", uri,
         install_target],
        stdout=sys.stdout,
        stderr=sys.stderr)


def parse_args() -> Namespace:
  parser = argparse.ArgumentParser()
  parser.add_argument("-i", "--install", action="store_true", required=True)
  return parser.parse_args()


def main() -> None:
  args = parse_args()
  if not args.install:
    return
  for plugin in plugins:
    install_plugin(plugin)


main()
