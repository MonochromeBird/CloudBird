#!/usr/bin/env python3
import re
def links(link: str) -> bool:
	if not link: return False
	regex = re.compile(
	r'^((https|http|tcp|utp|ftp|file)?://)?'
	r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'
	r'localhost||'r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
	r'(?::\d+)?'  r'(?:/?|[/?]\S+)$', re.IGNORECASE)
	return bool(regex.search(link))