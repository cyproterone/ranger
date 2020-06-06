#!/usr/bin/env python3

from argparse import ArgumentParser, Namespace
from os.path import abspath, basename, dirname, isdir, join, splitext
from subprocess import run
from typing import List
from urllib.parse import urlparse


work_dir = dirname(abspath(dirname(__file__)))
install_dir = join(work_dir, "plugins")
spec_file = join(work_dir, "plugins.txt")


def read_lines(path: str) -> List[str]:
  with open(path, "r") as fd:
    return fd.readlines()


def p_name(uri: str) -> str:
  url = urlparse(uri)
  name = basename(url.path)
  target, _ = splitext(name)
  return target


def install_plugin(uri: str) -> None:
  install_target = join(install_dir, p_name(uri))
  print(f"安装: {uri}")
  if isdir(install_target):
    run(["git", "pull"],
        cwd=install_target.encode())
  else:
    run(["git", "clone", "--depth=1", uri,
         install_target])


def parse_args() -> Namespace:
  parser = ArgumentParser()
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
