# -*- coding: utf-8 -*-
"""GLAAD.

---
layout:     post
source:     GLAAD Media Reference Guide - 9th Edition
source_url: http://www.glaad.org/reference
title:      GLAAD Guidelines
date:       2016-07-06
categories: writing
---

This check looks for improper terms related to LGTQ issues. The
New York Times and Associated Press have also adopted this style guide.

"""
from proselint.tools import memoize, preferred_forms_check


@memoize
def check(text):
	"""Suggest preferred forms given the reference document."""
	err = "glaad.misc"
	msg = "Possibly offensive term. Use '{}' instead of '{}'."
	
	glaad_terms = [
	    [],
	]
	
	return preferred_forms_check(text, glaad_terms, err, msg, ignore_case=False)