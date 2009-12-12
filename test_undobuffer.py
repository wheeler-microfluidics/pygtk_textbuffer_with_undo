#!/usr/bin/env python
# -*- coding:utf-8 -*-

""" unit tests for gtk textbuffer with undo functionality """

# Copyright (C) 2009 Florian Heinle
# 
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
# 
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

import undobuffer
import unittest

class EmptyBufferTest(unittest.TestCase):
    """empty buffers shouldn't show any side effects when undoing"""
    def setUp(self):
        self.buf = undobuffer.UndoableBuffer()

    def test_undo(self):
        """test if undo on empty buffers has no sideeffects"""
        self.buf.undo()
        self.assertEqual(len(self.buf.undo_stack), 0)
        self.assertEqual(len(self.buf.redo_stack), 0)

    def test_redo(self):
        """test if redo on empty buffers has no sideeffects"""
        self.buf.redo()
        self.assertEqual(len(self.buf.undo_stack), 0)
        self.assertEqual(len(self.buf.redo_stack), 0)

class UndoKeyboardInsertTest(unittest.TestCase):
    """test when entering char after char like with keyboard input"""
    def setUp(self):
        self.buf = undobuffer.UndoableBuffer()
        test_string = "This is  a test\nstring"
        for char in test_string:
            self.buf.insert(self.buf.get_end_iter(), char)

    def test_can_undo(self):
        """test if can_undo gives correct result"""
        self.assertEqual(self.buf.can_undo, True)
    
    def test_cannot_redo(self):
        """test if can_redo gives correct negative result"""
        self.assertEqual(self.buf.can_redo, False)

    def test_correct_number(self):
        """test if merging happened correctly"""
        self.assertEqual(len(self.buf.undo_stack), 10)

    def test_undo(self):
        """test if undo works"""
        self.buf.undo()
        self.buf.undo()
        self.assertEqual(len(self.buf.undo_stack), 8)

    def test_can_redo_now(self):
        """test if can_redo gives positive result after undo"""
        self.buf.undo()
        self.assertEqual(self.buf.can_redo, True)

class UndoPasteInsertTest(unittest.TestCase):
    """insert multiple characters at once, like when pasting"""
    def setUp(self):
        self.buf = undobuffer.UndoableBuffer()
        test_string = "This will be pasted"
        self.buf.insert(self.buf.get_end_iter(), test_string)

    def test_only_one_undo(self):
        """test if pasting results in only one undo"""
        self.assertEqual(len(self.buf.undo_stack), 1)
    
    def test_undo(self):
        """test if undoing of that works"""
        self.buf.undo()
        self.assertEqual(len(self.buf.undo_stack), 0)

if __name__ == '__main__':
    unittest.main()
