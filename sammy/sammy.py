#!/usr/bin/env python3

import click
import re
import sys
import shutil
import os
from pathlib import Path
import subprocess


def get_sjsu_dev2_path():
  # Get the user's home directory where the SJSU-Dev2's location file should
  # live
  home = str(Path.home())

  # Open the .sjsu_dev2.mk and read its contents
  root_mk_file = open(f'{home}/.sjsu_dev2.mk', 'r')
  root_mk_contents = root_mk_file.read()

  # Use regex to parse just for the location variable
  m = re.search('SJSU_DEV2_BASE[ ]*= (.*)', root_mk_contents)
  base_path = m.group(1)

  return base_path


@click.group()
def main():
  """
  Sammy is a tool for managing SJSU-Dev2 firmware projects and to install
  external packages such as platforms and libraries.
  """
  pass


@main.group()
def platform():
  """
  Install, update, and configure the SJSU-Dev2 platform settings.
  """
  pass


@platform.command()
def install():
  """
  Install SJSU-Dev2 on your computer.
  """
  print("I install SJSU-Dev2 in your home directory")


@platform.command()
def update():
  """
  Update SJSU-Dev2 on your computer.

  This works even if you did not install SJSU-Dev2 in the home directory.
  """
  platform_path = get_sjsu_dev2_path()

  # Returns just the branch name of the current branch being used in SJSU-Dev2
  proc = subprocess.Popen(['git', 'rev-parse', '--abbrev-ref', 'HEAD'],
                          stdout=subprocess.PIPE,
                          cwd=platform_path)

  current_branch = proc.stdout.read()

  if current_branch != b'master\n':
    print('SJSU-Dev2 must be on the master branch to be updated!')
    print(f'>> Current branch is: {current_branch.decode("utf-8")}')
    return

  print('Updating SJSU-Dev2 ...\n')

  subprocess.Popen(['git', 'pull', 'origin', 'master'],
                   stdout=sys.stdout,
                   stderr=sys.stderr,
                   cwd=platform_path).communicate()


@main.group()
def project():
  """
  Start and configure firmware projects
  """
  pass


@project.command()
@click.argument('project_name')
def start(project_name):
  """
  Start a new firmware project.
  """
  platform_path = get_sjsu_dev2_path()

  try:
    shutil.copytree(f'{platform_path}/projects/starter/', project_name)
    print(f'Creating firmware project in "{project_name}" directory')
  except FileExistsError:
    sys.exit((f'Failed to create project, project directory "{project_name}" '
            'already exists'))


@main.command()
def build():
  """
  Build projects firmware
  """
  print("Not implemented.")


if __name__ == "__main__":
  main()