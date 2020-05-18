#!/usr/bin/env python3

import argparse
import subprocess
import sys
from argparse import Namespace
from os import path
from typing import List
from urllib.parse import urlparse

work_dir = path.abspath(path.dirname(__file__))
install_dir = path.join(work_dir, "plugins")
spec_file = path.join(work_dir, "plugins.txt")


def read_lines(path: str) -> List[str]:
  with open(path, "r") as fd:
    return fd.readlines()


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
  plugins = read_lines(spec_file)
  for plugin in plugins:
    install_plugin(plugin)


main()
