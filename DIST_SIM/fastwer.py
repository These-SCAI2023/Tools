#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 16:44:38 2021

@author: antonomaz
"""

import fastwer


hypo = ['This is an example .', 'This is another example .']
ref = ['This is the example :)', 'That is the example .']

# Corpus-Level WER: 40.0
fastwer.score(hypo, ref)
# Corpus-Level CER: 25.5814
fastwer.score(hypo, ref, char_level=True)

# Sentence-Level WER: 40.0
fastwer.score_sent(hypo[0], ref[0])
# Sentence-Level CER: 22.7273
fastwer.score_sent(hypo[0], ref[0], char_level=True)