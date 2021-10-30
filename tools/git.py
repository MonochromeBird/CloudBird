#!/usr/bin/env python
from subprocess import PIPE, call, check_output, Popen

class Repo:
	def __init__(self, clone: str, path: str, depth: int = 1):
		call(f'git clone {clone} {path} --depth {depth}', shell = True)
		self.path = path

	def commit(self, commit: str):
		call(f'cd {self.path} && g add .* * && g commit -m {commit}')

	def push(self):
		call(f'cd {self.path} && g push')

	def branch(self, branch: str, new: bool = False):
		call(f'cd {self.path} {f"g branch {branch}" if new else f"g checkout {branch}"}')
